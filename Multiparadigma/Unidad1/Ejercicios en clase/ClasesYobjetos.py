#crear una clase llamada cuenta con los atributos titular y cantidad, 
#el titulo sera obligatorio y cantidad opcional, la clase debe contener lo siguiente:
#un constructor donde los datos puedan estar vacios
#seters y gethers de cada atributo pero el atributo de cantidad no se puede modificar utilizando
#el seter (no crearle), metodo mostrar que muestre los datos del objeto
#metodo de ingresar y un metodo retirar, los numeros pueden estar en 0

class cuenta():
    
    def __init__(self) -> None:
        pass
    def __init__(self,titular = "", cantidad =0):
        self._titular = titular
        self._cantidad = cantidad
    
    @property
    def getTitular(self):
        return self._titular
    @getTitular.setter
    def setTiular(self,t):
        self._titular = t
    
    @property
    def getCantidad(self):
        return self._cantidad
    
    def Mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.cantidad)
        return f'Titular: {self._titular} Saldo: {self._cantidad}'
    
    def ingresar(self,ingreso):
        self.cantidad += ingreso
    def retirar(self,retiro):
        self.cantidad -= retiro

    class CuentaJoven(cuenta):
        def __init__(self, titular, cantidad, bonificacion, edad) -> None:
            super().__init__(titular, cantidad)
            self._bonificacion = bonificacion
            self._edad = edad
            
