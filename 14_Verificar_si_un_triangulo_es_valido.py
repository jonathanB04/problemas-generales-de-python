#Escribe un programa que solicite las longitudes de los tres lados de un triángulo y
#determine si es un triángulo válido (la suma de las longitudes de dos lados debe ser
#mayor que la longitud del tercer lado).
print("---------------------------------------------")
print("|-          año de un siglo                -|")
print("---------------------------------------------")
lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Es un triángulo válido: ")
else:
    print("No es un triángulo válido: ")
