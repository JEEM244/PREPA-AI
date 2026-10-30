import tempfile
import unittest
from pathlib import Path
from cli.prepa_ai.config import DEFAULTS
from cli.prepa_ai.doctor import collect_diagnostics

class DoctorTests(unittest.TestCase):
    def test_reports_missing_engine_and_model(self):
        with tempfile.TemporaryDirectory() as folder:
            results=collect_diagnostics(Path(folder),DEFAULTS.copy())
            by_name={name:ok for name,ok,_ in results}
            self.assertFalse(by_name["Motor llama.cpp"])
            self.assertFalse(by_name["Modelo GGUF"])
            self.assertTrue(by_name["Internet"])

if __name__=="__main__": unittest.main()
