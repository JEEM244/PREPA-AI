from __future__ import annotations
import socket
import subprocess
import time
import urllib.error
from pathlib import Path
from .http_client import request_json

class EngineError(RuntimeError): pass

def port_is_available(port:int)->bool:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as probe:
        return probe.connect_ex(("127.0.0.1",int(port)))!=0

class Engine:
    def __init__(self,root:Path,config:dict):
        self.root=root; self.config=config; self.process:subprocess.Popen|None=None
        self.base_url=f"http://127.0.0.1:{config['port']}"

    def start(self)->None:
        server=(self.root/self.config["server_exe"]).resolve()
        model=(self.root/self.config["model"]).resolve()
        if not server.is_file(): raise EngineError(f"No se encontró llama-server: {server}")
        if not model.is_file(): raise EngineError(f"No se encontró el modelo GGUF: {model}")
        if not port_is_available(self.config["port"]):
            raise EngineError(f"El puerto {self.config['port']} ya está ocupado. Cambia el puerto en config.json.")
        command=[str(server),"--host","127.0.0.1","--port",str(self.config["port"]),
                 "--ctx-size",str(self.config["context_size"]),"--threads",str(self.config["threads"]),"-m",str(model)]
        try:
            self.process=subprocess.Popen(command,cwd=str(self.root),stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        except OSError as exc: raise EngineError(f"No se pudo iniciar el motor: {exc}") from exc
        deadline=time.monotonic()+self.config["startup_timeout"]
        while time.monotonic()<deadline:
            if self.process.poll() is not None:
                raise EngineError("llama-server se cerró durante el arranque. Revisa el modelo y la versión.")
            try:
                request_json(self.base_url+"/health",timeout=2)
                return
            except (urllib.error.URLError,TimeoutError,OSError,ValueError): time.sleep(1)
        self.stop()
        raise EngineError("Se agotó el tiempo de espera al iniciar el modelo.")

    def is_running(self)->bool:
        return self.process is not None and self.process.poll() is None

    def healthy(self)->bool:
        if not self.is_running(): return False
        try: request_json(self.base_url+"/health",timeout=3); return True
        except Exception: return False

    def stop(self)->None:
        if self.process is not None:
            if self.process.poll() is None:
                self.process.terminate()
                try: self.process.wait(timeout=8)
                except subprocess.TimeoutExpired:
                    self.process.kill(); self.process.wait(timeout=5)
            self.process=None
