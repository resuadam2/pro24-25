# Comprobar tipos de datos en python

# Ejemplo

# La funcion type() se utiliza para comprobar el tipo de datos de una variable.

# Ejemplo

x = 5
print(type(x)) # <class 'int'>

x = 5.0
print(type(x)) # <class 'float'>

x = "Hola, mundo!"
print(type(x)) # <class 'str'>

# Comprobar el tipo de datos de una variable

# En Python, se puede comprobar el tipo de datos de una variable utilizando la función type().
# La función type() devuelve el tipo de datos de una variable como un objeto de tipo type.

# Ejemplo
x = "5"
if type(x) == int:
    print("La variable x es de tipo entero.")
else:
    print("La variable x no es de tipo entero.")

# En este ejemplo, se comprueba si la variable x es de tipo entero utilizando la función type().

# Función isinstance()

# La función isinstance() se utiliza para comprobar si una variable es de un tipo de datos específico.

# Ejemplo

x = 5
if isinstance(x, int):
    print("La variable x es de tipo entero.")
else:
    print("La variable x no es de tipo entero.")

# En este ejemplo, se comprueba si la variable x es de tipo entero utilizando la función isinstance().

# La función isinstance() devuelve True si la variable es del tipo de datos especificado y False en caso contrario.

# Funciones str(), int(), float()

# Las funciones str(), int() y float() se utilizan para convertir una variable a un tipo de datos específico.

# Ejemplo

x = 5
print(type(x)) # <class 'int'>

x = str(x)
print(type(x)) # <class 'str'>

# En este ejemplo, se convierte la variable x de tipo entero a tipo cadena utilizando la función str().

# Ejemplo

x = "5"
print(type(x)) # <class 'str'>

x = int(x)
print(type(x)) # <class 'int'>

# En este ejemplo, se convierte la variable x de tipo cadena a tipo entero utilizando la función int().
# Si la cadena no se puede convertir a entero, se produce un error de tipo ValueError.

# Ejemplo

x = "5.0"
print(type(x)) # <class 'str'>

x = float(x)
print(type(x)) # <class 'float'>

# En este ejemplo, se convierte la variable x de tipo cadena a tipo flotante utilizando la función float().

