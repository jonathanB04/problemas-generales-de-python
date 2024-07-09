print("pide al usuario un numero entero positivo y convierte ese numero a binario usando un ciclo while")
print("---------------------------------------------------------------------------------\n")

numero_decimal = int(input("ingrese un numero entero positivo: "))
while numero_decimal <=0:
	print("este numero es negativo debes ingresar un numero entero positivo.")
	numero_decimal = int(input("otra ves"))
	
numero_binario = ""
while numero_decimal>0:
	residuo = numero_decimal % 2
	numero_binario = str(residuo) + numero_binario
	numero_decimal //= 2
print(f"el numero en binario es: {numero_binario}")