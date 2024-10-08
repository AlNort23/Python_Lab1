import turtle
import random


def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()


def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(50, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)


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
t.speed(0)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()
# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("dark blue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()


# Draw three jack-o-lanterns
draw_pumpkin(t, -150, -200, 100)  # Adjusted y-coordinate
draw_eye(t, -190, -160, 30)  # Left eye
draw_eye(t, -110, -160, 30)  # Right eye
draw_mouth(t, -190, -240, 80)  # Mouth

draw_pumpkin(t, 0, -220, 80)  # Adjusted y-coordinate
draw_eye(t, -20, -190, 25)
draw_eye(t, 20, -190, 25)
draw_mouth(t, -30, -240, 60)

draw_pumpkin(t, 150, -200, 100)  # Adjusted y-coordinate
draw_eye(t, 110, -160, 30)
draw_eye(t, 190, -160, 30)
draw_mouth(t, 110, -240, 80)


# Draw a starry sky
draw_sky(t, 30)


# Close the turtle graphics window when clicked
turtle.exitonclick()