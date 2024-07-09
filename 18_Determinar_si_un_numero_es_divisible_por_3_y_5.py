#Escribe un programa que solicite un número al usuario y determine si es divisible por 3,
#por 5, por ambos o por ninguno.
print("---------------------------------------------")
print("|-          Número Entero                  -|")
print("---------------------------------------------")
numero = int(input("Ingrese un número entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(numero, "es divisible por 3 y 5.")
elif numero % 3 == 0:
    print(numero, "es divisible por 3 pero no por 5.")
elif numero % 5 == 0:
    print(numero, "es divisible por 5 pero no por 3.")
else:
    print(numero, "no es divisible por 3 ni por 5.")
