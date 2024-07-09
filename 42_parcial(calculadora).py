print("calculadora de productos")

precio = float(input("ingresa el precio del producto:"  ))
descuento = float(input("ingresa el porcentaje del descuento:"  ))
impuesto = float(input("ingresa el impuesto:"  ))

print("resultado✓")

precio = precio * (impuesto / 100)
descuento = precio  -  descuento
impuesto = precio * (impuesto * 2)
total = descuento + impuesto

print(total)