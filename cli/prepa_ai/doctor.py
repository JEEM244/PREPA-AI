from __future__ import annotations
import platform
import sys
from pathlib import Path

def collect_diagnostics(root: Path, config: dict) -> list[tuple[str, bool, str]]:
    server=(root/config["server_exe"]).resolve()
    model=(root/config["model"]).resolve()
    return [
        ("Sistema",platform.system()=="Windows",f"{platform.system()} {platform.release()} ({platform.machine()})"),
        ("Python",sys.version_info >= (3,10),platform.python_version()+" (se requiere 3.10 o superior)"),
        ("Motor llama.cpp",server.is_file(),str(server)),
        ("Modelo GGUF",model.is_file(),str(model)),
        ("Puerto local",True,f"127.0.0.1:{config['port']} (se verifica al iniciar)"),
        ("Internet",True,"No es necesario para inferencia local"),
    ]

def print_diagnostics(root: Path, config: dict) -> bool:
    print("Diagnóstico de PREPA AI")
    results=collect_diagnostics(root,config)
    for label,ok,detail in results:
        print(f"[{'OK' if ok else 'FALTA'}] {label}: {detail}")
    return all(item[1] for item in results)
