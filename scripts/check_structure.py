"""Offline sanity checks for the list. Run: python scripts/check_structure.py

Checks:
  * every relative markdown link points at a file that exists
  * every http(s) link is well-formed
  * no link appears twice in README.md
  * README states a verification date
Exit code 1 on any problem.
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def main() -> int:
    problems = []
    for md in sorted(ROOT.glob("**/*.md")):
        text = md.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            if target.startswith("#") or target.startswith("mailto:"):
                continue
            if target.startswith(("http://", "https://")):
                parsed = urlparse(target)
                if not parsed.netloc or " " in target:
                    problems.append(f"{md.name}: malformed URL {target}")
            else:
                path = (md.parent / target.split("#")[0]).resolve()
                if not path.exists():
                    problems.append(f"{md.name}: missing file {target}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    urls = [u for u in LINK.findall(readme) if u.startswith("http")]
    for url in sorted({u for u in urls if urls.count(u) > 1}):
        problems.append(f"README.md: duplicate link {url}")
    if not re.search(r"20\d\d-\d\d-\d\d", readme):
        problems.append("README.md: no verification date found")

    for p in problems:
        print("PROBLEM:", p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
