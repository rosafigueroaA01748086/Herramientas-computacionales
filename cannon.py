from random import randrange
from turtle import *
from freegames import vector

ball = vector(-400, -400)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Función que se encarga de responde al tap del usuario. No requiere ningun valor de entrada."
    if not inside(ball):
        # Comprobar si la pelota está fuera de la pantalla
        ball.x = -199
        ball.y = -199
        speed.x = (x + 300) / 25
        speed.y = (y + 300) / 25

def inside(xy):
    "Función que se encarga de regresar el valor True si xy esta dentro de la pantalla. Requiere un valor de entrada xy."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Función que se encarga de dibujar la pelota y los targets. No requiere ningun valor de entrada. "
    clear()

    # Se dibuja el objeto
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # Se dibuja la pelota
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    # Se actualiza la pantalla
    update()

def move():
    "Función que se encarga del movimiento de la pelota y de los targets. NO requiere ningun valor de entrada. "

    # Se generan los objetos aleatoria
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Movimiento de los objetos que ya se encuentran dentro de la pantalla
    for target in targets:
        target.x -= 2.5

    # Movimiento de la pelota
    if inside(ball):
        speed.y -= 0.5
        ball.move(speed)

    # Colisión entre la pelota y los objetos
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        # Si la distancia entre el objeto y la pelota es mayor que 13, 
        # no se ocurre la colisión y el objeto se agrega de nuevo a la lista
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Reaparecen los objetos que se salieron de la pantalla
    for target in targets:
        if not inside(target):
            target.x = 200

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()