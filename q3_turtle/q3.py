import turtle
import math

def draw_koch_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3
        draw_koch_edge(t, length, depth-1)
        t.left(60)
        draw_koch_edge(t, length, depth-1)
        t.right(120)
        draw_koch_edge(t, length, depth-1)
        t.left(60)
        draw_koch_edge(t, length, depth-1)

def draw_polygon(a, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_koch_edge(t, length, depth)
        t.right(angle)

# User inputs
sides = int(input("Enter number of sides: "))
length = int(input("Enter side length: "))
depth = int(input("Enter recursion depth: "))

# Turtle setup
t = turtle.Turtle()
t.speed('fastest')
screen = turtle.Screen()
screen.bgcolor("white")

draw_polygon(t, sides, length, depth)

screen.mainloop()

