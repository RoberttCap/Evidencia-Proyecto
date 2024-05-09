"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Dibujar la cuadrícula del juego de tic-tac-toe."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibujar el símbolo X del jugador."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Dibujar el símbolo O del jugador."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Redondear un valor hacia abajo al tamaño de la cuadrícula (133)."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Dibujar X o O en la casilla seleccionada."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()