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

def square(x, y):
    """Funcion que dibuja un cuadro blanco con un contorno negro en el punto indicado. Requiere dos parámetros uno de x y otro de y."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    # dibuja los lados del cuadro
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """ Funcion que convierte las coordenadas en los tiles index. Requiere dos parámetros uno de x y otro de y."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """ Funcion que convierte los tiles en coordenadas. Requiere un parámetro."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """ Funcion encargada en actualizar los tiles marcados y ocultarlos en respuesta al tap realizado por el usuario. Requiere dos parámetros uno de x y y que marca la tarjeta selecionada."""
    spot = index(x, y)

    # Se actualiza la marca y los tiles ocultos
    mark = state['mark']
    taps.append(1)
    print('Taps:', len(taps))
    title(len(taps))
    # Si las en las posiciones correspondientes no son iguales,
    if mark is None or mark == spot or letters[mark] != letters[spot]:
        #     
        state['mark'] = spot
    else:
        # si son iguales se revelan los tiles ocultos
        hide[spot] = False
        hide[mark] = False
        # la marca actual se restablece como 'None'
        state['mark'] = None
        # se añade 1 al final de la lista disp
        disp.append(1)
        # se imprime la longitud de la lista disp para ver el progreso del juego
        print(len(disp))
        # si la longitud de disp es igual a 32, se muestra el mensaje en la ventana
        if len(disp) == 32:
            title('LO LOGRASTE')


def draw():
    """Funcion que dibuja los tiles y la imagen. No requiere de ningun parámetro de entrada. """
    clear()
    goto(0, 0)
    # se dibuja la imagen del coche
    shape(car)
    stamp()

    # se dibujan los tiles ocultos
    for count in range(64):
        # si el tile está oculto
        if hide[count]:
            # obtiene las coordenadas del tile oculto
            x, y = xy(count)
            # y se dibuja el cuadro
            square(x, y)

    mark = state['mark']

    # comprueba si hay una marca seleccionada y si el tile correspondiente está oculto
    if mark is not None and hide[mark]:
        # se obtiene las coordenadas (x,y) del tile seleccionado
        x, y = xy(mark)
        up()
        # contenido dentro del cuadro, en este caso son las letras del abecedario
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
