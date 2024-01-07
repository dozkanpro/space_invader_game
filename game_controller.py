from player import Player
from alien import Alien
from bullet import Bullet
from scoreboard import ScoreBoard


class GameController:
    def __init__(self):
        self.player = Player()
        self.bullet = Bullet()
        self.aliens = [Alien(row, column) for row in range(5) for column in range(11)]
        self.scoreboard = ScoreBoard()

    def bullet_fire(self):
        if self.bullet.state == "ready":
            self.bullet.state = "fire"
            x = self.player.xcor()
            y = self.player.ycor() + 10
            self.bullet.goto(x, y)
            self.bullet.showturtle()

    def check_collisions(self):
        for alien in self.aliens:
            if self.bullet.distance(alien) < 10:
                self.bullet.hideturtle()
                self.bullet.goto(1000,1000)
                self.bullet.state = "ready"
                alien.goto(1000, 1000)
                self.scoreboard.update()

        for alien in self.aliens:
            if self.player.distance(alien) < 20:
                return True
