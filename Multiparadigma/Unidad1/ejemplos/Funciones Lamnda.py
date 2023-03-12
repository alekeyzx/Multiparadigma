#es una funcion anonima, se le llama asi por que no tiene nombre.
#se utilizan para ahorrate codigo. no declaras el nombre de la funcion, pero se puede
#guardar o ejecutar en el momento.
#en js se utilizan despues de hacer una llamada a un servidor, para que el proceso usas una funcion para procesar el resultado
#en python va de lo mismo pero sirve para moldes de mas funciones

x=0
suma = lambda a: print(a+10)
suma(10)
(lambda z: z+x)(15)
print(x)
(lambda *n:print(sum(n)))(*list(range(0,101,1))) #se utiliza el * para solo enviar lo que esta dentro de la lista y no lo que esta fuera

def multiplicador(a):
    return lambda b:print(a*b)

duplicador = multiplicador(2)
duplicador(50)

triplicador = multiplicador(3)
triplicador(100)

#excepciones:
try:
    por10 = multiplicador(10)
    por10(15+10)
except Exception as e:
    print("ocurrio un error: "+ e)
else:
    por10(5)
finally:
    print("reiniciando")

#acerciones son valores booleanos que se usan mucho para hacer testing
#assert
def suma(a,b): 
    try:
        assert(type(a)== int)
        assert(type(b)== int)
        print(a+b)
    except AssertionError as e:
        print("No son enteros")
suma(1.1,2)
suma(5,5)

def sumacien(*n):
    assert(sum(n)== 5050)
    print(sum(n))
sumacien(*list(range(0,102,1)))