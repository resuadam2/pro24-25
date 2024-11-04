# Laboratorio 3.4.1.13: Lo básico de las listas - Los Beatles

"""
Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

a banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).


Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

Paso 1: Crea una lista vacía llamada beatles.
Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
"""

Beatles = []# paso 1
print("Paso 1:", Beatles)

Beatles.append("John Lennon")# paso 2
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3
for i in range(2):
    Beatles.append(input("Ingrese un miembro de la banda: "))
print("Paso 3:", Beatles)

# paso 4
# del Beatles[3]
# del Beatles[3]
# Beatles.pop()
# Beatles.pop()
del Beatles[3:]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))