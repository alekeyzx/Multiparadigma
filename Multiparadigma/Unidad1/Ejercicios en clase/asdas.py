#crear una cuenta llamada cuenta joven derivada de la aneterior
#se le agregara un atributo llamada bonificacion expresada en porcentaje
#constructor seters y geters
#los titulares de este tipo de cuenta tienen que ser mayores de edad
#la retirada solo se podra hacer si el titular es mayor de edad y si tiene dinero en la cuenta
#el metodo mostrar debe devolver el mensaje de cuenta joven y la bonificacion de la cuenta
class cuentajoven():
    
    def __init__(self) -> None:
        pass
    def __init__(self,titular = "", bonificacion= "", edad =0, cantidad=0):
        self.titular = titular
        self.cantidad = 0
        
        if edad >= 18:
            self.edad = edad
        else:
            print("no se puede ya que es menor de edad")
        self.bonificacion = bonificacion
        
    
    def Mostrar(self):
        print("Titular: ", self.titular)
        print("edad: ", self.edad)
        print("bonificacion: ", self.bonificacion)
        print("Cantidad: ", self.cantidad)
    
    def ingresar(self,ingreso):
        self.cantidad += ingreso
    def retirar(self,retiro):
        if self.cantidad >= 0 and self.cantidad - retiro > 0:
            self.cantidad -= retiro
        else:
            print("el saldo es negativo")
prueba = cuentajoven("juan",10,10)
prueba.Mostrar()
prueba.ingresar(300)
prueba.Mostrar()
prueba.retirar(500)
prueba.Mostrar()