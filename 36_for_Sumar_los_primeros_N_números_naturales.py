print("Pide al usuario un número entero positivo NNN y suma los primeros NNN números naturales usando un ciclo for.")
print("------------------------------------------------------------------------------------\n")

print("ingresa el valor (n)")
a = int(input())
b = 0
for i in range(1,a+1):
	print(i)
	b = b+1
print("la suma es:",b)