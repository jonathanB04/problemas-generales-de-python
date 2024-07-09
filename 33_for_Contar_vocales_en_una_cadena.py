print("Pide al usuario que ingrese una cadena de texto y cuenta cuántas vocales hay en la cadena usando un ciclo for")
print("--------------------------------------------------------------------------------\n")

texto = input("ingrese un texto: ")
vocales = "aeiouAEIOU"
c = 0

for i in texto:
	if i in vocales:
		c = c + 1
print(f"el texto tiene {c} vocales")