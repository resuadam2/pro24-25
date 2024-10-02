# Laboratorio 2.4.1.9: Variables, un sencillo convertidor

kilometers = 12.25
miles = 7.38

miles_to_kilometers = 1.61
kilometers_to_miles = 1 / miles_to_kilometers
nautic_miles_to_kilometers = 1.852
kilometers_to_nautic_miles = 1 / nautic_miles_to_kilometers

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 3), "millas")
print(kilometers, "kilómetros son", round(kilometers_to_nautic_miles, 2), "millas náuticas")

