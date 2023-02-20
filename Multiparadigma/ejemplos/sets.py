#set
#son similares a las listas pero tienen ciertas diferencias, por ejemplo no permiten datos duplicados
#son listas mutables e inmutables a la vez 
#a= set[5,4,3,2,1,8] #en este caso elimina el ultimo 2
#son mutables ya que puedo agregar datos, pero sin embargo los que estan dentro no puedo liminarlos ni editar
#la posicion que ya tienen
#print(a)
#para declarar un set vacio tengo que: {0} ya que si no pongo el 0 lo toma como un diccionario

#s = {0}
#d ={}
#print(type(s))
#print(type(d))

#no puede tener listas anidadas
#lista = ["Mexico", "España"]
#a = set (["usa", "tlaxcala"])

s = {2,3,4,6,7}
s.add(5)    #añade
s.remove(3) #elimina pero si no esta marca error
s.discard(6) #lo busca pero si no esta no hace nada, si si lo elimina
s.pop() #elimina el primero de la lista

print(s)
s.clear() #limpia todos los elementos

s1 = {1,2,3}
s2 = {3,4,5,6}

print(s1.union(s2))
print(s1.intersection(s2))