#!/usr/bin/env python3
"""Static integrity checks for a Markdown-only cycling Skill. No dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = list(ROOT.rglob("*.md"))
failures = []
if not (ROOT / "SKILL.md").exists():
    failures.append("missing root SKILL.md")
else:
    if not (ROOT / "SKILL.md").read_text(encoding="utf-8").startswith("---\n"):
        failures.append("SKILL.md must start with YAML frontmatter")

pat = re.compile(r"\]\(([^)]+)\)")
for doc in MARKDOWN:
    text = doc.read_text(encoding="utf-8")
    for link in pat.findall(text):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_text = link.split("#", 1)[0].split("?", 1)[0]
        if not path_text:
            continue
        target = (doc.parent / path_text).resolve()
        if not target.exists():
            failures.append(f"{doc.relative_to(ROOT)} -> missing {path_text}")

source = "\n".join(p.read_text(encoding="utf-8") for p in MARKDOWN)
banned = {
    "wrong IF formula": r"IF\s*=\s*平均功率\s*÷\s*FTP",
    "forced sodium prescription": r"必须补充.*钠500-700mg/h",
    "universal indoor FTP higher": r"典型差异.*室内FTP比室外高",
}
for title, pattern in banned.items():
    if re.search(pattern, source):
        failures.append(title)

if "IF = NP" not in source and "IF = NP ÷" not in source:
    failures.append("expected corrected IF definition")
for required in ["references/multisource_coaching.md", "references/return_to_riding.md"]:
    if not (ROOT / required).exists():
        failures.append(f"missing required document {required}")

# Codex-first metadata and legacy platform checks
if not (ROOT / "agents/openai.yaml").exists():
    failures.append("missing Codex interface metadata expected by this repository")
if re.search(r"(?i)(?:openclaw|qclaw|\\.qclaw)", source):
    failures.append("outdated platform branding in Markdown")
if not (ROOT / "AGENTS.md").exists():
    failures.append("missing Codex maintenance guidance")

if failures:
    print("Skill validation failed:")
    for failure in failures:
        print(" - " + failure)
    sys.exit(1)

print(f"Skill validation passed: {len(MARKDOWN)} Markdown files, links and key invariants.")
