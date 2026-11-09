import json, tempfile, unittest, pathlib, io, contextlib
from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec
loader=SourceFileLoader("tcsa",str(pathlib.Path(__file__).resolve().parents[1]/"src"/"tcsa.py"))
spec=spec_from_loader(loader.name,loader)
tcsa=module_from_spec(spec);loader.exec_module(tcsa)
class TCSATests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.root=pathlib.Path(self.tmp.name);self.source=self.root/"in.json"
  self.source.write_text('{"nextAction":"test"}',encoding="utf-8")
 def create(self,expected="NONE"):
  with contextlib.redirect_stdout(io.StringIO()):tcsa.checkpoint(self.root,"AF-CORE",self.source,expected)
  return self.root/"00-CHECKPOINTS"/"BY-PROJECT"/"AF-CORE"/"LATEST.json"
 def test_commit_restore_readback(self):
  p=self.create()
  with contextlib.redirect_stdout(io.StringIO()):self.assertEqual(tcsa.verify_checkpoint(p),0)
 def test_cas_conflict_preserves_pointer(self):
  p=self.create();before=p.read_bytes()
  with self.assertRaisesRegex(RuntimeError,"CAS_CONFLICT"):self.create()
  self.assertEqual(before,p.read_bytes())
 def test_chain_expected_sha(self):
  p=self.create();prev=tcsa.load(p)["checkpointSha256"]
  self.create(prev);self.assertEqual(tcsa.load(p)["prevSha256"],prev)
 def test_tamper_detected(self):
  p=self.create();snap=p.parent/(tcsa.load(p)["checkpointId"]+".json")
  snap.write_bytes(snap.read_bytes()+b"bad")
  with contextlib.redirect_stdout(io.StringIO()):self.assertEqual(tcsa.verify_checkpoint(p),2)
 def test_invalid_project(self):
  with self.assertRaisesRegex(ValueError,"INVALID_PROJECT_ID"):tcsa.checkpoint(self.root,"../escape",self.source,"NONE")
if __name__=="__main__":unittest.main(verbosity=2)
