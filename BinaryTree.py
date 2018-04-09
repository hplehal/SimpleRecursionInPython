#binary tree
import turtle

t = turtle.Turtle()

def tree(branchLength):
    if(branchLength > 5):#base case
        t.forward(branchLength)
        t.right(20)
        tree(branchLength-10)
        t.left(40)
        tree(branchLength-10)
        t.right(20)
        t.backward(branchLength)

tree(35)
