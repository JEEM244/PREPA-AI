from __future__ import annotations
from pathlib import Path
from .chat import ChatSession
from .commands import HELP,normalize_command
from .engine import Engine,EngineError
from .doctor import print_diagnostics
from . import __version__

class Application:
    def __init__(self,root:Path,config:dict):
        self.root=root; self.config=config; self.engine=Engine(root,config)
        self.chat=ChatSession(config,self.engine.base_url)

    def run(self)->int:
        print("PREPA AI | Asistente local de terminal")
        print("Funciona sin internet cuando el motor y el modelo están disponibles.")
        print("Escribe /ayuda para ver los comandos.\\n")
        try:
            print("Iniciando modelo local...")
            self.engine.start()
            print("Modelo listo. Puedes comenzar.\\n")
            self._repl()
            return 0
        except EngineError as exc:
            print(f"Error del motor: {exc}")
            return 1
        finally:
            self.engine.stop()
            print("Motor detenido. Sesión finalizada.")

    def _repl(self)->None:
        while True:
            try: line=input("Tú > ").strip()
            except (EOFError,KeyboardInterrupt): print(); return
            if not line: continue
            command=normalize_command(line)
            if command=="/salir": return
            if command=="/version": print(f"PREPA AI {__version__}\\n")
            elif command=="/diagnostico":
                print_diagnostics(self.root,self.config); print()
            elif command=="/ayuda": print(HELP+"\\n")
            elif command=="/estado":
                state="activo" if self.engine.healthy() else "sin respuesta"
                print(f"Motor: {state} | Dirección local: {self.engine.base_url}\\n")
            elif command=="/limpiar":
                self.chat.clear(); print("Conversación borrada de la memoria de esta sesión.\\n")
            elif command=="/modelo": print(f"Modelo: {self.config['model']}\\n")
            elif command.startswith("/"): print("Comando desconocido. Escribe /ayuda.\\n")
            else:
                try: print(f"\\nPREPA AI > {self.chat.send(line)}\\n")
                except Exception as exc: print(f"No se pudo generar la respuesta: {exc}\\n")
