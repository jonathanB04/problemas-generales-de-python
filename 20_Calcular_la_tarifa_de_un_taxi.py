#Escribe un programa que solicite la distancia recorrida en kilómetros y calcule la tarifa
#del taxi. La tarifa es $2.50 por kilómetro para los primeros 10 kilómetros y $2.00 por
# kilómetro adicional.

distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
if distancia <= 10:
    distancia = 10 
    tarifa = distancia * 2.50
else:
    tarifa = 10 * 2.50 + (distancia - 10) * 2.00

print("La tarifa del taxi es: ",tarifa)
