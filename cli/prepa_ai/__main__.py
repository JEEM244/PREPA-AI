from pathlib import Path
import sys
from .app import Application
from .config import ConfigError,load_config

def main()->int:
    root=Path(sys.executable).resolve().parent if getattr(sys,"frozen",False) else Path(__file__).resolve().parents[2]
    try:
        config=load_config(root/"config.json")
        return Application(root,config).run()
    except ConfigError as exc:
        print(f"Error de configuración: {exc}")
        return 2

if __name__=="__main__":
    raise SystemExit(main())
