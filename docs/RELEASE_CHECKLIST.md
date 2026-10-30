# Lista de verificación para PREPA AI v1.0

## Código
- [ ] Todas las pruebas unitarias pasan en Windows.
- [ ] El ejecutable se inicia desde una carpeta con espacios en el nombre.
- [ ] El CLI informa cuando falta el motor o el modelo.
- [ ] El cierre detiene únicamente el proceso iniciado por PREPA AI.
- [ ] El historial desaparece al cerrar la sesión.

## Componentes
- [ ] Versión y arquitectura del motor llama.cpp documentadas.
- [ ] Origen, licencia e integridad del modelo comprobados.
- [ ] Ejecutable PyInstaller probado en Windows x64.
- [ ] Paquete portable probado sin Python instalado.

## Equipo destino
- [ ] Probado sin internet después de copiar los componentes.
- [ ] Probado con permisos normales, sin administrador.
- [ ] Rendimiento y uso de RAM medidos en el equipo más limitado.
- [ ] Reglas del laboratorio permiten ejecutar la aplicación.

## Privacidad
- [ ] No se guardan conversaciones en disco.
- [ ] No se incluyen claves API.
- [ ] El servidor escucha solo en 127.0.0.1.
- [ ] No se intenta evadir controles de red o del equipo.
