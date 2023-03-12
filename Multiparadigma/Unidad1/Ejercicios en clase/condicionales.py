#una pizzeria ofrece pizzas vegetarianas y no vegetarianas con un listado de ingredientes.
#ingredientes vegetarianos = pimiento y tofue
#ingredientes no vegetarianos: peperoni, salmon y jamon
#escribir un programa si se quiere una pizza vegetariana o no
#en funcion a la respuesta desplegar el menu de ingredientes, se puede elegir maximo 2 ingredientes y minimo 1
#ademas la mozarella estan en todas las pizzas
#y al final se debe mostrar en pantalla si la pizza es vegetariana o no
#y todos los ingredientes

print("¿Quiere pizza vegetariana?")
print("1- Si")
print("2- No")
decision = input()
contador = 0
ingrediente= []
while(True):
    if decision.lower() == "si" or decision == "1":
        print("#menu#")
        print("Pimiento")
        print("Tofu")
    print("Peperoni")
    print("Salmon")
    print("Jamon")
    if contador == 1:
        print("salir")
    ingrediente.insert(contador, input("seleccione un ingrediente: "))
    if contador == 2 or contador == "salir":
        
        break
    contador += 1
print("ingredientes: ")
for n in ingrediente:
    print(n)
print("Es vegana? ", decision)

    
