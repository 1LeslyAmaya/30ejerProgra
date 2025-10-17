n = int(input("Ingresa un numero para generar la secuencia de fibonacci: "))

a= 0
b= 1
contador = 0

while contador < n:
    print(a)
    c = a + b
    a = b
    b = c
    contador += 1
