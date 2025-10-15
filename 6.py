numero = int(input("Ingrese un número: "))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print("El número no es primo")
            break
    else:
        print("El número es primo")
else:
    print("El número no es primo")