# Funciones isdigit(), isalpha(), isalnum()

# Las funciones isdigit(), isalpha() e isalnum() se utilizan para comprobar si una cadena contiene solo dígitos, letras o caracteres alfanuméricos.

# Ejemplo

x = "123"
if x.isdigit():
    print("La cadena x contiene solo dígitos.")
else:
    print("La cadena x no contiene solo dígitos.")

# En este ejemplo, se comprueba si la cadena x contiene solo dígitos utilizando la función isdigit().
# La función isdigit() devuelve True si la cadena contiene solo dígitos y False en caso contrario.

# Ejemplo

x = "abc"
if x.isalpha():
    print("La cadena x contiene solo letras.")
else:
    print("La cadena x no contiene solo letras.")

# En este ejemplo, se comprueba si la cadena x contiene solo letras utilizando la función isalpha().
# La función isalpha() devuelve True si la cadena contiene solo letras y False en caso contrario.

# Ejemplo

x = "abc123"
if x.isalnum():
    print("La cadena x contiene solo caracteres alfanuméricos.")
else:
    print("La cadena x no contiene solo caracteres alfanuméricos.")

# En este ejemplo, se comprueba si la cadena x contiene solo caracteres alfanuméricos utilizando la función isalnum().
# La función isalnum() devuelve True si la cadena contiene solo caracteres alfanuméricos y False en caso contrario.

# Funciones islower(), isupper(), istitle()

# Las funciones islower(), isupper() e istitle() se utilizan para comprobar si una cadena contiene solo letras minúsculas, mayúsculas o en formato de título.

# Ejemplo

x = "abc"
if x.islower():
    print("La cadena x contiene solo letras minúsculas.")
else:
    print("La cadena x no contiene solo letras minúsculas.")

# En este ejemplo, se comprueba si la cadena x contiene solo letras minúsculas utilizando la función islower().

# Ejemplo

x = "ABC"
if x.isupper():
    print("La cadena x contiene solo letras mayúsculas.")
else:
    print("La cadena x no contiene solo letras mayúsculas.")

# En este ejemplo, se comprueba si la cadena x contiene solo letras mayúsculas utilizando la función isupper().
# La función isupper() devuelve True si la cadena contiene solo letras mayúsculas y False en caso contrario.

# Ejemplo

x = "Abc"
if x.istitle():
    print("La cadena x está en formato de título.")
else:
    print("La cadena x no está en formato de título.")

# En este ejemplo, se comprueba si la cadena x está en formato de título utilizando la función istitle().
# La función istitle() devuelve True si la cadena está en formato de título y False en caso contrario.

# Funciones lower(), upper(), title()

# Las funciones lower(), upper() y title() se utilizan para convertir una cadena a minúsculas, mayúsculas o en formato de título.

# Ejemplo

x = "Abc"
print(x.lower()) # "abc"

# En este ejemplo, se convierte la cadena x a minúsculas utilizando la función lower().
# La función lower() devuelve una copia de la cadena en minúsculas.

# Ejemplo

x = "abc"
print(x.upper()) # "ABC"

# En este ejemplo, se convierte la cadena x a mayúsculas utilizando la función upper().
# La función upper() devuelve una copia de la cadena en mayúsculas.

# Ejemplo

x = "abc"
print(x.title()) # "Abc"

# En este ejemplo, se convierte la cadena x a formato de título utilizando la función title().
