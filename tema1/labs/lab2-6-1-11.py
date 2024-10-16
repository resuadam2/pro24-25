# Laboratorio 2.6.1.11: Operadores y expresiones

"""
La tarea es preparar un código simple para evaluar o encontrar el tiempo final 
 de un periodo de tiempo dado, expresándolo en horas y minutos. 
Las horas van de 0 a 23 y los minutos de 0 a 59. 
El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, 
lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

Prueba el código cuidadosamente. 
Pista: utilizar el operador % puede ser clave para el éxito.
"""

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.

mins += dura # incrementa los minutos a la hora de inicio
hour += mins // 60 # incrementa las horas si los minutos son mayores a 60
mins %= 60 # ajusta los minutos a 0-59, es lo mismo que mins = mins % 60
hour %= 24 # ajusta las horas a 0-23, es lo mismo que hour = hour % 24

print(hour, ":", mins, sep='')

# Posible ampliación: Controlar que cuándo las horas o minutos son menores a 10,
# se añada un cero a la izquierda, por ejemplo, 02:07 en lugar de 2:7.