print("programa que elija un número aleatorio entre 1 y 10 y permita al usuario adivinarlo,dándole pistas de mayor o menor hasta que acierte utilizando el ciclo while")
print("----------------------------------------------------------------------------------\n")

numero = 37 # ingrese el numero a encontrar
cont = 0 
intento = 1
print("adivina el numero")
while (cont == 0):
	print(f"intento {intento}")
	print(f"ingresa un numero")
	num = int(input())
	if num == numero:
		print("adivinaste el numero")
		print("fin del juego")
		print(f"intentaste {intento} veses")
		cont = 1
	elif num < numero:
		print(f"el numero es mayor a {num}")
		intento += 1
	elif num > numero:
		print(f"el numero es menor a {num}")
		intento += 1		