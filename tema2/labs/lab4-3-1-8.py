# Laboratorio 4.3.1.8: Día del año: escribiendo y utilizando tus propias funciones

"""
Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
"""

def is_year_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True

def days_in_month(year, month):
	if month < 1 or month > 12:
		return None
	if month == 2:
		if is_year_leap(year):
			return 29
		else:
			return 28
	elif month in [4, 6, 9, 11]:
		return 30
	else:
		return 31

def day_of_year(year, month, day):
    if days_in_month(year, month) == None:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    return sum([days_in_month(year, i) for i in range(1, month)]) + day

def day_of_year_sin_compresion(year, month, day):
    if days_in_month(year, month) == None:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    suma = day
    for i in range(1, month):
        suma += days_in_month(year, i)
    return suma

print(day_of_year(1995, 12, 25))
print(day_of_year_sin_compresion(1995, 12, 25))