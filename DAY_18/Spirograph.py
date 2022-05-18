from turtle import Turtle, Screen
from random import randint
import turtle
timmy = Turtle()

turtle.colormode(255)

timmy.speed("fastest")


def random_colour():
    """Generates the random colours and returns a tuple."""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    colour_generated = (red, green, blue)
    return colour_generated


timmy.color(random_colour())

for _ in range(int(360/7)):
    timmy.color(random_colour())
    timmy.circle(100)
    timmy.setheading(timmy.heading()+7)


screen = Screen()
screen.exitonclick()
