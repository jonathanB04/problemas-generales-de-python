print("Calcular el precio con descuento:")
print("================================\n")

precio = float(input("ingresa el precio del producto "))
precio_final = precio * 0.10
if precio >= 100:
	print(f"es alto de precio:{precio_final}")
	
elif precio < 100:
	print(f"no es alto el precio:{precio_final}")