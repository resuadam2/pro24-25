# Ejercicio 11
"""
Diseñar un algoritmo que lea del teclado un número entero
correspondiente a una cantidad de minutos y nos diga cuántos
días, horas y minutos son. Por ejemplo, si introducimos 1000    
minutos, el algoritmo mostrará por pantalla que son 0 días, 16  
horas y 40 minutos.
"""
print("Introduzca la cantidad de minutos: ") # Pedimos la cantidad de minutos   
minutos = int(input()) # Leemos la cantidad de minutos  
dias = minutos // 1440 # Calculamos los días    
horas = (minutos % 1440) // 60 # Calculamos las horas   
minutos = (minutos % 1440) % 60 # Calculamos los minutos    
print("Son ", dias, " días, ", horas, " horas y ", minutos, " minutos") # Mostramos el resultado    
