#!/usr/bin/env python3
# DD-契约与测试验证器
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(msg): errors.append(msg)

# 1) Schema files must be valid JSON
for path in [
    ROOT/"contracts/DD-skill-contract.schema.json",
    ROOT/"contracts/DD-agent-contract.schema.json",
]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            fail(f"{path}: schema draft mismatch")
    except Exception as e:
        fail(f"{path}: invalid JSON: {e}")

# 2) All eight required skills need positive / negative / failure cases
expected = {
 "dd-evidence","dd-name","dd-desire","dd-arena",
 "dd-min-action","dd-autonomy","dd-stop","dd-boundary"
}
test_dir = ROOT/"tests/skills"
found = {p.stem for p in test_dir.glob("*.json")}
missing = expected - found
extra = found - expected
if missing: fail(f"missing skill tests: {sorted(missing)}")
if extra: fail(f"unexpected skill tests: {sorted(extra)}")

for p in test_dir.glob("*.json"):
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        kinds = {c.get("kind") for c in data.get("cases", [])}
        if kinds != {"positive","negative","failure"}:
            fail(f"{p}: cases must contain positive/negative/failure exactly")
        if data.get("version") != "1.1.0":
            fail(f"{p}: version must be 1.1.0")
    except Exception as e:
        fail(f"{p}: invalid test fixture: {e}")

# 3) Required documentation / examples / trace
required = [
 ROOT/"README_EN.md",
 ROOT/"CONTRIBUTING.md",
 ROOT/"SECURITY.md",
 ROOT/"docs/compatibility/DD-平台兼容说明.md",
 ROOT/"docs/trace/DD-标准Trace示例.json",
]
for p in required:
    if not p.exists() or not p.read_text(encoding="utf-8").strip():
        fail(f"missing or empty: {p.relative_to(ROOT)}")

examples = list((ROOT/"examples").glob("DD-*.md"))
if len(examples) < 6:
    fail(f"need at least 6 DD examples, found {len(examples)}")

# 4) Trace must expose governance fields
trace_path = ROOT/"docs/trace/DD-标准Trace示例.json"
if trace_path.exists():
    try:
        trace = json.loads(trace_path.read_text(encoding="utf-8"))
        for key in ["task_id","classification","evidence","decision","action","verification","stop"]:
            if key not in trace:
                fail(f"trace missing field: {key}")
    except Exception as e:
        fail(f"trace invalid JSON: {e}")

if errors:
    print("DD-DaoKernel validation FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("DD-DaoKernel validation PASSED")
print("8 skill test fixtures: OK")
print("2 contract schemas: OK")
print("6+ examples: OK")
print("compatibility / trace / contribution / security docs: OK")
