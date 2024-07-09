print("Determinar si un carácter es una vocal.")
print("======================================\n")
def validar(c):
	vocales = "aeiouAEIOU"
	if c in vocales:
		print(f"la letra {c} es vocal")
	else:
		print(f"la letra {c} no es vocal")
	

letra = input("Ingresa una letra: ")
validar (letra)