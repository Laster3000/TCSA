#!/usr/bin/env python3
"""Tests for deterministic C1 closure; no real Drive usage."""
from argparse import Namespace
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from tempfile import TemporaryDirectory
from unittest import TestCase, main
from cierre_ligero import close

class Checks(TestCase):
    def test_scoped_write_and_no_replay(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp); src=root/"source";drive=root/"drive"
            src.mkdir();(src/"module.py").write_text("x=1\n",encoding="utf8")
            (drive/"03-PROYECTOS"/"AF-CORE").mkdir(parents=True)
            args=Namespace(project_id="AF-CORE",operation_id="OP-101",
                summary="Change",tests="PASS",next_action="Next",
                source_root=src,drive_root=drive,evidence=["module.py"])
            result=close(args)
            self.assertEqual(result["status"],"PENDING_CLOUD_READBACK")
            self.assertEqual(result["evidenceCount"],1)
            with self.assertRaises(FileExistsError):close(args)
    def test_reject_path_escape(self):
        with TemporaryDirectory() as tmp:
            root=Path(tmp); src=root/"s";drive=root/"d"
            src.mkdir();(drive/"03-PROYECTOS"/"AF-CORE").mkdir(parents=True)
            args=Namespace(project_id="AF-CORE",operation_id="OP-102",
                summary="Change",tests="PASS",next_action="Next",
                source_root=src,drive_root=drive,evidence=["../escape.txt"])
            with self.assertRaises(ValueError):close(args)
if __name__=="__main__": main()
