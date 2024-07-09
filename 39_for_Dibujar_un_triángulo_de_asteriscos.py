n = int(input("ingrese un numero entero: "))

for i in range(1,n,+1):
	print('*' * i)
	if n<=75:
		continue
	else:
		print("se rebaso el limite")
		break