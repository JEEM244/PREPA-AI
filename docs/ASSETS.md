# Componentes para el modelo local

PREPA-AI está separado en varias partes para que el repositorio no tenga que guardar archivos muy pesados.

**Ojo:** esta guía registra los componentes elegidos para una primera prueba. La integración de llama.cpp con la CLI todavía no está terminada, así que descargar estos archivos no significa que PREPA-AI ya pueda conversar con el modelo.

## Componentes que estoy considerando

| Parte | Selección para las pruebas |
|---|---|
| Motor | llama.cpp para Windows x64, usando CPU |
| Modelo | Qwen2.5 1.5B Instruct GGUF, Q4_K_M |

Fuentes del proyecto:

- [Versiones de llama.cpp](https://github.com/ggml-org/llama.cpp/releases)
- [Modelo Qwen2.5 1.5B Instruct GGUF](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF)

Antes de descargar cualquier archivo revisa que sigas en la página oficial, la versión, la arquitectura y la licencia.

## Estructura que se espera usar

```text
PREPA-AI/
├── PREPA-AI.exe
├── prepa-ai.bat
├── config.json
├── runtime/
│   └── archivos de llama.cpp
└── models/
    └── modelo.gguf
```

Los nombres exactos pueden cambiar cuando se termine de integrar el motor.

## Por qué se descargan aparte

El motor y el modelo ocupan bastante espacio y tienen sus propias versiones y licencias. Por eso no se guardan dentro del repositorio de GitHub.

No mezcles archivos de distintas versiones de llama.cpp. Si una compilación necesita DLL, deben venir de la misma descarga que el ejecutable.

## Comprobar los archivos

El proyecto incluye un script para revisar los componentes locales:

```powershell
.\scripts\check-assets.ps1
```

También puedes obtener el hash de un archivo con:

```powershell
Get-FileHash .\runtime\llama-server.exe -Algorithm SHA256
```

## Uso sin internet

La meta es descargar los componentes en una conexión autorizada y después poder ejecutar el modelo localmente. Todavía falta comprobar todo el flujo en una computadora Windows sin conexión.
