def mifuncion(x):
    print("hola mundo", x)

mifuncion(21)

def resta(a,b,c):
    return a-b-c
print(resta(b=12, a=15, c=32)) 

def suma(a=5,b=3,c=12):
    return a+b+c
print(suma())

#metodos con parametros de longitud variable

lista = [1,5,7,8]

def Suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(Suma(lista))

def Suuma(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total
    
print(Suuma(1,2,3,4,5,6,7,8))

def suuuma(**Kwargs):
    suma = 0
    for key,value in Kwargs.items():
        print(key, value)
        suma += value
    return suma

print(suuuma(b=2,c=5,a=4, pedro =2))

def suma(**Kwargs):
    suma = 0
    for key,value in Kwargs.items():
        print(key, value)
        suma += value
    return suma
di = {"a": 10, "b":12, "c":13}
suma(**di)

def sumaMedia(a,b,c):
    suma = a+b+c
    media = suma/3
    return suma, media
sumaResultado,sumaResultadoMedia = sumaMedia(1,2,30)
print(sumaMedia(1,2,30))
print(sumaResultado)
print(sumaResultadoMedia)

def mifuncionSuma(a,b):
    """
    descripcion util de la funcion, como debe ser usada, parametros etc
    """
    return a+b
print(mifuncionSuma(1,2))

help(mifuncionSuma)
print(mifuncionSuma.__doc__)

def multiplicar(numero:int, numerodos:int) -> float:
    return numero * numerodos

print(multiplicar(5,5))
print(type(multiplicar(5,5)))


def funcion(a,b,*args, **kwargs):
    print(a)
    print(b)
    for n in args:
        print(n)
    for key, value in kwargs.items():
        print(key,value)

funcion(10,2,10,5,12,3,5,1,x=1,v=3,y=10)

numerosL = list(range(1,101,1))
print(numerosL)

def sumanumeros(*numeros):
    suma=0
    for n in numeros:
        suma += n
    return suma
print(sumanumeros(*numerosL))
