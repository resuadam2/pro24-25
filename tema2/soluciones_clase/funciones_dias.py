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