#Escribe un programa que solicite un número al usuario y determine si es un número
#primo.  
print("---------------------------------------------")
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero positivo: "))

if es_primo(numero):
    print(numero,"es un número primo")
else:
    print(numero, "no es un número primo")
