from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


for num_sides in range(4,9):
    length = 100
    angle = 360/num_sides

    timmy_the_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))

    for _ in range(num_sides):
        timmy_the_turtle.forward(length)
        timmy_the_turtle.right(angle)


screen.exitonclick()
