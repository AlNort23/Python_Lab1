import turtle

"""PUT YOUR FUNCTIONS HERE"""


def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y - radius)  # Start at the bottom of the pumpkin
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    t.penup()
    t.goto(x, y + radius)  # Move to the top of the pumpkin
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.setheading(0)  # Reset heading
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 2.5)
    t.left(90)
    t.forward(radius // 2)
    t.end_fill()


def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()


def draw_mouth(t, x, y, width):
    """Draws a jagged mouth with wide, pointy teeth pointing downwards."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)  # Ensure the turtle starts facing right
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):  # Create a zigzag mouth with 5 teeth

        t.right(60)
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(60)
    t.end_fill()



# Create a turtle object
t = turtle.Turtle()
# Hide the turtle and set speed
t.speed(5)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()
# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("black")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
# Drawing a jack-o-lantern with individual function calls
draw_pumpkin(t, 0, 0, 200)  # Draw the pumpkin
draw_eye(t, -60, 80, 60)  # Left eye
draw_eye(t, 60, 80, 60)  # Right eye
draw_mouth(t, -70, -70, 140)  # Mouth

# Close the turtle graphics window when clicked
turtle.exitonclick()