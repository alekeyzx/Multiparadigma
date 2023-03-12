#crear una funcion que reciba 2 listas de no necesariamente misma longitud y devuelva 2 listas, 
#la primera lista tendra los elementos que coinciden entre las 2 listas
#la segunda lista tendra los elementos que no coinciden entre las 2 listas
#imprimir en pantalla 2 lista

def compararlistas(lista1,lista2):
    elemntosiguales = []
    elementosdiferentes = []
    for elemento in lista1:
        if elemento in lista2:
            elemntosiguales.append(elemento)
        else:
            elementosdiferentes.append(elemento)
    for elemento in lista2:
        if elemento not in lista1:
            elementosdiferentes.append(elemento)
    return elemntosiguales, elementosdiferentes

lista1 = ["a","b",2,2,3]
lista2 = ["c","d",3,4]

iguales, diferentes = compararlistas(lista1,lista2)

prueba1 = set(iguales)
prueba2 = set(diferentes)

print("lista 1:", lista1, "lista 2:",lista2)
print("elementos iguales:", list(prueba1) )
print("elementos diferentes:", list(prueba2))

