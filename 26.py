n = int(input("Ingrese la cantidad de términos de la serie: "))

suma = 0
for i in range(1, n + 1):
    suma += i
    print(suma, end=", ")
