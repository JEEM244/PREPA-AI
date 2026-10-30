import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from cli.prepa_ai.app import Application
from cli.prepa_ai.config import DEFAULTS

class AppTests(unittest.TestCase):
    @patch("cli.prepa_ai.app.Engine.start",side_effect=RuntimeError("fallo simulado"))
    @patch("builtins.print")
    def test_engine_is_stopped_after_start_error(self,print_mock,start_mock):
        with tempfile.TemporaryDirectory() as folder:
            app=Application(Path(folder),DEFAULTS.copy())
            with patch.object(app.engine,"stop") as stop:
                with self.assertRaises(RuntimeError):
                    app.run()
                stop.assert_called_once()

if __name__=="__main__": unittest.main()
