print("Pide al usuario que ingrese números enteros positivos uno a uno y suma estos números hasta que la suma alcance un límite (por ejemplo, 100).Usa un ciclo while.")
print("---------------------------------------------------------------------------------\n")

n = 0 #numeros a contar
s = 0 #suma total
lim = float(input("escribe el limite a contar: "))
while n >= 0:
    print(n)
    n = n + 1
    s = s + n
    if n >= lim:
        break
    elif n < lim:
        continue
    
print(f'{n}< limite establecido')
print(f'la suma_total es de: {s}')