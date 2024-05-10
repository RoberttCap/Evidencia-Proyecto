"""Tic Tac Toe


"""

from turtle import (
    setup, hideturtle, tracer, update, onscreenclick,
    done, up, goto, circle, down, color,
)
from freegames import line

COLOR_X = "green"
COLOR_O = "yellow"

# Inicializar una matriz de 3x3 para registrar el estado de cada casilla
board = [[None, None, None], [None, None, None], [None, None, None]]


def grid():
    """Dibujar la cuadrícula del juego de tic-tac-toe."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibujar el símbolo X del jugador."""
    color(COLOR_X)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Dibujar el símbolo O del jugador."""
    color(COLOR_O)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Redondear un valor hacia abajo al tamaño de la cuadrícula (133)."""
    return ((value + 200) // 133) * 133 - 200


def tap(x, y):
    """Dibujar X o O en la casilla seleccionada."""
    x = floor(x)
    y = floor(y)
    player = state['player']

    # Obtener la fila y columna correspondiente en la matriz
    i = int((x + 200) // 133)
    j = int((y + 200) // 133)

    # Verificar si la casilla está vacía
    if board[i][j] is None:
        draw = players[player]
        draw(x, y)
        update()
        # Registrar el símbolo del jugador en la matriz
        board[i][j] = player
        state['player'] = not player  # Cambiar al siguiente jugador
    else:
        print("Casilla ocupada. Por favor, selecciona otra casilla.")


state = {'player': 0}
players = [drawx, drawo]

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
