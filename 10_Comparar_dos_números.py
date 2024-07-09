print("Escribe un programa que solicite al usuario dos números y determine cuál es mayor o si son iguales.")
print("===================================================================================\n")
a = int(input("ingrese un numero: "))
b = int(input("ingrese un segundo numero: "))

if a == b:
	print("ambos son iguales")
elif a > b:
	print(f'el numero mayor es {a}')
	print(f'el numero menor es {b}')
elif a < b:
	print(f'el numero mayor es {b}')
	print(f'el numero menor es {a}')