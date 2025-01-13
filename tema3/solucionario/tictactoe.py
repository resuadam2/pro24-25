# Proyecto Tic Tac Toe

"""
Realizaremos un juego de Tic Tac Toe en Python.

El juego se ejecutará en la terminal.

El juego tendrá dos jugadores, uno será 'X' y el otro 'O'.

El juego mostrará el tablero en la terminal.

El juego preguntará al jugador en qué posición desea colocar su ficha.

El juego verificará si hay un ganador. 

El juego verificará si hay un empate.

El juego preguntará si los jugadores desean jugar de nuevo.

Se debe separar la lógica del juego en funciones.
"""

# Importamos la librería random
import random

# Definimos la función que imprime el tablero

def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()

# Definimos la función que verifica si hay un ganador

def check_winner(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Definimos la función que verifica si hay un empate

def check_tie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# Definimos la función que comprueba si la posición elegida por el jugador es válida

def is_valid(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != " ":
        return False
    return True

# Definimos la función que comprueba que la entrada de datos es válida

def get_input(board):
    while True:
        try:
            row = int(input("Fila: "))
            col = int(input("Columna: "))
            if is_valid(board, row, col):
                return row, col
            else:
                print("Posición inválida!")
        except ValueError:
            print("Entrada inválida!")

# Definimos la función que ejecuta el turno de un jugador

def player_turn(board, player):
    print_board(board)
    print(f"Turno del jugador {player}")
    row, col = get_input(board)
    board[row][col] = player
    if check_winner(board, player):
        print_board(board)
        print(f"El jugador {player} ha ganado!")
        return True
    if check_tie(board):
        print_board(board)
        print("Empate!")
        return True
    return False

# Definimos la función que ejecuta el juego

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)
    while True:
        for player in players:
            if player_turn(board, player):
                return

    

# Definimos la función que pregunta si los jugadores desean jugar de nuevo

def play_again():
    while True:
        answer = input("¿Desean jugar de nuevo? (s/n): ")
        answer = answer.lower()
        if answer == "s":
            return True
        elif answer == "n":
            return False
        else:
            print("Respuesta inválida!")    

# Definimos la función principal

def main():
    try:
        while True:
            play_game()
            if not play_again():
                break
    except KeyboardInterrupt:
        print("\nGracias por jugar!")

# Ejecutamos la función principal

if __name__ == "__main__":
    main()