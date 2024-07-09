#Escribe un programa que solicite al usuario su salario bruto y calcule el salario neto
#después de aplicar un impuesto del 20% si el salario bruto es mayor a $2000.
print("---------------------------------------------")
print("|-           salario_neto                  -|")
print("---------------------------------------------")

salario_bruto = float(input("Ingrese su salario bruto: "))

# Calculamos el impuesto dependiendo del salario bruto
if salario_bruto > 2000:  
    impuesto = salario_bruto * 0.20  
else: 
    impuesto = 0  

salario_neto = salario_bruto - impuesto
print("Su salario neto es:", salario_neto)
