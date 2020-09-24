""" A simple snake game, following Robert Heaton's 5th project for advanced beginners
See here for the project outline: https://robertheaton.com/2018/12/02/programming-project-5-snake/
Written with the good people of Women's Tech Hub Bristol's PyLAB.
"""


class Snake:
    "Our players avatar; a serpent."


class Apple:
    "The prize our player seeks; one of your five-a-day."


class Game:
    "Play to win; the master class for this little programme."

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def render(self):
        print("Game height: %d" % (self.height))
        print("Game height: %d" % (self.width))


game = Game(20, 30)
game.render()
