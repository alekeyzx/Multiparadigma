from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipoExcepcion,mensajeExcepcion,detalleExcepcion):
        log.debug("sale with")
        if mensajeExcepcion:
            log.error("error",mensajeExcepcion)
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ =="__Main__":
    with CursorDelPool() as cursor:
        cursor.excecuteu("Select * from persona")
        log.debug(cursor.fetchall())