from turtle import Turtle, Screen, resetscreen

timmy = Turtle()
screen = Screen()


def move_up():
    timmy.forward(10)


def move_down():
    timmy.back(10)


def move_left():
    timmy.left(10)


def move_right():
    timmy.right(10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(fun=move_up, key="Up")
screen.onkey(fun=move_down, key="Down")
screen.onkey(fun=move_left, key="Left")
screen.onkey(fun=move_right, key="Right")
screen.onkey(fun=clear_screen, key="space")
screen.exitonclick()
