#escribir un programa en el cual se pide una frase y una letra, escribir en pantalla el numero de veces que se repite la letra

print("Inserte la palabra")
palabra = input()
print("Inserte la letra")
letra = input()
contador = 0
for n in palabra:
    if letra == n:
        contador += 1

print("se repitio: ", contador)
