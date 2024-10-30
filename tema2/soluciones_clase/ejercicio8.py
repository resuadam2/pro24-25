def registro():
    global username, password
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    print("Usuario registrado con éxito")

def login():
    username_input = input("Ingrese su nombre de usuario: ")
    password_input = input("Ingrese su contraseña: ")
    if username_input == username and password_input == password:
        print("Bienvenido")
    else:
        print("Usuario o contraseña incorrectos")

registro()
login()

def registro_v2():
    global username, password
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    repite_password = input("Repita su contraseña: ")
    while password != repite_password:
        print("Las contraseñas no coinciden")
        password = input("Ingrese su contraseña: ")
        repite_password = input("Repita su contraseña: ")
    print("Usuario registrado con éxito")

def login_v2():
    username_input = input("Ingrese su nombre de usuario: ")
    password_input = input("Ingrese su contraseña: ")
    while username_input != username or password_input != password:
        print("Usuario o contraseña incorrectos")
        username_input = input("Ingrese su nombre de usuario: ")
        password_input = input("Ingrese su contraseña: ")
    print("Bienvenido")

registro_v2()
login_v2()
