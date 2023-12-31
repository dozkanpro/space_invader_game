import turtle
from game_controller import GameController

game = GameController()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.tracer(0)

# Keyboard bindings
screen.listen()
screen.onkey(game.player.move_left, "Left")
screen.onkey(game.player.move_right, "Right")
screen.onkey(game.bullet_fire, "space")

# Main game loop
while True:
    screen.update()
    game.bullet.move(game.player)

    for alien in game.aliens:
        alien.move()

    if game.check_collisions():
        screen.write('Game Over', align='center', font=('Courier', 20, 'normal'))

# Close the window
screen.exitonclick()
