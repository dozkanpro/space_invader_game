from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("triangle")
        self.color("yellow")
        self.penup()
        self.goto(0, -100)
        self.speed = 20
        self.state = "ready"

    def move(self):
        if self.state == "fire":
            y = self.ycor()
            y += self.speed
            self.sety(y)
