from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    current_heading = tim.heading()
    tim.setheading(current_heading + 10)

def turn_right():
    current_heading = tim.heading()
    tim.setheading(current_heading - 10)

def clear_drawing():
    tim.reset()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()