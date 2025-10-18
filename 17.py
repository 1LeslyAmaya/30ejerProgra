limite = int (input("Ingrese la cantidad de datos: "))
i = 1
suma = 0
while i <= limite:
    numeros = int (input("Ingrese los numeros: "))
    suma += numeros
    i += 1
suma = suma / limite
print("El promedio es:", suma)
