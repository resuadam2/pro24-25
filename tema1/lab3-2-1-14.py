# Laboratorio 3.2.1.14: Fundamentos del bucle while

"""
Escucha esta historia: Un niño y su padre, un programador de computadoras, 
juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, 
es plana. La pirámide se apila de acuerdo con un principio simple: 
cada capa inferior contiene un bloque más que la capa superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los 
constructores, y generar la altura de la pirámide que se puede construir utilizando 
estos bloques.

Nota: La altura se mide por el número de capas completas: si los constructores 
no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, 
terminan su trabajo inmediatamente.

Prueba tu código con los datos que hemos proporcionado.
"""

blocks = int(input("Ingresa el número de bloques: "))

height = 0

while blocks >= height + 1: # height + 1 porque la primera capa tiene 1 bloque
    height += 1 # incrementa la altura
    blocks -= height # resta los bloques de la capa actual
    

print("La altura de la pirámide:", height)
print("Bloques restantes:", blocks)