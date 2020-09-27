""" A simple snake game, following Robert Heaton's 5th project for advanced beginners
See here for the project outline: https://robertheaton.com/2018/12/02/programming-project-5-snake/
Written with the good people of Women's Tech Hub Bristol's PyLAB.
"""


class Snake:
    "Our players avatar; a serpent."
#    def __init__(self):
#      self.vector = 


class Apple:
    "The prize our player seeks; one of your five-a-day."


class Game:
    "Play to win; the master class for this little programme."

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.clear_board()

    def clear_board(self):
      ''' A list of lists representing the game board
      '''
      self.board = [[' ']*self.width for i in range(0, self.height)]

    def render(self):
      print("Game height: {}".format(self.height))
      print("Game width:  {}".format(self.width))

      border_text = '+' + '-'*self.width + '+'

      print('   ' + border_text)
      for row in range(self.height-1, 0, -1):
        row_text = ''.join(self.board[row])
        print(f"{row:2d} |{row_text}|")
      print('   ' + border_text)

game = Game(20, 30)
game.render()

game = Game(20, 10)
game.render()
