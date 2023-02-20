#escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, preguntar al usuario por la fruta
#y el numero de kilos y muestre en pantalla el precio de ese numero de kilos
#si la fruta no esta en el diccionario debe mostrar un mensaje informando
Frutas = {
    "platano":1.35,
    "manzana":0.80,
    "pera":0.85,
    "naranja":0.70
    }
print("Seleccione una fruta",)
frutaSeleccionada = input()


if frutaSeleccionada in Frutas:
    print("¿cuantos kilos?")
    kilos = float(input())
    resultado = Frutas.get(frutaSeleccionada) * kilos
    print(resultado)
else:
    print("fruta no existe")
 
