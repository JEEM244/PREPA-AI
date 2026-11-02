import tempfile
import unittest
from pathlib import Path
from cli.prepa_ai.engine import EngineError,port_is_available,resolve_asset

class EngineTests(unittest.TestCase):
    def test_detects_port_in_use(self):
        import socket
        sock=socket.socket()
        sock.bind(("127.0.0.1",0))
        sock.listen(1)
        try: self.assertFalse(port_is_available(sock.getsockname()[1]))
        finally: sock.close()
    def test_unused_port_is_available(self):
        import socket
        sock=socket.socket()
        sock.bind(("127.0.0.1",0))
        port=sock.getsockname()[1]
        sock.close()
        self.assertTrue(port_is_available(port))
    def test_asset_must_stay_inside_project(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(EngineError):
                resolve_asset(Path(folder),"../outside.exe",".exe")
    def test_asset_must_be_relative(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(EngineError):
                resolve_asset(Path(folder),str(Path(folder)/"server.exe"),".exe")
    def test_asset_extension_is_checked(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(EngineError):
                resolve_asset(Path(folder),"runtime/not-an-exe.txt",".exe")

if __name__=="__main__": unittest.main()
