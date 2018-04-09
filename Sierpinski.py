import turtle

tri = turtle.Turtle()

tri.penup()
tri.setx(0)
tri.sety(200)
tri.pendown()
tri.shape("arrow")
tri.color("white")
tri.speed(2)

def sierpinski(length, depth):
    if depth == 0: #base case
        for i in range(3):
 
            tri.forward(length)
            tri.left(120)
            
 
    else:
        sierpinski(length/2, depth-1)#iteration
        tri.forward(length/2)
        sierpinski(length/2,depth-1)#iteration
        tri.backward(length/2)
        tri.left(60)
        tri.forward(length/2)
        tri.right(60)
        sierpinski(length/2,depth-1)#iteration
        tri.left(60)
        tri.backward(length/2)
        tri.right(60)
    
def create_screen():
    window = turtle.Screen()
    window.bgcolor("black")
    
 #   draw_square()
 #   draw_circle()
    sierpinski(100,0)
 
create_screen()
