#escribe un programa que pregunte el nombre de un producto, su precio y su numero de unidades y que muestre en pantalla el nombre del producto
#seguido de su precio unitario con 6 digitos y 2 decimales, el numero de unidades con 3 digitos, y el coste total 8 digitos y 2 decimales

nombre_producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio unitario del producto: "))
num_unidades = int(input("Introduce el número de unidades: "))

# Calculamos el coste total del producto
coste_total = precio_unitario * num_unidades

# Mostramos en pantalla la información solicitada
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: {precio_unitario:0.2f}")
print(f"Número de unidades: {num_unidades:03}")
print(f"Coste total: {coste_total:8.2f}")
