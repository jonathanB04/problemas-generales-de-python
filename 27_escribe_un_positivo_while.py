print("Pide al usuario que ingrese un número positivo.Si el usuario ingresa un número negativo, solicita nuevamente la entrada hasta que ingrese un número positivo. Usa un ciclo while")
print("----------------------------------------------------------------------------\n")

p = -1
suma = 0
while p<0:
	p = int(input("ingrese un positivo: "))
	if p<0:
		suma = suma + p
	elif p>=0:
		print("fin")