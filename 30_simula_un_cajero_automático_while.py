print("escribe un programa que simule un cajero automatico")
print("-----------------------------------------------------------------------------------\n")

PIN = 3473
intento = 0
bloqueo = 3

while intento<bloqueo:
	numero = int(input("escribe el PIN: "))
	if numero == PIN:
		print("pin valido")
		print("bienvenido, Andy Rodriguez")
		break
	elif numero!=PIN:
		intento+=1
		print(f"PIN incorrecto")
	if intento == bloqueo:
		print("la targeta a sido bloqueda")