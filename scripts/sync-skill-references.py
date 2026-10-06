#!/usr/bin/env python3
"""Copy or check the shared reference files inside each skill.

The Markdown files in ``references/`` at the plugin root are the copies to
edit. A skill reads those guides through relative links. Each skill folder
keeps an identical copy of every shared guide it reaches, including guides
linked from those files. The skill folder then still resolves those links
when it is copied on its own.

Links from one skill to a sibling skill, such as ``../grill-me-workflow/SKILL.md``,
are not copied. GitHub Actions runs this script with ``--check`` on pull
requests. See ``.github/workflows/check-shared-guides.yml``.

Edit a file under ``references/``, then run::

    python3 scripts/sync-skill-references.py
    python3 scripts/sync-skill-references.py --check

``--check`` changes nothing and exits 1 when a skill copy is missing or
differs from the plugin-root file.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "references"
SKILLS = ROOT / "skills"

LINK_RE = re.compile(r"\[[^]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def fail(message: str) -> None:
    print(f"sync-skill-references: {message}", file=sys.stderr)
    raise SystemExit(2)


def strip_fences(text: str) -> str:
    return FENCE_RE.sub("", text)


def link_path(raw: str) -> str | None:
    """Return a local relative path, or None for external and anchor links."""
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")].strip()
    if not target or target.startswith("#"):
        return None
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    # A Markdown title may follow the path: (file.md "title").
    if not target.startswith(("http://", "https://")) and " " in target:
        target = target.split()[0]
    target = target.split("#", 1)[0].strip()
    if not target:
        return None
    return target


def links_in(path: Path) -> list[str]:
    text = strip_fences(path.read_text(encoding="utf-8"))
    found = []
    for raw in LINK_RE.findall(text):
        target = link_path(raw)
        if target is not None:
            found.append(target)
    return found


def is_inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError:
        return False
    return True


def sibling_skill_file(skill: Path, resolved: Path) -> bool:
    """True when resolved is a file path inside a different skill folder."""
    try:
        relative = resolved.resolve().relative_to(SKILLS.resolve())
    except ValueError:
        return False
    if not relative.parts:
        return False
    other = relative.parts[0]
    if other == skill.name:
        return False
    return (SKILLS / other).is_dir()


def shared_name(skill: Path, source: Path, link: str) -> str | None:
    """Return the canonical filename when link points at a shared guide."""
    name = Path(link).name
    canon = CANON / name
    if not canon.is_file():
        return None
    resolved = (source.parent / link).resolve()
    skill_copy = (skill / "references" / name).resolve()
    canon_resolved = canon.resolve()
    if resolved == canon_resolved or resolved == skill_copy:
        return name
    return None


def closure(skill: Path) -> tuple[list[str], list[str], list[str]]:
    """Walk skill links and return shared filenames, sibling links, problems."""
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        return [], [], [f"{skill.name} has no SKILL.md"]

    shared: list[str] = []
    siblings: list[str] = []
    problems: list[str] = []
    seen_sources: set[Path] = set()
    queue: list[tuple[Path, Path | None]] = [(skill_md, None)]

    while queue:
        source, via = queue.pop(0)
        resolved_source = source.resolve()
        if resolved_source in seen_sources:
            continue
        if not source.is_file():
            problems.append(f"{skill.name} missing linked file {source}")
            continue
        seen_sources.add(resolved_source)

        for link in links_in(source):
            name = shared_name(skill, source, link)
            if name is not None:
                if name not in shared:
                    shared.append(name)
                    queue.append((CANON / name, source))
                continue

            resolved = (source.parent / link).resolve()
            if sibling_skill_file(skill, resolved):
                label = f"{skill.name}: {source.relative_to(ROOT)} -> {link}"
                if label not in siblings:
                    siblings.append(label)
                if not resolved.is_file():
                    problems.append(f"{label} does not resolve in this plugin")
                continue

            if is_inside(resolved, skill) and resolved.is_file():
                queue.append((resolved, source))
                continue

            where = source.relative_to(ROOT)
            problems.append(f"{where} link does not resolve: {link}")

    return shared, siblings, problems


def standalone_problems(skill: Path) -> list[str]:
    """Report links that a copied skill folder could not resolve itself.

    Sibling skill links are allowed to leave the folder. Every other relative
    link must land on a file inside the skill folder.
    """
    problems = []
    files = [skill / "SKILL.md"]
    reference_dir = skill / "references"
    if reference_dir.is_dir():
        files.extend(sorted(reference_dir.glob("*.md")))

    for source in files:
        if not source.is_file():
            continue
        for link in links_in(source):
            resolved = (source.parent / link).resolve()
            if is_inside(resolved, skill):
                if not resolved.is_file():
                    problems.append(
                        f"{skill.name} standalone missing {source.relative_to(skill)} -> {link}"
                    )
                continue
            if sibling_skill_file(skill, resolved) and resolved.is_file():
                continue
            problems.append(
                f"{skill.name} link leaves the skill folder: {source.relative_to(skill)} -> {link}"
            )
    return problems


def extra_shared_copies(skill: Path, expected: set[str]) -> list[Path]:
    reference_dir = skill / "references"
    if not reference_dir.is_dir():
        return []
    extras = []
    for path in sorted(reference_dir.glob("*.md")):
        if (CANON / path.name).is_file() and path.name not in expected:
            extras.append(path)
    return extras


def main(argv: list[str]) -> int:
    if argv[1:] not in ([], ["--check"]):
        fail("usage: scripts/sync-skill-references.py [--check]")
    check_only = argv[1:] == ["--check"]

    if not CANON.is_dir():
        fail(f"missing canonical directory {CANON}")
    if not SKILLS.is_dir():
        fail(f"missing skills directory {SKILLS}")

    skills = sorted(path for path in SKILLS.iterdir() if (path / "SKILL.md").is_file())
    if not skills:
        fail("no skills found")

    problems: list[str] = []
    actions: list[str] = []
    sibling_lines: list[str] = []

    for skill in skills:
        shared, siblings, link_problems = closure(skill)
        problems.extend(link_problems)
        sibling_lines.extend(siblings)
        expected = set(shared)
        reference_dir = skill / "references"

        if check_only:
            for name in shared:
                dest = reference_dir / name
                src = CANON / name
                if not dest.is_file():
                    problems.append(f"{skill.name} is missing references/{name}")
                elif dest.read_bytes() != src.read_bytes():
                    problems.append(
                        f"{skill.name}/references/{name} differs from references/{name}"
                    )
            for extra in extra_shared_copies(skill, expected):
                problems.append(
                    f"{skill.name}/references/{extra.name} is not reached by the skill's links"
                )
        else:
            if shared:
                reference_dir.mkdir(parents=True, exist_ok=True)
            for name in shared:
                src = CANON / name
                dest = reference_dir / name
                data = src.read_bytes()
                if not dest.is_file() or dest.read_bytes() != data:
                    shutil.copyfile(src, dest)
                    actions.append(f"updated {skill.name}/references/{name}")
            for extra in extra_shared_copies(skill, expected):
                extra.unlink()
                actions.append(f"removed {skill.name}/references/{extra.name}")

        problems.extend(standalone_problems(skill))

    print("Shared reference copies:")
    for skill in skills:
        shared, _, _ = closure(skill)
        names = ", ".join(shared) if shared else "(none)"
        print(f"  {skill.name}: {names}")

    if sibling_lines:
        print("Sibling skill links kept as links:")
        for line in sibling_lines:
            print(f"  {line}")

    if actions:
        print("Changes:")
        for action in actions:
            print(f"  {action}")
    elif not check_only:
        print("Copies already matched references/.")

    if problems:
        print("Problems:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    print("OK" if check_only else "Sync complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
