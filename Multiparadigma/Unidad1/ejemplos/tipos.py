#tipos de datos numericos
#entero
#integer = 1
#integernegativo = -1
#integercero = 0
#print(type(integer), integer, id(integer))
#print(type(integernegativo), integernegativo, id(integernegativo))
#print(type(integercero), integercero, id(integercero))
#flotante

#flotante = 3.5
#flotanten = -3.5
#flotantec = 0.0

#print(type(flotante), flotante, id(flotante))
#print(type(flotanten), flotanten, id(flotanten))
#print(type(flotantec), flotantec, id(flotantec))

#complejos

#complexN = 5j+4j
#complexNN = -5j
#complexNC = 0J

#print(type(complexN), complexN, id(complexN))
#print(type(complexNN), complexNN, id(complexNN))
#print(type(complexNC), complexNC, id(complexNC))

#intafloat = int(integer)
#intafloatN = float(integernegativo)
#intafloatC = float(integercero)
#print(type(intafloat), intafloat)
#print(type(intafloatN), intafloatN)
#print(type(intafloatC), intafloatC)

#floatToInt = int(flotante)
#print(type(floatToInt), floatToInt)

#BOOLEANO

#x= 10
#y = 5
#print(bool(x == y))
#x = None
#print(bool(x))
#tupla
#x=(3,1)
#print(bool(x))
#x={}
#print(bool(x))
#x = 0.1
#print(bool(x))
#cadenaV = "hola"
#cadena = ""
#print(bool(cadenaV), bool(cadena))

#cadenas

print(type("hello"), "hello")
saludo = "hola"
despedir = "adios"
print(saludo)
print("saludo", end=", ")
print("adios")
#interpolacion
print(f"""saludo: {saludo}
despedida: {despedir}""")
for letra in saludo:
    print (letra)

#invertir cadena ctrl k c ctrl

print(saludo[::-1])

