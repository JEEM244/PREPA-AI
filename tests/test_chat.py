import unittest
from unittest.mock import patch
from cli.prepa_ai.chat import ChatSession
from cli.prepa_ai.config import DEFAULTS

class ChatTests(unittest.TestCase):
    def setUp(self): self.chat=ChatSession(DEFAULTS.copy(),"http://127.0.0.1:8080")
    @patch("cli.prepa_ai.chat.request_json")
    def test_send_stores_turn_in_memory(self,request):
        request.return_value={"choices":[{"message":{"content":"Hola"}}]}
        self.assertEqual(self.chat.send("Buenas"),"Hola")
        self.assertEqual(len(self.chat.messages),3)
    def test_clear_keeps_system_prompt_only(self):
        self.chat.messages.append({"role":"user","content":"privado"})
        self.chat.clear()
        self.assertEqual(len(self.chat.messages),1)
        self.assertEqual(self.chat.messages[0]["role"],"system")

if __name__=="__main__": unittest.main()
