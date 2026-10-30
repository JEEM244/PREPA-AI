# Arquitectura de PREPA AI

## Principio central

La CLI y la interfaz web son dos clientes del mismo backend. Ninguna interfaz inicia una copia independiente del modelo.

```text
CLI (terminal) ─────┐
                    ├── Backend local ─── llama.cpp ─── modelo GGUF
Web (navegador) ────┘       │
                            ├── conversaciones locales
                            ├── preferencias locales
                            └── proveedores online opcionales
```

## Componentes

### Backend

Responsabilidades:

- administrar el ciclo de vida del servidor de inferencia;
- exponer una API HTTP local;
- validar entradas y límites de contexto;
- gestionar conversaciones y preferencias;
- ofrecer un estado de salud del motor;
- detener únicamente los procesos que inició.

### CLI

Cliente de terminal que consume la API local. Debe permitir conversar, seleccionar conversaciones, consultar el estado del motor y abrir la ayuda. No debe duplicar la lógica de inferencia.

### Web

Aplicación estática servida por el backend en loopback. Consume la misma API que la CLI. No debe depender de CDNs ni recursos externos para funcionar offline.

### Motor y modelo

Se descargan por separado del repositorio. La primera implementación utilizará llama.cpp con un modelo GGUF compatible. El modelo se seleccionará por configuración y se validará antes de iniciar.

## Almacenamiento

El código versionado vive en el repositorio. Los datos del usuario viven en un directorio local de datos, separado del código y excluido de Git.

La ruta de datos debe resolverse de forma explícita y mostrarse en la pantalla de privacidad. No se deben guardar conversaciones dentro de carpetas sincronizadas o compartidas por defecto.

## Red

- El backend escucha exclusivamente en `127.0.0.1`.
- No se habilita acceso desde otros equipos.
- Las llamadas a proveedores online son opcionales y configurables.
- No se incluyen proxies, túneles ni mecanismos para evadir controles de red.

## Portabilidad

La aplicación debe evitar dependencias globales. Se evaluará distribuir un runtime de Python portable o un ejecutable firmado/revisado. Los binarios de terceros se obtendrán de sus fuentes oficiales y no se incluirán en Git sin revisar tamaño y licencia.
