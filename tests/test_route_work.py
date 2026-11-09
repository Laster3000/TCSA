import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / "tools" / "route_work.py"
spec = importlib.util.spec_from_file_location("route_work", path)
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)

class EconomyRoutingTests(unittest.TestCase):
    def test_deterministic_does_not_call_model(self):
        r = router.decide({"kind": "build", "deterministicAvailable": True})
        self.assertEqual(r["route"], "L0_DETERMINISTIC")
        self.assertEqual(r["networkCallsMade"], 0)

    def test_local_implementation(self):
        r = router.decide({"kind": "implement", "localModelAvailable": True})
        self.assertEqual(r["route"], "L1_LOCAL_MODEL")

    def test_expert_only_with_authorized_scope_and_budget(self):
        r = router.decide({"kind": "design", "risk": "high", "localModelAvailable": True,
                           "remoteExpertAuthorized": True, "approvedRemoteDataScope": True,
                           "remoteCallsRemaining": 1})
        self.assertEqual(r["route"], "L2_REMOTE_EXPERT")
        self.assertTrue(r["dryRun"])

    def test_never_send_without_scope(self):
        r = router.decide({"kind": "design", "risk": "high", "remoteExpertAuthorized": True,
                           "remoteCallsRemaining": 10})
        self.assertEqual(r["route"], "BLOCKED")

    def test_protected_operations_are_blocked(self):
        r = router.decide({"kind": "build", "protectedOperation": True,
                           "deterministicAvailable": True})
        self.assertEqual(r["route"], "BLOCKED")

    def test_stop_stale_retries(self):
        r = router.decide({"kind": "implement", "localModelAvailable": True,
                           "sameApproachFailures": 2, "newDiagnosticEvidence": False})
        self.assertEqual(r["reason"], "STALE_RETRY_REQUIRES_NEW_EVIDENCE")

    def test_no_executor_is_not_success(self):
        r = router.decide({"kind": "implement", "localModelAvailable": False})
        self.assertEqual(r["route"], "BLOCKED")

if __name__ == "__main__":
    unittest.main()
