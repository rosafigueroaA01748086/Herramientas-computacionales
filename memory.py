from random import *
from turtle import *

from freegames import path

car = path('car.gif')
#tiles = list(range(32)) * 2
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z', '*', '#', '$', '%', '&', '?',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z', '*', '#', '$', '%', '&', '?',]
state = {'mark': None}
hide = [True] * 64
taps = []
disp = []

# Funcion que dibuja un cuadro blanco con un contorno negro
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Funcion que convierte las coordenadas en los tiles index
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Funcion que convierte los tiles en coordenadas
def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Funcion encargada en actualizar los tiles marcadas y ocultos al tocar
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    taps.append(1)
    print('Taps:', len(taps))
    title(len(taps))
    if mark is None or mark == spot or letters[mark] != letters[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        disp.append(1)
        print(len(disp))
        if len(disp) == 32:
            title('LO LOGRASTE')


# Funcion que dibuja los tiles y la imagen
def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 27, y)
        color('black')
        write(letters[mark], align="center", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(letters)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
