import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from cli.prepa_ai import __main__ as cli_main

class CliArgumentTests(unittest.TestCase):
    def test_version_option_does_not_start_engine(self):
        output=io.StringIO()
        with patch("sys.argv",["PREPA-AI","--version"]),redirect_stdout(output):
            self.assertEqual(cli_main.main(),0)
        self.assertIn("PREPA AI",output.getvalue())
    def test_help_option_is_available_without_model(self):
        output=io.StringIO()
        with patch("sys.argv",["PREPA-AI","--ayuda"]),redirect_stdout(output):
            self.assertEqual(cli_main.main(),0)
        self.assertIn("/salir",output.getvalue())
    @patch("cli.prepa_ai.__main__.print_diagnostics",return_value=False)
    @patch("cli.prepa_ai.__main__.load_config",return_value={})
    def test_diagnostic_returns_failure_if_assets_are_missing(self,load_config,diagnostics):
        with patch("sys.argv",["PREPA-AI","--diagnostico"]):
            self.assertEqual(cli_main.main(),1)
        diagnostics.assert_called_once()

if __name__=="__main__": unittest.main()
