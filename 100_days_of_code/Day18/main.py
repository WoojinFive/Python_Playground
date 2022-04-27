from turtle import Turtle, Screen, shape
from random import randint

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

def draw_shape(num_sides):
    angle = 360 / num_sides
    
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


for shape_side_n in range(3, 11):
    timmy_the_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))
    draw_shape(shape_side_n)

screen.exitonclick()
