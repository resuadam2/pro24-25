minutos = input("Introduce los minutos: ")

if minutos.isdigit():
    minutos = int(minutos)
    horas = minutos // 60
    minutos = minutos % 60
    dias = horas // 24
    horas = horas % 24
    print(f"{dias} días, {horas} horas y {minutos} minutos")
else:
    print("Por favor, introduce un número entero")
