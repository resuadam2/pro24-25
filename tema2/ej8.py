# Ejercicio 8

"""
Implementar un programa de registro y login de usuarios. En primer lugar se ejecutará el código de registro,
que solicitará un nombre de usuario y una contraseña. A continuación, se ejecutará el código de login, que solicitará
el nombre de usuario y la contraseña. Si el nombre de usuario y la contraseña coinciden con los introducidos en el
registro, se mostrará un mensaje de bienvenida. En caso contrario, se mostrará un mensaje de error.
Necesitaremos una función para el registro y otra para el login.
Y las llamadas a las funciones de registro y login se realizarán en el algoritmo principal.
"""

def registro():
    global usuario, contrasena
    usuario = input("Introduce un nombre de usuario: ")
    contrasena = input("Introduce una contraseña: ")
    print("Registro completado.")

def login():
    usuario_login = input("Introduce tu nombre de usuario: ")
    contrasena_login = input("Introduce tu contraseña: ")
    if usuario_login == usuario and contrasena_login == contrasena:
        print("Bienvenido.")
    else:
        print("Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    registro()
    login()