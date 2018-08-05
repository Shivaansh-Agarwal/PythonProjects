import turtle

def square_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    
    design = turtle.Turtle()
    design.shape("turtle")
    design.color("yellow")
    design.speed(10)

    degree=0
    while(degree<360):
        sq=1
        while(sq<=4):
            design.forward(100)
            design.right(90)
            sq=sq+1

        design.right(5)
        degree=degree+5

square_circle()
    


