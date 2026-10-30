from __future__ import annotations
import json
from pathlib import Path

DEFAULTS = {
    "server_exe": "runtime/llama-server.exe",
    "model": "models/qwen2.5-1.5b-instruct-q4_k_m.gguf",
    "host": "127.0.0.1",
    "port": 8080,
    "context_size": 2048,
    "threads": 4,
    "temperature": 0.7,
    "max_tokens": 512,
    "startup_timeout": 180,
    "request_timeout": 300,
    "system_prompt": "Eres PREPA AI, un asistente educativo. Explica con claridad y sencillez.",
}

class ConfigError(ValueError):
    pass

def load_config(path: Path) -> dict:
    config = DEFAULTS.copy()
    if path.exists():
        try:
            supplied = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ConfigError(f"No se pudo leer {path.name}: {exc}") from exc
        if not isinstance(supplied, dict):
            raise ConfigError("La configuración debe ser un objeto JSON.")
        config.update(supplied)
    validate_config(config)
    return config

def validate_config(config: dict) -> None:
    if config.get("host") != "127.0.0.1":
        raise ConfigError("Por seguridad, el servidor solo puede usar 127.0.0.1.")
    for key, low, high in (("port",1024,65535),("context_size",256,131072),
                           ("threads",1,256),("max_tokens",1,32768),
                           ("startup_timeout",5,900),("request_timeout",10,3600)):
        value=config.get(key)
        if isinstance(value,bool) or not isinstance(value,int) or not low<=value<=high:
            raise ConfigError(f"{key} debe ser un entero entre {low} y {high}.")
    temp=config.get("temperature")
    if isinstance(temp,bool) or not isinstance(temp,(int,float)) or not 0<=temp<=2:
        raise ConfigError("temperature debe estar entre 0 y 2.")
    for key in ("server_exe","model"):
        if not isinstance(config.get(key),str) or not config[key].strip():
            raise ConfigError(f"{key} debe ser una ruta válida.")
