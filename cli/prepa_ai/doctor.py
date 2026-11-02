from __future__ import annotations
import platform
import sys
from pathlib import Path
from .engine import EngineError,resolve_asset

def collect_diagnostics(root:Path,config:dict)->list[tuple[str,bool,str]]:
    checks=[]
    checks.append(("Sistema",platform.system()=="Windows",
                   f"{platform.system()} {platform.release()} ({platform.machine()})"))
    checks.append(("Python",sys.version_info>=(3,10),
                   platform.python_version()+" (se requiere 3.10 o superior)"))
    for label,key,extension in (("Motor llama.cpp","server_exe",".exe"),("Modelo GGUF","model",".gguf")):
        try:
            asset=resolve_asset(root,config[key],extension)
            checks.append((label,asset.is_file(),str(asset)))
        except (EngineError,KeyError,TypeError) as exc:
            checks.append((label,False,str(exc)))
    checks.append(("Puerto local",True,f"127.0.0.1:{config['port']} (se verifica al iniciar)"))
    checks.append(("Internet",True,"No es necesario para inferencia local"))
    return checks

def print_diagnostics(root:Path,config:dict)->bool:
    print("Diagnóstico de PREPA AI")
    results=collect_diagnostics(root,config)
    for label,ok,detail in results:
        print(f"[{'OK' if ok else 'FALTA'}] {label}: {detail}")
    return all(item[1] for item in results)
