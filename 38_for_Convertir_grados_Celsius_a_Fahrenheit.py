print("Pide al usuario un rango de temperaturas en grados Celsius (inicio y fin) y muestra la conversión a Fahrenheit para cada grado en ese rango usando un ciclo for.")
print("---------------------------------------------------------------------------------\n")

inicio = int(input("ingresa inicio de grados celcius: "))
fin = int(input("ingresa fin de grados celcius: "))
print("convercion de celcius a farenheit: ")
for celcius in range (inicio,fin,+1):
	farenheit = (celcius * 9/5)+32
print(f"{celcius} en grados celcius es {farenheit} en grados farenheit.")