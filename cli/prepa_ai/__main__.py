from pathlib import Path
import argparse
import sys
from . import __version__
from .app import Application
from .commands import HELP
from .config import ConfigError,load_config
from .doctor import print_diagnostics

def build_parser()->argparse.ArgumentParser:
    parser=argparse.ArgumentParser(
        prog="PREPA-AI",
        description="Asistente educativo local para CMD y PowerShell."
    )
    parser.add_argument("--diagnostico","--check",action="store_true",
                        help="revisar archivos y requisitos sin iniciar el modelo")
    parser.add_argument("--version",action="store_true",help="mostrar la versión")
    parser.add_argument("--ayuda",action="store_true",help="mostrar los comandos de la aplicación")
    return parser

def main()->int:
    args=build_parser().parse_args()
    if args.version:
        print(f"PREPA AI {__version__}")
        return 0
    if args.ayuda:
        print(HELP)
        print("\nOpciones: --diagnostico, --version, --ayuda")
        return 0
    root=Path(sys.executable).resolve().parent if getattr(sys,"frozen",False) else Path(__file__).resolve().parents[2]
    try:
        config=load_config(root/"config.json")
        if args.diagnostico:
            return 0 if print_diagnostics(root,config) else 1
        return Application(root,config).run()
    except ConfigError as exc:
        print(f"Error de configuración: {exc}")
        return 2

if __name__=="__main__":
    raise SystemExit(main())
