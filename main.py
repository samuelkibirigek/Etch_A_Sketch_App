from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(20)


def move_back():
    timmy.back(20)


# Here I provide two possible approaches to turning.


def turn_left():
    turn_more = timmy.heading() + 10
    timmy.setheading(turn_more)


def turn_right():
    timmy.circle(50, 20)


def reset_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()
