import math

sumatorio = 0
sumatorio_cuadrados = 0

n_vueltas = int(input("Introduzca el número de veces que va a introducir números: "))

if n_vueltas <= 0:
    print("El número de veces debe ser mayor que 0")
else:
    for i in range(n_vueltas):
        num = float(input("Introduzca un número: "))
        sumatorio += num
        sumatorio_cuadrados += num ** 2
    else:
        media = sumatorio / n_vueltas
        varianza = (sumatorio_cuadrados - (sumatorio ** 2) / n_vueltas) / n_vueltas
        desviacion_tipica = math.sqrt(varianza) # desviacion_tipica = varianza ** 0.5
        print("La media es:", media)
        print("La varianza es:", varianza)
        print("La desviación típica es:", desviacion_tipica)
