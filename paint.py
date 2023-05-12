""" Juego que se encarga de dibujar figuras o lineas dependiendo de lo que ingrese el usuario
Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Dibuja una linea despues de recibir un punto de inicio y un punto de final. Requiere dos parámetros el punto de inicio y final."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    """Dibuja una cuadrado de inicio a fin. Requiere dos parámetros un punto de inicio y final."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    """Dibuja un circulo de inicio a fin. Requiere dos parámetros el de inicio y final."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(20):
        forward(end.x - start.x)
        left(18) #Ángulo exterior 360/n n=20

    end_fill()

def rectangle(start, end):
    """Dibuja un rectangulo de inicio a fin. Requiere dos parámetros un punto de inicio otro de final."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        for i in range(1):
            forward((2*end.x) - (2*start.x))
            left(90)
        forward(end.x - start.x)
        left(90)

    end_fill()

def triangle(start, end):
    """Dibuja un triangulo completo. Requiere dos parámetros el punto de inicio o de fin. """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    """Se encarga de recibir las coordenadas del del punto de inicio y dibujar una figura o linea.Requiere dos parámetros una x y otra y. """
    # Actualización del estado
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        # Se obtiene la función de dibujo correspondiente almacenada en state['state']
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Actualiza el estado para dibujar diferentes figuras"""
    state[key] = value
    # Por ejemplo:
    # store('shape', square)

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
