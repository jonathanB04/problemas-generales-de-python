print("Pide al usuario un número entero positivo y muestra su tabla de multiplicar del 1 al 10 usando un ciclo for.")
print("---------------------------------------------------------------------------------\n")
i = float(input("escribe la tabla: "))
print(f"tabla del {i}")
for num in range(1,11):
	res = i * num
	print(f"{i} × {num} = {res}")		