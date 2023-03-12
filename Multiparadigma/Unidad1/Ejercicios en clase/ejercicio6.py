#crea una funcion que reciba 2 lista de no necesariamente la misma longitud 
#y devuelva 2 listas, la primer lista tendra los elementos que coinciden entre las 2 listas, la segunda 
#lista tendra los elementos que no coinciden entre las dos listas

def comparar_listas(lista1, lista2):
    elementos_comunes = []
    elementos_no_comunes = []
    
    for elemento in lista1:
        if elemento in lista2:
            elementos_comunes.append(elemento)
        else:
            elementos_no_comunes.append(elemento)
    
    for elemento in lista2:
        if elemento not in lista1:
            elementos_no_comunes.append(elemento)
    
    return elementos_comunes, elementos_no_comunes

lista1 = ["a","b",2,3]
lista2 = ['c','d',3,4]
resultados = comparar_listas(lista1, lista2)
print(resultados)