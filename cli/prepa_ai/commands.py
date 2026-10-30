HELP="""Comandos de PREPA AI:
  /ayuda       Mostrar esta ayuda
  /estado      Revisar el estado del motor local
  /limpiar     Borrar la conversación de esta sesión
  /modelo      Mostrar la ruta del modelo configurado
  /salir       Cerrar PREPA AI y detener el motor

Cualquier otro texto se envía al modelo local."""
ALIASES={"/help":"/ayuda","/exit":"/salir","/quit":"/salir",
         "/clear":"/limpiar","/status":"/estado"}

def normalize_command(line:str)->str:
    command=line.strip().lower()
    return ALIASES.get(command,command)
