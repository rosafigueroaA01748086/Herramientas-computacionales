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

# Dibuja una linea despues de recibir una l
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Dibuja una cuadrado despues de recibir una s
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Dibuja un circulo despues de recibir una c
def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(20):
        circle(end.x - start.x)
        left(18) #Ángulo exterior 360/n n=20

    end_fill()

# Dibuja un rectangulo despues de recibir una r
def rectangle(start, end):
    """Draw rectangle from start to end."""
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

# Dibuja un triangulo despues de recibir una t
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

# Se encarga de recibir las coordenadas del del punto de inicio 
def tap(x, y):
    """Store starting point or draw shape."""
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

# Actualiza el estado para dibujar diferentes figuras
def store(key, value):
    """Store value in state at key."""
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
