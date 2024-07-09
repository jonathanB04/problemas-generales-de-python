# Escribe un programa que solicite al usuario su peso y altura, calcule el Índice de Masa
#Corporal (IMC) y clasifique el resultado: "Bajo peso" (IMC < 18.5), "Normal" (18.5 ≤ IMC< 24.9), "Sobrepeso" (25 ≤ IMC < 29.9) y "Obesidad" (IMC ≥ 30).
print("---------------------------------------------")
print("|-         clasifica segun peso            -|")
print("---------------------------------------------")
altura = float(input("Ingrese su altura en metros: ")) 
peso =float(input("Ingrese su peso en kilogramos: ")) 

imc = peso / (altura ** 2)

if imc < 18.5:
    clasificacion = "Bajo peso" 
elif imc > 18.5 and imc <= 24.9: 
    clasificacion = "Normal"
elif imc > 25 and imc <= 29.9: 
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
print (f"Su IMC es: {imc:.2f}, lo que indica que tiene {clasificacion}.") 

