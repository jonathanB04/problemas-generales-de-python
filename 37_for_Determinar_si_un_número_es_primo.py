print("Pide al usuario un número entero positivo y determina si es primo usando un ciclo for.")
print("----------------------------------------------------------------------------------\n")

numero = int(input("Ingrese el numero: "))
primo = True

for i in range(2, numero):
	if numero % i == 0:
		print("No es primo,", i, "es divisor")
		primo = False
		break
if primo:
	print("Es primo")