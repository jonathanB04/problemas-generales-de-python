# lEscribe un programa que solicite un nombre al usuario y determine si el nombre es
#corto (menos de 5 letras), mediano (5-8 letras) o largo (más de 8 letras).
nombre = input("Ingrese un nombre: ")
longitud = len(nombre)
if longitud < 5:
    clasificacion = "Corto"
elif  5 <= longitud <= 8:
    clasificacion = "Mediano"
else:
    clasificacion = "Largo"

print(f"El nombre es  {clasificacion},")
