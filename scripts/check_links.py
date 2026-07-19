#!/usr/bin/env python3
"""Check catalog links: HuggingFace Hub API + lightweight HTTP HEAD/GET."""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Please install PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
CATALOG_YML = ROOT / "data" / "catalog.yml"
UA = "Awesome-TCM-LLM-linkcheck/1.0 (+https://github.com/tyang816/Awesome-TCM-LLM)"
HF_RE = re.compile(r"^https?://huggingface\.co/(datasets/)?([^/]+)/([^/]+)/?")


def collect_urls(catalog: dict) -> list[tuple[str, str, str]]:
    rows = []
    for item in catalog.get("items", []):
        iid = item.get("id", "?")
        for label, url in (item.get("links") or {}).items():
            if url:
                rows.append((iid, label, url))
    return rows


def check_hf(url: str) -> tuple[str, str]:
    m = HF_RE.match(url)
    if not m:
        return "skip", "not hf"
    is_ds, owner, name = m.group(1), m.group(2), m.group(3)
    api = (
        f"https://huggingface.co/api/datasets/{owner}/{name}"
        if is_ds
        else f"https://huggingface.co/api/models/{owner}/{name}"
    )
    req = urllib.request.Request(api, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
        title = data.get("id") or f"{owner}/{name}"
        return "pass", title
    except urllib.error.HTTPError as e:
        return "fail", f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return "fail", str(e)[:80]


def check_http(url: str) -> tuple[str, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            code = resp.getcode()
            body = resp.read(8000).decode("utf-8", errors="replace")
        title_m = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
        title = re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else ""
        if code >= 400:
            return "fail", f"HTTP {code} {title[:60]}"
        # Soft-pass known anti-bot walls
        if code in (401, 403) or "captcha" in body.lower():
            return "soft", f"HTTP {code} (anti-bot) {title[:40]}"
        return "pass", f"HTTP {code} {title[:60]}"
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 429):
            return "soft", f"HTTP {e.code}"
        return "fail", f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return "soft", f"net:{str(e)[:60]}"


def main() -> int:
    catalog = yaml.safe_load(CATALOG_YML.read_text(encoding="utf-8"))
    rows = collect_urls(catalog)
    stats = {"pass": 0, "soft": 0, "fail": 0}
    fails = []
    for iid, label, url in rows:
        if HF_RE.match(url):
            status, detail = check_hf(url)
        else:
            status, detail = check_http(url)
        stats[status] = stats.get(status, 0) + 1
        mark = {"pass": "OK", "soft": "~", "fail": "X"}.get(status, "?")
        print(f"[{mark}] {iid} / {label}: {detail}")
        if status == "fail":
            fails.append((iid, label, url, detail))
    print("---")
    print(f"total={len(rows)} pass={stats.get('pass',0)} soft={stats.get('soft',0)} fail={stats.get('fail',0)}")
    if fails:
        print("FAILURES:")
        for row in fails:
            print(" ", row)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
