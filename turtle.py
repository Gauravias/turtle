import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move the turtle forward by 100 units
    my_turtle.left(90)     # Turn the turtle 90 degrees to the left

# Keep the window open until it is manually closed
turtle.done()
