from Persona import Persona

from cursosDelPool import CursorDelPool

from logger_base import log

class personaDAO:
    _Seleccionar = "select * from persona order by IdPersona"
    _Insertar = "insert into Persona(Nombre, Apellido, Email, Edad) values ({},{},{},{})"
    _Actualizar = "update persona set Nombre={}, Apellido={}, Email={}, Edad={} where Idpersona={}"
    _Eliminar="Delete from persona where idPersona={}"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool as cursor:
            cursor.execute(cls.seleccionar)
            registros = cursor.fetchall()
            Personas = []
            for r in registros:
                Persona = Persona(r[0],r[1],r[2],r[3],r[4])
                Personas.Append(Persona)
            return Persona
        
    @classmethod
    def insertar(cls, persona):
            with CursorDelPool as cursor:
                valores = (persona.Nombre,persona.Apellido, persona.Email,persona.Edad)
                cursor.execute(cls._Insertar,valores)
                return cursor.rowcount
                
                
    def actualizar(cls, persona):
            with CursorDelPool as cursor:
                valores = (persona.Nombre,persona.Apellido, persona.Email,persona.Edad, persona.IdPersona)
                cursor.execute(cls._Actualizar,valores)
                return cursor.rowcount
            
            
    @classmethod
    def eliminar (cls, persona):
        with CursorDelPool as cursor:
                valores = (persona.idPersona,)
                cursor.execute(cls._Eliminar, valores)
                return cursor.rowcount
    
if __name__ =="__Main__":
    persona1 = Persona(Nombre="pedro", Apellido="Ramirez", Email="pedror@hotmail.com", Edad="23")
    personaInsertada = personaDAO.insertar(persona1)
    log.debug(f"persona agregada {personaInsertada}")
    #leer
    persona = personaDAO.seleccionar()
    for p in persona:
        log.debug(p)

    