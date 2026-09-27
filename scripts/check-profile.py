#!/usr/bin/env python3
"""Drift check for this profile repository.

Standard library only. Exit code 1 on any finding, so it can gate a pull request.

Checks:
  1. Every relative Markdown link in README.md and case-studies/*.md resolves to a file.
  2. Every case study is linked from README.md, and every case study links back to at
     least one sibling in its "Related" line (or the body).
  3. Load-bearing facts read identically everywhere they are stated, and phrases that
     have already drifted once are not reintroduced.
  4. The machine-readable YAML block in README.md agrees with the prose on the facts
     listed in FACTS.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CASE_DIR = ROOT / "case-studies"

# Each fact: a phrase that must appear in every listed file. Add a fact when the same
# claim is stated in more than one place; the check then makes disagreement a failure.
FACTS: list[tuple[str, list[str]]] = [
    ("Senior Product Manager, Cubic Transportation Systems", ["README.md"]),
    ("Senior Technical Project Manager", ["README.md", "case-studies/deutschland-ticket-turnaround.md"]),
    ("1.6 to 4.0", ["README.md"]),
    ("€2M+", ["README.md", "case-studies/deutschland-ticket-turnaround.md"]),
    ("3M+", ["README.md", "case-studies/deutschland-ticket-turnaround.md", "case-studies/open-loop-payments-end-to-end.md"]),
    ("€5M+ B2G", ["README.md", "case-studies/deutschland-ticket-turnaround.md"]),
    ("US, Canada and Oceania", ["README.md", "case-studies/open-loop-payments-end-to-end.md"]),
    ("not in EMEA yet", ["README.md", "case-studies/open-loop-payments-end-to-end.md"]),
    ("approved by the CPO", ["README.md"]),
    ("v1.0 is targeted for March 2027", ["README.md"]),
    ("stopped the German launch in early 2020", ["README.md", "case-studies/banking-act-to-specifications.md"]),
    ("employed or freelance", ["README.md"]),
    ("Sabbatical", ["README.md"]),
    ("Pause during COVID", ["README.md"]),
]

# Phrases that drifted once and must not come back. Pair each with the reason.
FORBIDDEN: list[tuple[str, str]] = [
    ("global remit", "Umo operates in the US, Canada and Oceania; say that instead"),
    ("EMEA payment sovereignty", "Umo is not in EMEA yet; describe the compliance groundwork"),
    ("digital-mobility portfolio", "it was one program, not a portfolio"),
    ("Directed a €5M+", "led delivery of a program; did not direct a portfolio"),
    ("EPI) digital-identity", "the identity layer is EU digital identity, EPI is the payment rail"),
    ("hidden instructions", "reads as a tell to screening tools and adds nothing for people"),
    ("Not on the market", "open to mandates, employed or freelance; the old line blocked both"),
    ("$215M", "the Nuance acquisition happened after the role ended"),
    ("PMO advisor", "the role was PMO officer and assistant to the director"),
    ("Users voted that rating change", "the rating followed product fixes and a well-timed review prompt; say so"),
    ("refute-prompted votes", "say what cast the votes and who reviewed them"),
    ("community layer", "no second contributor yet; it is a data layer designed for community"),
]

# YAML keys whose value must contain a phrase that also appears in the README prose.
YAML_AGREEMENT: list[tuple[str, str]] = [
    ("current_role", "Senior Product Manager, Cubic Transportation Systems"),
    ("current_role", "at Cubic since 2021"),
    ("experience_years", "15+"),
    ("location", "Frankfurt am Main"),
]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FINDINGS: list[str] = []


def finding(msg: str) -> None:
    FINDINGS.append(msg)


def md_files() -> list[Path]:
    return [README, *sorted(CASE_DIR.glob("*.md"))]


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def check_links() -> None:
    for f in md_files():
        for target in LINK_RE.findall(f.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = (f.parent / target.split("#", 1)[0]).resolve()
            if not path.exists():
                finding(f"{rel(f)}: link target does not exist: {target}")


def check_cross_links() -> None:
    readme = README.read_text(encoding="utf-8")
    studies = sorted(CASE_DIR.glob("*.md"))
    for s in studies:
        if f"case-studies/{s.name}" not in readme:
            finding(f"README.md does not link {rel(s)}")
        body = s.read_text(encoding="utf-8")
        siblings = [o.name for o in studies if o != s]
        if not any(name in body for name in siblings):
            finding(f"{rel(s)} links no sibling case study")


def check_facts() -> None:
    for phrase, files in FACTS:
        for name in files:
            text = (ROOT / name).read_text(encoding="utf-8")
            if phrase not in text:
                finding(f"{name}: expected fact missing: {phrase!r}")
    for f in md_files():
        text = f.read_text(encoding="utf-8")
        for phrase, why in FORBIDDEN:
            if phrase in text:
                finding(f"{rel(f)}: drifted phrase present: {phrase!r} ({why})")


def yaml_block() -> str:
    m = re.search(r"```yaml\n(.*?)```", README.read_text(encoding="utf-8"), re.S)
    if not m:
        finding("README.md: machine-readable YAML block not found")
        return ""
    return m.group(1)


def check_yaml_agreement() -> None:
    block = yaml_block()
    if not block:
        return
    readme = README.read_text(encoding="utf-8")
    prose = readme.replace(block, "")
    # Join folded continuation lines so a value can be matched as one string.
    flat = re.sub(r"\n\s+", " ", block)
    for key, phrase in YAML_AGREEMENT:
        m = re.search(rf"^{re.escape(key)}:\s*(.*)$", flat, re.M)
        if not m:
            finding(f"README.md yaml: key missing: {key}")
            continue
        if phrase not in m.group(1):
            finding(f"README.md yaml: {key} does not contain {phrase!r}: {m.group(1).strip()!r}")
        if phrase not in prose:
            finding(f"README.md prose: yaml value for {key} not stated in prose: {phrase!r}")
    # Every case study cited in open_source or highlights must exist on disk when relative.
    for name in re.findall(r"case-studies/[\w-]+\.md", block):
        if not (ROOT / name).exists():
            finding(f"README.md yaml: cites missing file {name}")


def main() -> int:
    check_links()
    check_cross_links()
    check_facts()
    check_yaml_agreement()
    if FINDINGS:
        print(f"RED: {len(FINDINGS)} finding(s)")
        for f in FINDINGS:
            print(f"  - {f}")
        return 1
    print("GREEN: links resolve, case studies cross-link, facts agree, YAML matches prose")
    return 0


if __name__ == "__main__":
    sys.exit(main())
