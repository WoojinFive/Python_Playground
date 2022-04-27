from turtle import Turtle, Screen, shape
from random import randint, choice

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

def draw_line():
    timmy_the_turtle.forward(20)

def change_direction():
    angles = [90, 180, 270, 360]
    timmy_the_turtle.right(choice(angles))

def change_color():
    timmy_the_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))


for _ in range(100):
    change_color()
    change_direction()
    draw_line()

screen.exitonclick()
