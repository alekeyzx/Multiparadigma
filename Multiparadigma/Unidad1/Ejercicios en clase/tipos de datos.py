#tipos de datos:
#una jugeteria vende 2 tipos de productos, payasos y muñecas, hace su venta por correo y la logistica les cobra por peso de cada paquete
#se debe calcular el peso de los payasos y muñecas, cada payaso pesa 112 gr y cada muñeca 75 gr
#escribir un programa en el cual se capture numero de payasos y muñecas, calcule el peso total del paquete y el precio total, si por cada 100 gramos
#de payaso se cobra 2.5 pesos y por cada 100 gr de muñeca se cobran 2 pesos

print("inserte el numero de payasos:")
payasos = float(input())
print("inserte el numero de muñecas:")
muñecas = float(input())

pesoTotalPayasos = (payasos*112)
precioPayasos = (pesoTotalPayasos/ 100) * 2.5
pesoTotalMuñecas = (muñecas * 75)
precioMuñecas = (pesoTotalMuñecas/ 100) * 2

print("precio final payasos:", str(precioPayasos)+  "$", "Peso payasos:", str(pesoTotalPayasos) + " 5gr")
print("Precio final muñecas:", str(precioMuñecas)+ "$", "Peso Muñecas:", str(pesoTotalMuñecas)+ " gr")