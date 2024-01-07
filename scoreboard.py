from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('red')
        self.penup()
        self.hideturtle()
        self.goto(-330, -280)
        self.score = 0
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))
