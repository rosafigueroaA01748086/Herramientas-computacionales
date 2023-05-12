from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(2)) * 2
state = {'mark': None}
hide = [True] * 4
taps = []
disp = []

def square(x, y):
    """Función que dibuja un cuadro blanco con un contorno negro en la coordenada marcada. Requiere de input dos parámetros x y y."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Función que convierte las coordenadas en los tiles index. Requiere dos parametros uno de x y otro de y."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Función que convierte los tiles en coordenadas. Requiere solo de un parámetro."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Funcion encargada en actualizar los tiles marcadas y ocultos al tocar"""
    spot = index(x, y)
    mark = state['mark']
    taps.append(1)
    print('Taps:', len(taps))
    title(len(taps))
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        disp.append(1)
        print(len(disp))
        if len(disp) == 32:
            title('LO LOGRASTE')
    
def draw():
    """Función que dibuja los tiles y la imagen. No requiere ningún parámetro."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(4):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    
    write('Taps:', font=('Arial', 30, 'normal'))
    update()
    ontimer(draw, 100)


# Funcion que mezcla el memorama
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()