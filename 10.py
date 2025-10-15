precio = float(input("Ingrese el precio: "))
porcentaje  = float(input("Ingrese el descuento: "))

descuento = precio * (porcentaje / 100)
final = precio - descuento 

print("El descuento es de:", descuento)
print("El precio final con descuento es:", final)