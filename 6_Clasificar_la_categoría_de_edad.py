print("Clasificar la categoría de edad:")
print("===============================\n")
print("ingrese la edad de la persona: ")

edad = int(input())

if edad>=0 and edad<=12:
	print("infantil")
	
elif edad>=13 and edad<=19:
	print("adolecente")
	
elif edad>=20 and edad<=59:
    print("adulto")
  
else:
	print("adulto mayor")