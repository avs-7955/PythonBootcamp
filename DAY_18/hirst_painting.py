import colorgram
import turtle as turtle_module
from random import choice


colors = colorgram.extract('D:\VIT\Self_Dev\CODING\Python\DAY_18\ori.jpg', 100)
new_rgb_colours = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colour = (r, g, b)
    new_rgb_colours.append(new_colour)


def line_colour():
    for _ in range(10):
        timmy.dot(20, choice(new_rgb_colours))
        timmy.forward(50)


timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.hideturtle()
turtle_module.colormode(255)
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

line_colour()

for _ in range(4):
    timmy.dot(20, choice(new_rgb_colours))
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)

    line_colour()

    timmy.dot(20, choice(new_rgb_colours))
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)

    line_colour()

timmy.dot(20, choice(new_rgb_colours))
timmy.left(90)
timmy.forward(50)
timmy.left(90)
line_colour()
timmy.dot(20, choice(new_rgb_colours))


my_screen = turtle_module.Screen()
my_screen.exitonclick()
