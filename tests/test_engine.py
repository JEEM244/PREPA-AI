import socket
import unittest
from cli.prepa_ai.engine import port_is_available

class EngineTests(unittest.TestCase):
    def test_detects_port_in_use(self):
        sock=socket.socket()
        sock.bind(("127.0.0.1",0))
        sock.listen(1)
        try:
            self.assertFalse(port_is_available(sock.getsockname()[1]))
        finally:
            sock.close()
    def test_unused_port_is_available(self):
        sock=socket.socket()
        sock.bind(("127.0.0.1",0))
        port=sock.getsockname()[1]
        sock.close()
        self.assertTrue(port_is_available(port))

if __name__=="__main__": unittest.main()
