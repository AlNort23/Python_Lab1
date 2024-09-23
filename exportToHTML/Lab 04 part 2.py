import turtle


class JackOLantern:
    def __init__(self, x=0, y=0, radius=200):
        self.x = x
        self.y = y
        self.radius = radius
        self.t = turtle.Turtle()
        self.t.speed(5)
        self.t.hideturtle()

    def draw_polygon(self, sides, length):
        angle = 360 / sides
        for _ in range(sides):
            self.t.forward(length)
            self.t.left(angle)

    def draw_pumpkin(self):
        self.t.penup()
        self.t.goto(self.x, self.y - self.radius)
        self.t.pendown()
        self.t.fillcolor("orange")
        self.t.begin_fill()
        self.t.circle(self.radius)
        self.t.end_fill()

        # Drawing the stem
        self.t.penup()
        self.t.goto(self.x, self.y + self.radius)
        self.t.pendown()
        self.t.fillcolor("green")
        self.t.begin_fill()
        self.t.setheading(0)
        self.t.forward(self.radius // 5)
        self.t.left(90)
        self.t.forward(self.radius // 2)
        self.t.left(90)
        self.t.forward(self.radius // 2.5)
        self.t.left(90)
        self.t.forward(self.radius // 2)
        self.t.end_fill()

    def draw_eye(self, x_offset, y_offset, size):
        self.t.penup()
        self.t.goto(self.x + x_offset, self.y + y_offset)
        self.t.pendown()
        self.t.fillcolor("yellow")
        self.t.begin_fill()
        self.draw_polygon(3, size)
        self.t.end_fill()

    def draw_mouth(self, width):
        self.t.penup()
        self.t.goto(self.x - width // 2, self.y - self.radius // 2)
        self.t.setheading(0)
        self.t.pendown()
        self.t.fillcolor("yellow")
        self.t.begin_fill()
        for _ in range(5):
            self.t.right(60)
            self.t.forward(width // 5)
            self.t.left(120)
            self.t.forward(width // 5)
            self.t.right(60)
        self.t.end_fill()

    def draw(self):
        self.draw_pumpkin()
        self.draw_eye(-self.radius // 3, self.radius // 2, self.radius // 3)
        self.draw_eye(self.radius // 3, self.radius // 2, self.radius // 3)
        self.draw_mouth(self.radius * 0.7)


def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)

    jack = JackOLantern()
    jack.draw()

    turtle.exitonclick()


if __name__ == "__main__":
    main()