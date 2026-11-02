import unittest
from copy import deepcopy
from unittest.mock import patch
from cli.prepa_ai.chat import ChatSession
from cli.prepa_ai.config import DEFAULTS

class ChatTests(unittest.TestCase):
    def setUp(self):
        self.config=DEFAULTS.copy()
        self.chat=ChatSession(self.config,"http://127.0.0.1:8080")

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

    @patch("cli.prepa_ai.chat.request_json")
    def test_new_request_counts_toward_history_limit(self,request):
        self.config["max_history_turns"]=2
        self.chat.messages.extend([
            {"role":"user","content":"pregunta 1"},{"role":"assistant","content":"respuesta 1"},
            {"role":"user","content":"pregunta 2"},{"role":"assistant","content":"respuesta 2"},
            {"role":"user","content":"pregunta 3"},{"role":"assistant","content":"respuesta 3"},
        ])
        sent=[]
        def fake_request(_url,payload,timeout):
            sent.append(deepcopy(payload))
            return {"choices":[{"message":{"content":"respuesta nueva"}}]}
        request.side_effect=fake_request

        self.chat.send("pregunta nueva")

        contents=[message["content"] for message in sent[0]["messages"]]
        self.assertEqual(contents,[self.config["system_prompt"],"pregunta 3","respuesta 3","pregunta nueva"])
        self.assertEqual(len(self.chat.messages),5)

    @patch("cli.prepa_ai.chat.request_json")
    def test_one_turn_limit_does_not_send_old_messages(self,request):
        self.config["max_history_turns"]=1
        self.chat.messages.extend([
            {"role":"user","content":"anterior"},{"role":"assistant","content":"respuesta anterior"}
        ])
        sent=[]
        def fake_request(_url,payload,timeout):
            sent.append(deepcopy(payload))
            return {"choices":[{"message":{"content":"respuesta"}}]}
        request.side_effect=fake_request

        self.chat.send("nuevo")

        self.assertEqual([m["content"] for m in sent[0]["messages"]],
                         [self.config["system_prompt"],"nuevo"])

    @patch("cli.prepa_ai.chat.request_json")
    def test_failed_request_preserves_existing_history(self,request):
        self.chat.messages.extend([
            {"role":"user","content":"anterior"},{"role":"assistant","content":"respuesta anterior"}
        ])
        original=deepcopy(self.chat.messages)
        request.side_effect=TimeoutError("motor no disponible")

        with self.assertRaises(TimeoutError):
            self.chat.send("nuevo")

        self.assertEqual(self.chat.messages,original)

    @patch("cli.prepa_ai.chat.request_json")
    def test_oversized_input_is_rejected_before_request(self,request):
        self.config["max_input_chars"]=5
        original=deepcopy(self.chat.messages)

        with self.assertRaises(ValueError):
            self.chat.send("mensaje demasiado largo")

        request.assert_not_called()
        self.assertEqual(self.chat.messages,original)

if __name__=="__main__":
    unittest.main()
