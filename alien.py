from turtle import Turtle
import random


class Alien(Turtle):

    def __init__(self, row, column):
        super().__init__()
        self.speed(0)
        self.screen.register_shape("alien.gif")
        self.shape("alien.gif")
        self.penup()
        x = -350 + column * 50
        y = 250 - row * 50
        self.goto(x, y)
        self.movement_x = 0.1
        self.movement_y = 15
        self.column = column

    def move(self):
        x = self.xcor()
        x += self.movement_x
        self.setx(x)

        if x > 380 or x < -380:
            self.movement_x *= -1

            y = self.ycor()
            y -= self.movement_y
            self.sety(y)
