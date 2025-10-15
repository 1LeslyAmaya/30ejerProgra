calificacion = float(input("Ingrese la calificación: "))

if calificacion >= 90 and calificacion <= 100:
    print("Su nota es A")
elif calificacion >= 80 and calificacion <= 89:
    print("Su nota es B")
elif calificacion >= 70 and calificacion <= 79:
    print("Su nota es C")
elif calificacion >= 60 and calificacion <= 69:
    print("Su nota es D")
elif calificacion >= 0 and calificacion <= 59:
    print("Su nota es F")
else:
    print("Calificación fuera de rango (debe estar entre 0 y 100)")