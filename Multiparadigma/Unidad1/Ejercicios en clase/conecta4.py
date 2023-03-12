#la entrada seran 2 jugadores
#o mayuscula y x mayuscula
#el tablero es de 6 filas por 7 columnas
#se debe visualizar el recorrido de las fichas
#el jugador debe elegir la columna donde quiere su ficha
#gana el primero que agrupe 4 fichas en horizontal, vertical o diagonal
#si se acaba el espacio en el tablero es empate
#de lo contrario mostrar un mensaje del ganador
contador =0
matriz = [[0 for j in range(7)] for i in range(6)]
for n in range(6):
    print(matriz[n])
while(True):
    print("del escoja la columna del 0 al 7")
    numcol = int(input())
    
    for n in reversed(range(6)):
        if matriz[n][numcol] == 0:
           matriz[n][numcol] = "x"
           break
        elif matriz[n][numcol] != 0:
            continue
    contadorGanadorx =0
    for j in range(6):
        print(matriz[j])
        for y in range(7):
            if matriz[j][y] == "x":
                contadorGanadorx += 1
            elif matriz[j][y] != "x":
                contadorGanadorx = 0
            if contadorGanadorx == 4:
                print("el ganador es x")
            