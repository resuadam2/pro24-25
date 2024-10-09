a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: ")) 

if(a > 0 and b > 0) or (a < 0 and b < 0): # inversa (a < 0 or b < 0) and (a > 0 or b > 0) el producto es negativo
    print("El producto es positivo")
elif(a == 0 or b == 0):
    print("El producto es nulo")
else: # if(a > 0 and b < 0) or (a < 0 and b > 0): el producto es negativo
    print("El producto es negativo")

