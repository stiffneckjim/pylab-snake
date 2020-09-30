""" A simple snake game, following Robert Heaton's 5th project for advanced beginners
See here for the project outline: https://robertheaton.com/2018/12/02/programming-project-5-snake/
Written with the good people of Women's Tech Hub Bristol's PyLAB.
"""


class Snake:
    "Our players avatar; a serpent."
    def __init__(self, start = (0,0), direction = 'UP'):
      self.vectors = {
        'UP': (0,1),
        'DOWN': (0,-1),
        'LEFT':(-1,0),
        'RIGHT':(1,0)
      }
      self.location = [start]
      self.velocity = self.vectors[direction]

    def move(self, grow=False, direction=''):
      # Only change direction if one is provided
      if direction in self.vectors:
        self.velocity = self.vectors[direction]

      shift_x, shift_y = self.velocity
      loc_x, loc_y = self.location[0]
      self.location.insert(0, (loc_x+shift_x, loc_y+shift_y))
      if grow==False:
        self.location.pop()


class Apple:
    "The prize our player seeks; one of your five-a-day."


class Game:
    "Play to win; the master class for this little programme."

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake((round(height/2), round(width/2)), 'UP')

    def render(self):
      print("Game height: {}".format(self.height))
      print("Game width:  {}".format(self.width))

      border_text = '+' + '-'*self.width + '+'

      print('   ' + border_text)
      s_loc = self.snake.location
      for row in range(self.height-1, 0, -1):
        row_text = ''
        for col in range(self.width):
          if (col,row) in s_loc:
            row_text = row_text + '*'
          else:
            row_text = row_text + ' '

        print(f"{row:2d} |{row_text}|")
      print('   ' + border_text)

game = Game(10, 10)
snake = game.snake
game.render()
snake.move(grow=True)
game.render()
