#!/usr/bin/env python3
"""Static integrity checks for a Markdown-only cycling Skill. No dependencies."""
from pathlib import Path
import json
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

# Codex / Agent Skills identity and optional metadata checks.
skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
frontmatter_match = re.match(r"\A---\n(.*?)\n---\n", skill_text, flags=re.S)
if not frontmatter_match:
    failures.append("invalid or missing SKILL.md YAML frontmatter")
else:
    frontmatter = frontmatter_match.group(1)
    declared_name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", frontmatter)
    if not declared_name or declared_name.group(1) != ROOT.name:
        failures.append("SKILL.md name must match skill directory")
    if not re.search(r"(?m)^description:\s*(?:>|[^\n]+)$", frontmatter):
        failures.append("frontmatter description is required")
    if declared_name and len(declared_name.group(1)) > 64:
        failures.append("skill name exceeds 64 characters")

ui_path = ROOT / "agents/openai.yaml"
if ui_path.exists():
    ui_text = ui_path.read_text(encoding="utf-8")
    if not re.search(r"(?m)^interface:\s*$", ui_text):
        failures.append("agents/openai.yaml missing interface block")
    if f"$" + ROOT.name not in ui_text:
        failures.append("default_prompt should mention $skill-name")

# Regression checks for quantitative coaching errors.
guide = ROOT / "references/advanced_data_analysis.md"
if guide.exists():
    g = guide.read_text(encoding="utf-8")
    if "100 × IF²" not in g:
        failures.append("TSS per hour must equal 100 × IF²")
    if re.search(r"TSS密度\s*<\s*60/h\s*[→-]\s*恢复骑行", g):
        failures.append("60 TSS/hour must not be prescribed as recovery")

polarized = ROOT / "references/polarized_training.md"
if polarized.exists():
    q = polarized.read_text(encoding="utf-8")
    if "三分区" not in q or "七分区" not in q:
        failures.append("polarized training must distinguish 3-zone from 7-zone models")

if not (ROOT / "tests/scenarios.md").exists():
    failures.append("missing manual coaching scenario tests")

# Validate desired GitHub About metadata; this does NOT apply metadata to GitHub.
about_path = ROOT / ".github/repository-about.json"
if not about_path.exists():
    failures.append("GitHub About profile file missing")
else:
    try:
        about = json.loads(about_path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as ex:
        failures.append(f"GitHub About JSON invalid: {ex}")
    else:
        expected_repo = "1164origami/" + ROOT.name
        if about.get("repository") != expected_repo:
            failures.append(f"About repository must equal {expected_repo}")
        description = about.get("description", "")
        topics = about.get("topics", [])
        if not isinstance(description, str) or not (15 <= len(description) <= 160):
            failures.append("About description must be between 15 and 160 characters")
        if isinstance(description, str) and re.search(r"(?i)openclaw|qclaw", description):
            failures.append("About description contains legacy platform branding")
        if not isinstance(topics, list) or not (3 <= len(topics) <= 20):
            failures.append("About topics must be a list of 3 to 20 entries")
        else:
            valid_topic = re.compile(r"^[a-z0-9-]+$")
            if any(not isinstance(topic, str) or not valid_topic.fullmatch(topic) for topic in topics):
                failures.append("Topics must use lowercase letters, digits and hyphens")
            if len(set(topics)) != len(topics):
                failures.append("About topics contain duplicates")
            for required in ("codex", "agent-skills", "cycling"):
                if required not in topics:
                    failures.append(f"Missing shared topic: {required}")
if not (ROOT / "scripts/sync-github-about.ps1").exists():
    failures.append("Missing local GitHub About sync script")

if failures:
    print("Skill validation failed:")
    for failure in failures:
        print(" - " + failure)
    sys.exit(1)

print(f"Skill validation passed: {len(MARKDOWN)} Markdown files, links and key invariants.")
