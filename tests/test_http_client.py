import json
import unittest
from unittest.mock import patch,MagicMock
from cli.prepa_ai.http_client import request_json

class HttpClientTests(unittest.TestCase):
    @patch("cli.prepa_ai.http_client.urllib.request.urlopen")
    def test_decodes_json_response(self,open_url):
        response=MagicMock()
        response.__enter__.return_value.read.return_value=b'{"ok":true}'
        open_url.return_value=response
        self.assertEqual(request_json("http://127.0.0.1:8080/health"),{"ok":True})
    @patch("cli.prepa_ai.http_client.urllib.request.urlopen")
    def test_sends_json_payload(self,open_url):
        response=MagicMock()
        response.__enter__.return_value.read.return_value=b'{"ok":true}'
        open_url.return_value=response
        request_json("http://127.0.0.1:8080/api",{"message":"hola"})
        request=open_url.call_args.args[0]
        self.assertEqual(json.loads(request.data.decode()),{"message":"hola"})

if __name__=="__main__": unittest.main()
