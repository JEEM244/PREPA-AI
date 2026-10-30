#!/usr/bin/env python3
"""PREPA AI - CLI local para llama.cpp en Windows."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.json"
DEFAULTS = {
    "server_exe": "runtime/llama-server.exe",
    "model": "models/qwen2.5-1.5b-instruct-q4_k_m.gguf",
    "host": "127.0.0.1",
    "port": 8080,
    "context_size": 2048,
    "threads": 4,
    "temperature": 0.7,
    "max_tokens": 512,
}


def load_config() -> dict:
    config = DEFAULTS.copy()
    if CONFIG_PATH.exists():
        try:
            supplied = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            if isinstance(supplied, dict):
                config.update(supplied)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"No pude leer config.json: {exc}")
            raise SystemExit(2)
    return config


def request_json(url: str, payload: dict | None = None, timeout: int = 10) -> dict:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"} if data is not None else {}
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


class PrepaAI:
    def __init__(self, config: dict):
        self.config = config
        self.process: subprocess.Popen | None = None
        self.base_url = f"http://{config['host']}:{int(config['port'])}"
        self.history: list[dict[str, str]] = []

    def start_engine(self) -> None:
        server = (ROOT / self.config["server_exe"]).resolve()
        model = (ROOT / self.config["model"]).resolve()
        if not server.is_file():
            raise FileNotFoundError(
                f"No encuentro el motor: {server}\nColoca llama-server.exe en runtime/."
            )
        if not model.is_file():
            raise FileNotFoundError(
                f"No encuentro el modelo: {model}\nColoca el archivo GGUF en models/."
            )

        command = [
            str(server), "--host", str(self.config["host"]),
            "--port", str(int(self.config["port"])),
            "--ctx-size", str(int(self.config["context_size"])),
            "--threads", str(int(self.config["threads"])),
            "-m", str(model),
        ]
        creationflags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
        self.process = subprocess.Popen(
            command, cwd=str(ROOT), stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            creationflags=creationflags,
        )
        print("Iniciando el modelo local...")
        deadline = time.monotonic() + 180
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(
                    "El motor se cerró al iniciar. Revisa la versión de llama.cpp y el modelo."
                )
            try:
                request_json(self.base_url + "/health", timeout=2)
                print("Modelo listo. No se necesita internet.\n")
                return
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
                time.sleep(1)
        self.stop_engine()
        raise TimeoutError("El motor tardó demasiado en iniciar.")

    def stop_engine(self) -> None:
        if self.process and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=8)
            except subprocess.TimeoutExpired:
                self.process.kill()
        self.process = None

    def status(self) -> None:
        if self.process is None:
            print("Motor: no iniciado por esta sesión")
            return
        if self.process.poll() is not None:
            print("Motor: detenido")
            return
        try:
            request_json(self.base_url + "/health", timeout=3)
            print(
                f"Motor: activo | Dirección: {self.base_url} | "
                f"Conversación: {len(self.history)} mensajes"
            )
        except Exception:
            print("Motor: proceso activo, todavía no responde")

    def ask(self, prompt: str) -> None:
        self.history.append({"role": "user", "content": prompt})
        payload = {
            "model": "local-model",
            "messages": self.history,
            "temperature": float(self.config["temperature"]),
            "max_tokens": int(self.config["max_tokens"]),
            "stream": False,
        }
        try:
            result = request_json(
                self.base_url + "/v1/chat/completions", payload, timeout=300
            )
            answer = result["choices"][0]["message"]["content"].strip()
            self.history.append({"role": "assistant", "content": answer})
            print(f"\nPREPA AI > {answer}\n")
        except (
            urllib.error.URLError, TimeoutError, KeyError, IndexError,
            json.JSONDecodeError, OSError
        ) as exc:
            self.history.pop()
            print(f"No se pudo obtener respuesta: {exc}\n")

    def run(self) -> None:
        print("PREPA AI | CLI local")
        print("Escribe /ayuda para ver comandos. /salir para cerrar.\n")
        self.start_engine()
        try:
            while True:
                try:
                    line = input("Tú > ").strip()
                except (EOFError, KeyboardInterrupt):
                    print("\nCerrando PREPA AI...")
                    break
                if not line:
                    continue
                command = line.lower()
                if command in {"/salir", "/exit", "/quit"}:
                    break
                if command in {"/ayuda", "/help"}:
                    print("Comandos: /ayuda  /estado  /limpiar  /salir\n")
                elif command == "/estado":
                    self.status()
                elif command == "/limpiar":
                    self.history.clear()
                    print("Conversación actual borrada de memoria.\n")
                elif command.startswith("/"):
                    print("Comando desconocido. Escribe /ayuda.\n")
                else:
                    self.ask(line)
        finally:
            self.stop_engine()
            print("Motor detenido. Hasta luego.")


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] in {"--help", "-h"}:
        print("PREPA AI CLI\nUso: prepa-ai.bat\nComandos internos: /ayuda, /estado, /limpiar, /salir")
        return 0
    try:
        PrepaAI(load_config()).run()
        return 0
    except (FileNotFoundError, RuntimeError, TimeoutError, ValueError) as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
