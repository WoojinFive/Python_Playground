from turtle import Turtle, Screen, shape
from random import randint, choice

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(5)
timmy_the_turtle.speed("fastest")

directions = [0, 90, 180, 270]

def draw_line(length):
    timmy_the_turtle.forward(length)

def change_color():
    timmy_the_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))

for _ in range(200):
    change_color()
    draw_line(20)
    timmy_the_turtle.setheading(choice(directions))

screen.exitonclick()
