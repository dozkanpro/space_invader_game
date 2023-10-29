from turtle import Turtle
import random


class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(random.randint(-380, 380), random.randint(100, 250))
        self.speed = 1

    def move(self):
        x = self.xcor()
        x += self.speed
        self.setx(x)

        if x > 380 or x < -380:
            y = self.ycor()
            y -= 40
            self.sety(y)
            self.speed *= -1
