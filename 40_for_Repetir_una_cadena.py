print("Pide al usuario una cadena de texto y un número entero positivo NNN.Muestra la cadena repetida NNN veces, cada vez en una nueva línea, usando un ciclo for.")
print("----------------------------------------------------------------------------------\n")

texto = input("Ingrese una palabra: ")
numero = int(input("Ingrese un numero entero positivo: "))
for i in range(1, numero+1):
	print(texto)