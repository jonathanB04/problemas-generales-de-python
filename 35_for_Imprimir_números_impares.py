print("Pide al usuario un número entero positivo y muestra todos los números impares del 1 hasta ese número usando un ciclo for.")
print("---------------------------------------------------------------------------------\n")

inicio = int(input("escribe el numero inicial:"))
fin = int(input("escribe el nuemro final:"))
print("los numeros imparares del intervalo \n")
for i in range(inicio, fin + 1):
	if i % 2 !=0:
		print(i)
		