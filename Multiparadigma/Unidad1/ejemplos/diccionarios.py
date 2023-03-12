#son dinamicos, no tienen un orden, tienen un indice que es la llave que le damos a las propiedades
#pueden ser anidados, un diccionario puede estar dentro de otro y se puede acceder y modificar los elementos
d1 = {
    "Nombre":"Rocio",
    "Edad":24,
    "documento":2321
    }
print(d1)

d3 = dict(nombre ="rocio", edad=24, documento=123213)
print(d3)
print(d1["Nombre"])
print(d1.get("Nombre"))

d1["Nombre"] = "juan"
print(d1)
d1["Direccion"] = "calle 123"
print(d1)


for x in d1:
    print(d1[x])

for x,y in d1.items():
    print(x,y)
    
d1 = {"a":1, "b":2}
d2 ={"c":3,"d":4}

d={
    "d1":d1,
    "d2":d2    
}

print(d)

print(d.get("a")) #regresa valor si esa lalve existe
it = d.items() #regresa lista iterable
print(list(it))
print(list(it)[1][0])
print(d)

k = d.keys()
print(k)
print(list(k)[1])
d.pop('d1')
print(d)
pop = d.pop("d3",-1)
print(pop)
d.popitem()
print()

d1 = {'a':1,"b":2}
d2 = {"a":223,"d":122}

d1.update(d2)
print(d1)

d2.update(d1)
d1.update(d2)
print(d2)


d.clear() #limpia todas las llaves
