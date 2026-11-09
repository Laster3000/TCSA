#!/usr/bin/env python3
"""TCSA C1: one scoped local-to-synced-Drive closure; cloud API confirmation is separate.
No model calls, no worker, no COMMITTED pointer, no bulk file operations.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, sys, uuid
from datetime import datetime, timezone
from pathlib import Path

IDENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{1,79}\Z")
MAX_EVIDENCE = 5 * 1024 * 1024

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""): h.update(block)
    return h.hexdigest()

def close(args):
    if not IDENT.fullmatch(args.project_id) or not IDENT.fullmatch(args.operation_id):
        raise ValueError("PROJECT_OR_OPERATION_ID_INVALID")
    if not args.summary.strip() or not args.next_action.strip():
        raise ValueError("SUMMARY_AND_NEXT_ACTION_REQUIRED")
    source = args.source_root.resolve(strict=True)
    drive = args.drive_root.resolve(strict=True)
    project = drive / "03-PROYECTOS" / args.project_id
    if not project.is_dir() or project.is_symlink():
        raise ValueError("REGISTERED_PROJECT_FOLDER_REQUIRED")
    target = project / "CIERRES-LIGEROS" / args.operation_id
    if target.exists():
        raise FileExistsError("EXISTING_OPERATION_RECONCILE_DO_NOT_REPLAY")
    if len(args.evidence) > 12: raise ValueError("C1_MAX_12_EVIDENCE_FILES")
    checked = []
    for rel in args.evidence:
        p = Path(rel)
        if p.is_absolute() or ".." in p.parts or not p.parts:
            raise ValueError("EVIDENCE_RELATIVE_PATH_REQUIRED")
        src = (source / p).resolve(strict=True)
        if not src.is_file() or src.is_symlink() or not src.is_relative_to(source):
            raise ValueError("EVIDENCE_UNSAFE_OR_MISSING")
        if src.stat().st_size > MAX_EVIDENCE:
            raise ValueError("EVIDENCE_TOO_LARGE_ESCALATE_C2")
        checked.append((p, src))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.mkdir()  # atomic NO-OVERWRITE claim; orphan remains for reconciliation
    evidence = []
    for p, src in checked:
        dst = target / "EVIDENCIAS" / p
        dst.parent.mkdir(parents=True, exist_ok=True)
        with src.open("rb") as r, dst.open("xb") as w:
            shutil.copyfileobj(r, w); w.flush(); os.fsync(w.fileno())
        digest = sha(src)
        if sha(dst) != digest: raise IOError("EVIDENCE_READBACK_MISMATCH")
        evidence.append({"path": p.as_posix(), "sha256": digest, "bytes": src.stat().st_size})
    doc = {
        "schema": "tcsa.cierre-c1.r2", "projectId": args.project_id,
        "operationId": args.operation_id,
        "createdUtc": datetime.now(timezone.utc).isoformat(),
        "summary": args.summary.strip(), "tests": args.tests.strip(),
        "evidence": evidence, "nextAction": args.next_action.strip(),
        "scope": "C1_ROUTINE", "cloudStatus": "PENDING_CLOUD_READBACK",
        "originalExecutorStatus": "NOT_READ_IN_THIS_TOOL",
        "committedPointerChanged": False, "generalE2EAccepted": False
    }
    path = target / "CIERRE-LIGERO.json"
    raw = (json.dumps(doc, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    with path.open("xb") as f:
        f.write(raw); f.flush(); os.fsync(f.fileno())
    if sha(path) != hashlib.sha256(raw).hexdigest(): raise IOError("CLOSURE_READBACK_MISMATCH")
    return {"status": "PENDING_CLOUD_READBACK", "record": str(path),
            "sha256": sha(path), "evidenceCount": len(evidence)}

def main():
    p = argparse.ArgumentParser(description="TCSA C1 local close (Drive API readback separate)")
    p.add_argument("--project-id", required=True)
    p.add_argument("--operation-id", required=True)
    p.add_argument("--summary", required=True)
    p.add_argument("--next-action", required=True)
    p.add_argument("--tests", default="NOT_RUN")
    p.add_argument("--source-root", type=Path, required=True)
    p.add_argument("--drive-root", type=Path, required=True)
    p.add_argument("--evidence", action="append", default=[])
    args = p.parse_args()
    try:
        print(json.dumps(close(args), ensure_ascii=False, indent=2))
        return 0
    except Exception as error:
        print(json.dumps({"status": "BLOCKED_RECONCILE", "reason": str(error)}, ensure_ascii=False))
        return 2
if __name__ == "__main__": raise SystemExit(main())
