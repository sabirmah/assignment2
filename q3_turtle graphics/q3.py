import turtle

# Recursive function to create indentation on a line segment
def recursive_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        # divide edge into 3 parts
        recursive_edge(t, length / 3, depth - 1)
        t.left(60)  # turn to create inward triangle
        recursive_edge(t, length / 3, depth - 1)
        t.right(120)
        recursive_edge(t, length / 3, depth - 1)
        t.left(60)
        recursive_edge(t, length / 3, depth - 1)

# Function to draw a regular polygon recursively
def recursive_polygon(t, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        recursive_edge(t, length, depth)
        t.right(angle)

# Setup screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Recursive Geometric Pattern")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # fastest speed

# Get user input
sides = int(input("Enter number of sides for the polygon (e.g., 3, 4, 5): "))
length = float(input("Enter the length of each side: "))
depth = int(input("Enter recursion depth (e.g., 1-4): "))

# Move turtle to starting position
t.penup()
t.goto(-length/2, length/2)
t.pendown()

# Draw the recursive polygon
recursive_polygon(t, sides, length, depth)

# Keep window open
wn.mainloop()
