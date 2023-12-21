from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.screen.register_shape("ship.gif")
        self.shape("ship.gif")
        self.penup()
        self.goto(0, -250)
        self.speed = 15

    def move_left(self):
        x = self.xcor()
        x -= self.speed
        if x < -380:
            x = -380
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += self.speed
        if x > 380:
            x = 380
        self.setx(x)
