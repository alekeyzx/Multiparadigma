#en una matriz de 5*4 pedir al usuario los valores
#en una segunda matriz guardar 1 si el numero guardado en la misma posicion es multiplo de 3
#guardar un 2 si el numero es multiplo de 5
#o guardar un 3 si es multiplo de 3 y 5 a la vez
#si no se cumple ninguna de las anteriores, guardar un 0
#imprimir ambas matrices en formato de matriz

matriz = [[0 for j in range(4)] for i in range(5)]
matriz2 = [[0 for j in range(4)] for i in range(5)]
print(matriz)
print("inserte los valores:")
for n in range(5):
    for b in range(4):
        matriz[n][b] = int(input())

for n in range(5):
    for b in range(4):
        if matriz[n][b] % 3 == 0 and matriz[n][b] % 5 == 0:
            matriz2[n][b] = 3
        elif matriz[n][b] % 3 == 0:
            matriz2[n][b] = 1
        elif matriz[n][b] % 5 == 0:
            matriz2[n][b] = 2
        else:
            matriz2[n][b] = 0
print(matriz)
print(matriz2)
        

