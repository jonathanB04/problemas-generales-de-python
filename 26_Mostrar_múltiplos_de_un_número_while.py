print("Pide al usuario un número entero positivo y muestra sus múltiplos del 1 al 10 usando un ciclo while.")
print("-----------------–---------------------------------------------------------------\n")

tabla = float(input("escribe la tabla que quieras ver: "))
comienzo = 1

while comienzo <= 10:
	resultado = tabla * comienzo
	print(f"{tabla} × {comienzo} = {resultado}")
	comienzo += 1