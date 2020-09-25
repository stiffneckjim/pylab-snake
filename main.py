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
        self.board_matrix()

    def board_matrix(self):
      ''' A list of lists representing the game board
      '''
      self.board = []
      row = ['.']*self.width
      i = 0
      while i < self.height:
        self.board.append(row)
        i += 1

    def render(self):
      print("Game height: {}".format(self.height))
      print("Game width:  {}".format(self.width))

      border = '+' + '-'*self.width + '+'
      print('   ' + border)
      for row in range(self.height):
        print("{0:2d} |{1}|".format(row, ''.join(self.board[row])))
      print('   ' + border)

game = Game(20, 30)
game.render()

game = Game(20, 10)
game.render()

game = Game(10, 20)
game.render()
