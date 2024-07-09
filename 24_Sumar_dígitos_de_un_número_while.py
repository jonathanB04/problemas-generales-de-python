print("Pide al usuario que ingrese números enteros positivos uno a uno y suma estos números hasta que la suma alcance un límite (por ejemplo, 100).Usa un ciclo while.")
print("---------------------------------------------------------------------------------\n")

num = 0 #numeros a contar
suma = 0 #suma total
lim = 100
while num >= 0:
    print(num)
    num = num + float(input("ingresa numero a sumar: "))
    suma = suma + num
    if num >= lim:
        break
    elif num < lim:
        continue
    
print(f'{num}< limite')
print(f'la suma_total es de: {suma}')