from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


# Lista que nos ayuda a elegir entre estos colores para la comida y la snake
color = ['blue', 'yellow', 'pink', 'green', 'purple']
# Denominacion del color de la comida y la snake
foodC = random.choice(color)
snakeC = random.choice(color)

def change(x, y):
    "Función encargada del cambio de direccion. Solicita 2 parámetros x y y."
    aim.x = x
    aim.y = y

def inside(head):
    "Función que checa si la cabeza de la serpiente se encuentra dentro de los limites del mapa. Solicita un tipo punto donde se encuentre la cabeza de la serpiente."
    return -200 < head.x < 190 and -200 < head.y < 190

# Funcion encargada del movimiemto 
def move():
    "Función que se encarga del movimiento de la serpiente. No requiere ningun parámetro de entrada."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeC)

    square(food.x, food.y, 9, foodC)
    update()
    ontimer(move, 100)

# Funcion para que se mueva la comida
def move_food():
    """función que mueve de forma aleatoria un paso a la vez la comida, sin que esta salga del rango del mapa. No solicita ningun parámetro de entrada."""
    global food

    # Se generan direcciones random
    dx = randrange(-10, 11, 10)
    dy = randrange(-10, 11, 10)

    # Se calcula la nueva posición de la comida
    new_food = food + vector(dx, dy)

    # Ver si la nueva posición(new_food) está dentro de los límites
    if inside(new_food):
        food = new_food

    # Tiempo para el siguiente movimiento
    ontimer(move_food, 500)
    
def differentColor(foodC, snakeC):
    '''Función que se encarga de checar que el color si el color de la serpiente y de su comida es igual y cambiarlo. Requiere 2 parametros de entrada el color de la serpiente y el color de la comida.'''
    if (snakeC == foodC):
        snakeC = random.choice(color)


setup(420, 420, 370, 0)
hideturtle()
differentColor(foodC, snakeC)
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move_food()
move()
done()
