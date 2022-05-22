from turtle import Turtle, Screen, position
from random import randint

race_condition = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet_colour = my_screen.textinput(
    title="Make your bet.", prompt="Which turtle will win the race? Your choices are Red,Orange,Yellow,Green,Blue,Purple. Enter the colour:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

for turtle_index in range(0, 6):
    new_timmy = Turtle(shape="turtle")
    new_timmy.color(colors[turtle_index])
    new_timmy.penup()
    new_timmy.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_timmy)

if user_bet_colour:
    race_condition = True

while race_condition:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_condition = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet_colour:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner.")

        distance = randint(0, 10)
        turtle.forward(distance)

my_screen.exitonclick()
