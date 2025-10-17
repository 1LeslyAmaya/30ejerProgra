suma = 0

numero = int(input("Ingrese un número positivo: "))

while numero >= 0:
    suma += numero
    numero = int(input("Ingrese otro número positivo: "))

print("La suma total de los números positivos es:", suma)
