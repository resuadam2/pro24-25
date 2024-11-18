# Examen UD2 - Funciones en Python, listas en Python y recursividad

# Resuelve los siguientes ejercicios sin modificar ninguna de las lineas de código existentes.
# Nota: no se pueden modificar las líneas pero si se pueden añadir líneas de código entre las de inicio y final si se necesita más espacio.

# Ejericio 1 (2,5 puntos)

"""
Diseña una función que reciba el nombre de un planeta del Sistema Solar y devuelva el número de lunas que tiene.
La función debe devolver un número entero y debe aceptar el nombre del planeta en minúsculas, mayúsculas o combinando ambas.
Si el planeta es Plutón, la función debe devolver 5 y además debe imprimir un mensaje que diga "Plutón ya no es considerado un planeta :(". 
Si el planeta no existe, la función debe devolver None.
El número de lunas de los planetas del Sistema Solar son los siguientes:
- Mercurio: 0
- Venus: 0
- Tierra: 1
- Marte: 2
- Júpiter: 79
- Saturno: 82
- Urano: 27
- Neptuno: 14
- Plutón: 5

Una vez creada esta función, se debe crear otra que use la lista de planetas dada (planets)
 y devuelva una string con el nombre de cada planeta y el número de lunas que tiene.
 Si un planeta no lunas, se debe indicar que no tiene lunas de la siguiente manera: "Mercurio: 0 lunas".
 Si un planeta no existe, se debe indicar que no existe de la siguiente manera: "Alderaan: no existe en el Sistema Solar".        
 El formato de la string debe ser el siguiente:
 "Mercurio: 0 Lunas, Tierra: 1 Luna, Saturno: 82 Lunas, Urano: 27 Lunas, Plutón: 5 Lunas, Alderaan: no existe en el Sistema Solar".    

 Nota: para poner la primera letra de un String en mayúsculas, se puede usar el método capitalize().    
"""
planets = ["MERCURIO", "VENUS", "TIERRA", "ALDERAAN", "JUPITER", "MARTE", "SATURNO", "NEPTUNO", "PLUTON"]

def numLunas(planeta: str) -> int:
    planeta = planeta.lower()
    match planeta:
        case "mercurio":
            return 0
        case "venus":
            return 0
        case "tierra":
            return 1
        case "marte":
            return 2
        case "jupiter":
            return 79
        case "saturno":
            return 82
        case "urano":
            return 27
        case "neptuno":
            return 14
        case "pluton":
            print("Plutón ya no es considerado un planeta :(")
            return 5
        case _:
            return None
    
def numLunasPlanetas(planetas: list) -> str:
    resultado = ""
    for planeta in planetas:
        lunas = numLunas(planeta)
        if lunas == None:
            resultado += planeta.capitalize() + ": no existe en el Sistema Solar, "
        else:
            resultado += planeta.capitalize() + ": " + str(lunas) + " Lunas, "
    return resultado[:-2]


print(numLunas("Tierra"))
print(numLunas("Marte"))
print(numLunas("Pluton"))
print(numLunas("Alderaan"))
print(numLunasPlanetas(planets))

# Fin del ejercicio 1

print("-"*30)

# Ejericio 2 (2,5 puntos)

"""
Diseñar una función que reciba una altura y devuelva un árbol de navidad en forma de string.
El árbol de navidad debe tener la siguiente forma:

Para una altura de 6:
     *
    ***
   *****
  *******
 *********
***********
    ***

Para una altura de 3:
  *
 ***
*****
 ***

Para una altura de 5:
    *
   ***
  *****
 *******
*********
   ***

La función debe devolver un string con el árbol de navidad.
La función debe devolver None si la altura es menor que 3.

Notas a tener en cuenta:
- La base del árbol siempre tiene 3 asteriscos.
- La altura mínima del árbol es de 3.
- Se deben ir concatenando los saltos de línea al final de cada línea, pero no al final del string final.
"""

def arbolNavidad(altura: int) -> str:
    if altura < 3:
        return None
    resultado = ""
    for i in range(1, altura+1):
        resultado += " "*(altura-i) + "*"*(2*i-1) + "\n"
    resultado += " "*(altura-2) + "***"
    return resultado

print(arbolNavidad(6))
print(arbolNavidad(3))
print(arbolNavidad(5))
print(arbolNavidad(2))

# Fin del ejercicio 2

print("-"*30)

# Ejericio 3 (2,5 puntos)

"""
Diseña una función que reciba una nota numérica y devuelva la cualificación correspondiente.
Las notas son las siguientes:
- 0-4.9: Suspenso
- 5-6.9: Aprobado
- 7-8.9: Notable
- 9-9.9: Sobresaliente
- 10: Matrícula de Honor

La función debe devolver un string con la cualificación correspondiente.
Si la nota no está en el rango 0-10, la función debe devolver None.

Una vez creada esta función, se debe crear otra que reciba dos listas, una primera lista con 
los nombres de las materias y una segunda lista con las notas de esas materias.

La función debe devolver una lista con el nombre de las materias y la cualificación correspondiente.
Las notas de esta lista a devolver deben ser strings con la siguiente forma: "Matemáticas: Sobresaliente".  
Si una nota no está en el rango 0-10, se debe indicar que la nota es incorrecta de la siguiente manera: "Inglés: Nota incorrecta".
Si las listas no tienen la misma longitud, la función debe devolver una lista con un solo elemento que sea "Error: Las listas no tienen la misma longitud".
"""

def cualificacion(nota: float) -> str:
    if nota < 0 or nota > 10:
        return None
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    elif nota < 10:
        return "Sobresaliente"
    else:
        return "Matrícula de Honor"

def cualificacionMaterias(materias: list, notas: list) -> list:
    if len(materias) != len(notas):
        return ["Error: Las listas no tienen la misma longitud"]
    resultado = []
    for i in range(len(materias)):
        nota = cualificacion(notas[i])
        if nota == None:
            resultado.append(materias[i] + ": Nota incorrecta")
        else:
            resultado.append(materias[i] + ": " + nota)
    return resultado

materias = ["Matemáticas", "Física", "Química", "Inglés"]
notas = [9.5, 7.2, 11, 8.9]
notas2 = [9.5, 7.2, 8.9]
print(cualificacion(9.5))
print(cualificacion(7.2))
print(cualificacion(11))
print(cualificacion(8.9))
print(cualificacionMaterias(materias, notas))
print(cualificacionMaterias(materias, notas2))

# Fin del ejercicio 3

print("-"*30)

# Ejericio 4 (2,5 puntos)

"""
Elaborar dos funciones básicas para trabajar con listas de números enteros.
La primera debe sumar todos los elementos de la lista y devolver el resultado.
La segunda debe buscar un elemento de la lista pasado como parámetro junto con la propia lista 
y devolver si está o no el elemento en la lista.

Ambas funciones TIENE que ser recursivas.
"""

def sumaLista(lista: list) -> int:
    if len(lista) == 0:
        return 0
    return lista[0] + sumaLista(lista[1:])

def buscarElemento(lista: list, elemento: int) -> int:
    if not lista:
        return False
    if lista[0] == elemento:
        return True
    return buscarElemento(lista[1:], elemento)

lista = [1, 2, 3, 4, 5]
print(sumaLista(lista))
print(buscarElemento(lista, 3))
print(buscarElemento(lista, 6))

# Fin del ejercicio 5

print("-"*30)


