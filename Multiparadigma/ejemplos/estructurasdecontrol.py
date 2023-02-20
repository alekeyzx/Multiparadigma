#estructuras de control

#if

a = 4
b = 0

if a == b:
    print("es igual")
    
else:
    pass #sirve para que no de error

if b != 0:
    print(a/b)
print(b)

a = 10
if a > 5 and a < 15:
    print("a mayor que 5 y menor que 15")

if a > 5: print(a); print(b)

x=5
if x==5:
    print("es 5")
elif x == 4:
    print("Es 4")
elif x == 1:
    print("es 1")
else:
    print(x)
    
print("es 5" if x == 5 else "no es 5")

a = 10
b = 5
c = a/2 if b != 0 else -1
print(c)

#for
for i in "hola":
    print(i) 

lista = [[54,34,2],[12,4,5],[9,3,2]]
for i in lista:
    print(i)
    for j in i:
        print(j)

#funciones de rango:
rango = range(10)
print(rango)

for rango in range(-1,10,2):
    print(rango)
    if (rango == 5):
        break
    
for letra in "Python":
    if letra == "Y":
        print(letra)
        break

for letra in "PythonP":
    if letra == "P":
        continue
    print(letra)

x = 5
while x > 0:
    print(x)
    x -= 1
    
while x > 0: print(x); x-=1

x=5
while x > 3:
    print(x)
    x-=1
    if x == 4: break
else:
    print("Bucle finalizado")
    x = 5
z=7
x=1

while z>0:
    print(" "*z + "*"*x + " "*z)
    x+=2
    z-=1
    
c = input()
print(c)
sum()