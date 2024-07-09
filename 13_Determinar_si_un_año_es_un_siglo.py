#Escribe un programa que solicite un año al usuario y determine si es el primer año de
#un siglo (por ejemplo, 1900, 2000, 2100).
print("---------------------------------------------")
print("|-          año de un siglo                -|")
print("---------------------------------------------")
año = int(input("Ingrese un año: "))

if  1900 <= año <= 2100:
    print("es el primer año de un siglo.")
else:
    print("no es el primer año de un siglo.")
