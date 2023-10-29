from player import Player
from alien import Alien
from bullet import Bullet
import random


class GameController:
    def __init__(self):
        self.player = Player()
        self.bullet = Bullet()
        self.aliens = [Alien() for _ in range(5)]

    def bullet_fire(self):
        if self.bullet.state == "ready":
            self.bullet.state = "fire"
            x = self.player.xcor()
            y = self.player.ycor() + 10
            self.bullet.goto(x, y)
            self.bullet.showturtle()

    def check_collisions(self):
        for alien in self.aliens:
            if self.bullet.distance(alien) < 20:
                self.bullet.hideturtle()
                self.bullet.state = "ready"
                alien.goto(random.randint(-380, 380), random.randint(100, 250))

        for alien in self.aliens:
            if self.player.distance(alien) < 20:
                self.player.hideturtle()
                for a in self.aliens:
                    a.hideturtle()
                print("Game Over")
