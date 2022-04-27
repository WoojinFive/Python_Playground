from turtle import Turtle, Screen, shape
from random import randint, choice

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.speed("fastest")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)

    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()
