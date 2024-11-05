from funciones_dias import days_in_month

def dia_nac_correcto(dia, mes, anio):
    if days_in_month(anio, mes) == None:
        return False
    if dia < 1 or dia > days_in_month(anio, mes):
        return False
    else:
        return True