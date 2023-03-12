#una chocolateria lanza un nuevo producto el cual viene presentado en barras de n segmentos
#las barras solo vienen en tamaños que son pteoncia de 2 es decir 1,2,4,8,16
#realizar un programa para realizar una prueba de calidad de dicho producto pero para ello tienes que probar al menos k segmentos
#la barra solo se puede partir a la mitad
#el programa determinara el numero de veces que quebraras la barra parao btener exactamente k segmentos
#la salida sera el tamaño minimo de la barra que se tendra que pedir para tomar los k segmentos y el
#segundo numero es el menor numero de veces que tendras que romper la barra

k = input("Inserte el numero de segmentos: ")
pot = 1
cont = 0
prueba = 0
particiones = 0
divisones =0
while(True):
    n = pow(pot,1)
    if n == int(k):
        print(k, n,cont)
        break
    elif n > int(k):
        divisones=n
        while True:
            cont += 1
            particiones = divisones / 2
            divisones = particiones
            prueba = prueba + particiones
            if prueba > int(k):
                prueba = prueba - particiones
                
            elif prueba == int(k):
                print(k, n,cont)
                break
        break
    else:
        pot = pot*2

   