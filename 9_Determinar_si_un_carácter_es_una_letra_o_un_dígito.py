print("Determinar si un carácter es una letra o un dígito:")
print("======================================================\n")
caracter = input("Introduce un carácter: ")

if caracter.isalpha():
    print(f"El carácter '{caracter}' es una letra.")
    
elif caracter.isdigit():
    print(f"El carácter '{caracter}' es un dígito.")

else:
    print(f"El carácter '{caracter}' no es ni una letra ni un dígito.")