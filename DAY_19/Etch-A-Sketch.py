from turtle import Turtle, Screen

timmy = Turtle()


def forwards():
    'When w is hit, the turtle will move 10 paces forward.'
    timmy.fd(10)


def backwards():
    'When s is hit, the turtle will move 10 paces backwards.'
    timmy.backward(10)


def clockwise():
    'When d is hit, the turtle will turn 10 degree clockwise.'
    timmy.right(10)


def counter_clockwise():
    'When a is hit, the turtle will turn 10 degree counter-clockwise.'
    timmy.left(10)


def clear_drawing():
    'When c is hit, the screen will get cleared.'
    timmy.reset()


my_screen = Screen()
my_screen.listen()
my_screen.onkey(fun=forwards, key='w')
my_screen.onkey(fun=backwards, key='s')
my_screen.onkey(fun=clockwise, key='d')
my_screen.onkey(fun=counter_clockwise, key='a')
my_screen.onkey(fun=clear_drawing, key='c')


my_screen.exitonclick()
