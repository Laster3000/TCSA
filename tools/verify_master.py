#!/usr/bin/env python3
"""Verify a TCSA instruction master against its manifest; no network or writes."""
import argparse
import hashlib
import json
from pathlib import Path

def check(root):
    root = Path(root)
    mpath = root / "MANIFEST-INSTRUCCIONES.json"
    master = root / "INSTRUCCIONES-MAESTRAS.md"
    if not mpath.is_file() or not master.is_file():
        return {"status": "BLOCKED", "reason": "MANIFEST_OR_MASTER_MISSING", "root": str(root)}
    try:
        metadata = json.loads(mpath.read_text(encoding="utf-8-sig"))
        raw = master.read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        expected = str(metadata["sha256"]).lower()
        expected_size = metadata.get("bytesUtf8")
        ok = actual == expected and (expected_size is None or len(raw) == expected_size)
        return {"status": "PASS" if ok else "FAILED",
                "version": metadata.get("version"),
                "masterSha256": actual,
                "expectedSha256": expected,
                "bytesUtf8": len(raw),
                "reason": "VERIFIED" if ok else "HASH_OR_SIZE_MISMATCH"}
    except (OSError, ValueError, KeyError) as error:
        return {"status": "FAILED", "reason": str(error)}

def main():
    p = argparse.ArgumentParser(description="Verify canonical TCSA master before project work")
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args()
    result = check(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
