#Escribe un programa que solicite al usuario los años de experiencia y determine la
#categoría del trabajador: "Junior" (menos de 2 años), "Semi-Senior" (2-5 años), "Senior" (más de 5 años).
print("---------------------------------------------")
print("|-         categoría del trabajador        -|")
print("---------------------------------------------")
experiencia = float(input("Ingrese los años de experiencia del trabajador: "))

if experiencia < 2:
    categoria = "Junior"
elif experiencia <= 5:
    categoria = "Semi-Senior"
else:
    categoria = "Senior"

print("La categoría  es: ",categoria)
