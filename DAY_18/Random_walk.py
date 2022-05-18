from turtle import Turtle, Screen
from random import choice, randint
import turtle

timmy = Turtle()
turtle.colormode(255)
direction = [0, 90, 180, 270]


def random_colour():
    """Generates the random colours and returns a tuple."""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    colour_generated = (red, green, blue)
    return colour_generated


# FOR RANDOM WALK
timmy.width(15)
timmy.speed("fastest")
for _ in range(200):
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(choice(direction))


screen = Screen()
screen.exitonclick()
