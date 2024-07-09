print("Determinar si una persona es adolescente:")
print("========================================\n")
print("ingrese la edad de la persona: ")

edad = int(input())
if edad >=18:
	print("la persona es mayor de edad")
elif edad <18 and edad >=13:
	print("la persona es un adolecente")
else:
	print("la persona es un niño(a)")