from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.shapesize(0.2, 0.1)
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0, -100)
        self.movement = 20
        self.state = "ready"

    def move(self, player):
        if self.state == "fire":
            y = self.ycor()
            y += self.movement
            self.sety(y)

        if self.ycor() > 280:
            bullet_x = player.xcor()
            bullet_y = player.ycor()
            self.goto(bullet_x, bullet_y + 10)
            self.hideturtle()
            self.state = "ready"
