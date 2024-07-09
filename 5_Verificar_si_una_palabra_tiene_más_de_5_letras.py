print("Verificar si una palabra tiene más de 5 letras")

print("==============================================\n") 

p = input("Ingresa la palabra: ")
c = len(p.strip())
if c >= 5:
    print("Son 5 letras")
else:
    print("Menos de 5")