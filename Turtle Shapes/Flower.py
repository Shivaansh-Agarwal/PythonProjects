# Flower using Triangle

import turtle

def draw_rhombus(turtle):
    i=1
    while(i<=4):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
        i=i+1
    
def flower(turtle, size, angle):
    degree=0
    while(degree < 360):
        draw_rhombus(rabbit)
        turtle.right(angle)
        degree=degree+angle
    turtle.right(90)
    turtle.forward(250)

window = turtle.Screen()
window.bgcolor("white")

rabbit = turtle.Turtle()
rabbit.shape("turtle")
rabbit.color("blue")
rabbit.speed(11)

flower(rabbit, 100, 5)

    
