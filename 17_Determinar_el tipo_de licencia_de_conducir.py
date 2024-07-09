# un programa que solicite la edad del usuario y determine el tipo de licencia de
#conducir que puede obtener: "Licencia de menor" (16-17 años), "Licencia de adulto"
#(18-65 años) y "Licencia de adulto mayor" (más de 65 años).
print("---------------------------------------------")
print("|-           licencias                      -|")
print("---------------------------------------------")
edad = int(input("Ingrese su edad: "))

if 16 <= edad <= 17:
    licencia = " de menor"
elif 18 <= edad <= 65:
    licencia = "de adulto"
else:
    licencia = "de adulto mayor"

print("puede tener la licencia :",licencia)
