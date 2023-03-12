from psycopg2 import pool
from logger_base import log

class Conexion:
    _databse = "test_db" #probar
    _Username = "postgres"
    _Password = "admin"
    _DBPort = "5432"
    _Host = "127.0.0.1"
    _Min_Con = 1
    _Max_Con = 5
    _pool = None
    
    
    @classmethod
    def ObtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool( cls._Min_Con, cls._Max_Con, host=cls._Host, username=cls._Username, passowrd= cls._Password
                                                        , dbport = cls._DBPort, database = cls._databse)
                log.debug(f"Creacion del pool {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error("error en el pool",e)
        else:
            return cls._pool
        
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.ObtenerPool().getconn()
        log.debug(f"Conexion obtenida {conexion}")
        return conexion
    
    @classmethod
    def liberarConexion(cls,conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debu(f("Conexion regresada: {conexion}"))
        
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerConexion().closeAll()
if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    