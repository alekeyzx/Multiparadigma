a = [[1,2,3],[4,5,6]]
b = [[-1,0],[0,1],[1,1]]
#escribir un programa que almacene las matrices en una tupla y muestre en pantalla su producto
#el producto debe estar dado en listas anidadas.

#en resumen debe quedarnos= [2,5],[2,11]
#1*-1 + 1*0, 2*-1 +2*0 , 3*-1 + 3*0 = -1 + 0, -2 + 0, -3 +0 = 
resultado = 0
c = [[0,0],[0,0]]
suma =0
for n in range(len(a)):
    for j in range(len(b[1])):
        for k in range(len(b)):
            c[[n],[j]] = int(a[k]) * int(b[k])

print(c)
            
            