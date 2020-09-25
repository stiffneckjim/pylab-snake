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
        self.board = []


    def board_matrix(self):
      ''' A list of lists representing the game board
      '''
      for column in range(self.width):
        self.board.append(['.']*self.width)

    def render(self):
      print("Game height: {}".format(self.height))
      print("Game height: {}".format(self.width))
      self.board_matrix()

      border = '+' + '-'*self.width + '+'
      print('   ' + border)
      for column in range(self.width):
        print("{0:2d} |{1}|".format(column, ''.join(self.board[column])))
      print('   ' + border)

game = Game(20, 30)
game.render()
