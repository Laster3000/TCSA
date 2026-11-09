#!/usr/bin/env python3
"""TCSA portable: catalog, LISTA, discoveries and verifiable checkpoint writer.
Not an executor; never infers LIVE status from snapshots or replays jobs.
"""
import argparse, datetime, hashlib, json, os, pathlib, sys, tempfile, uuid

DEFAULT_ROOT = pathlib.Path(os.environ.get("TCSA_ROOT", r"G:\Mi unidad\TCSA"))
def digest(data): return hashlib.sha256(data).hexdigest()
def load(path):
    with path.open("r", encoding="utf-8-sig") as f: return json.load(f)
def atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=".tcsa-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data); f.flush(); os.fsync(f.fileno())
        os.replace(temp, path)
        if path.read_bytes() != data: raise IOError("READBACK_MISMATCH")
    finally:
        if os.path.exists(temp): os.unlink(temp)
def jsonbytes(value): return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
def listing(root, which):
    spec={"projects":("02-CATALOGO/PROYECTOS.json","projects"),
          "lista":("07-LISTA/INDEX.json","notes"),
          "discoveries":("08-DESCUBRIMIENTOS/INDEX.json","records")}
    path, key=spec[which]
    d=load(root/path); print(json.dumps({"source":str(root/path),"records":d.get(key,[]),"snapshot":d.get("updatedAtUtc") or d.get("updatedDate"),"note":"No live executor status inferred"},ensure_ascii=False,indent=2))
def check_manifest(root):
    problems=[]
    paths=["02-CATALOGO/PROYECTOS.json","07-LISTA/INDEX.json","08-DESCUBRIMIENTOS/INDEX.json",
           "01-INSTRUCCIONES/COPIAR-INSTRUCCIONES.txt"]
    for name in paths:
        p=root/name
        if not p.is_file(): problems.append(f"MISSING {name}");continue
        if p.suffix==".json":
            try:load(p)
            except Exception as exc:problems.append(f"INVALID {name}: {exc}")
    print(json.dumps({"status":"PASS_SCOPED" if not problems else "FAILED",
      "checks":len(paths),"issues":problems,"scope":"Index readability, NOT archive restore or live E2E"},ensure_ascii=False,indent=2))
    return 0 if not problems else 2
def checkpoint(root, project, source, expected):
    if not project.isascii() or not project or not all(c.isalnum() or c in "-_" for c in project):raise ValueError("INVALID_PROJECT_ID")
    payload=load(source)
    pdir=root/"00-CHECKPOINTS"/"BY-PROJECT"/project
    pdir.mkdir(parents=True, exist_ok=True)
    lock=pdir/".write.lock"
    try: fd=os.open(lock, os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    except FileExistsError:raise RuntimeError("CONCURRENT_WRITER: reconcile, do not overwrite")
    try:
        with os.fdopen(fd,"w") as f:f.write(str(os.getpid()))
        pointer=pdir/"LATEST.json"
        old=load(pointer) if pointer.exists() else None
        prev=old["checkpointSha256"] if old else None
        if expected != (prev or "NONE"):raise RuntimeError("CAS_CONFLICT: expected current checkpoint SHA")
        created=datetime.datetime.now(datetime.timezone.utc).isoformat()
        record={"schema":"tcsa.checkpoint.v1","checkpointId":uuid.uuid4().hex,
                "type":"PROJECT_CHECKPOINT","projectId":project,"createdAtUtc":created,
                "prevSha256":prev,"payload":payload,"snapshotStatus":"COMMITTED",
                "provenance":"USER_SUPPLIED_DOCUMENT_NOT_LIVE_EXECUTOR"}
        raw=jsonbytes(record); h=digest(raw)
        snapshot=pdir/(record["checkpointId"]+".json")
        atomic(snapshot,raw)
        if digest(snapshot.read_bytes()) != h:raise RuntimeError("CHECKPOINT_VERIFY_FAILED")
        atomic(pointer,jsonbytes({"checkpointId":record["checkpointId"],"checkpointSha256":h,"prevSha256":prev,"createdAtUtc":created}))
        if load(pointer)["checkpointSha256"] != h:raise RuntimeError("POINTER_READBACK_FAILED")
        print(json.dumps({"status":"COMMITTED","sha256":h,"checkpoint":str(snapshot),"pointer":str(pointer)},ensure_ascii=False))
    finally:lock.unlink(missing_ok=True)
def verify_checkpoint(path):
    d=load(path)
    snapshot=path.parent/(d["checkpointId"]+".json")
    ok=snapshot.exists() and digest(snapshot.read_bytes())==d["checkpointSha256"]
    print(json.dumps({"status":"PASS" if ok else "FAILED","checkpoint":str(snapshot),"sha256":d["checkpointSha256"]}))
    return 0 if ok else 2
def main(argv=None):
    ap=argparse.ArgumentParser(description="TCSA independent project continuity utility")
    ap.add_argument("--root",type=pathlib.Path,default=DEFAULT_ROOT)
    sub=ap.add_subparsers(dest="command",required=True)
    for c in ["menu","projects","lista","discoveries","doctor"]:sub.add_parser(c)
    cp=sub.add_parser("checkpoint");cp.add_argument("--project",required=True);cp.add_argument("--source",type=pathlib.Path,required=True);cp.add_argument("--expect",required=True,help="LATEST checkpoint SHA or NONE")
    vf=sub.add_parser("verify-checkpoint");vf.add_argument("pointer",type=pathlib.Path)
    a=ap.parse_args(argv)
    try:
        if a.command=="menu":print("TCSA CONTROL CENTER\n1 AUTOFABRICADOR\n2 MENU-AUTOFABRICADOR\n3 JUEGO-DEL-MENU\n4 TCSA\n5 LISTA\n6 DESCUBRIMIENTOS\n7 CHECKPOINTS\n8 NUEVO PROYECTO\n9 CONSULTA GENERAL\n(Consulta de catalogo, no motor ni menu integrado con ChatGPT)")
        elif a.command in ("projects","lista","discoveries"):listing(a.root,a.command)
        elif a.command=="doctor":return check_manifest(a.root)
        elif a.command=="checkpoint":checkpoint(a.root,a.project,a.source,a.expect)
        elif a.command=="verify-checkpoint":return verify_checkpoint(a.pointer)
    except (OSError,ValueError,RuntimeError,KeyError,json.JSONDecodeError) as exc:
        print(json.dumps({"status":"FAILED","error":str(exc)},ensure_ascii=False),file=sys.stderr);return 2
    return 0
if __name__=="__main__":sys.exit(main())
