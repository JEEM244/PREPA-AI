import unittest
from cli.prepa_ai.commands import normalize_command

class CommandTests(unittest.TestCase):
    def test_aliases(self):
        self.assertEqual(normalize_command("/help"),"/ayuda")
        self.assertEqual(normalize_command("/exit"),"/salir")
    def test_case_and_spaces(self):
        self.assertEqual(normalize_command("  /ESTADO  "),"/estado")

if __name__=="__main__": unittest.main()
