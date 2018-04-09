#recursion
import turtle

t = turtle.Turtle()

def spiral(length):
    if length > 0:
        t.forward(length)
        t.left(120)
        spiral(length - 3)

spiral(100)
