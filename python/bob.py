from turtle import*
import math



def draw_shape(num_sides):
    #name your Turtle
    bob=Turtle()


    #set up your screen and starting position

    setup(1000,800)
    x_pos = 0
    y_pos = 0
    bob.penup()
    setposition(x_pos, y_pos)


    bob.pendown()
    angle = 360/num_sides

    for side in range(num_sides):
        bob.forward(use)
        bob.right(angle)


user_input = input("What's your favorite number?")
user_input =int(user_input)
use = input("How big?")
use=int(use)
draw_shape(user_input)

#close window on click
exitonclick()
