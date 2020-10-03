import pytest
import main

@pytest.mark.parametrize("height, width",[(10,10),(8,12)])
def test_game_board(height, width):
  test_game = main.Game(height, width)
  assert test_game.height == height
  assert test_game.width == width

def test_snake():
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  assert test_snake.location[0] == (10,12)
  assert test_snake.velocity == (0,1)

def test_snake_move():
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  test_snake.move(grow=False, direction='UP')
  assert test_snake.velocity == (0,1)
  assert test_snake.location[0] == (10,13)
  test_snake.move(grow=False, direction='DOWN')
  assert test_snake.velocity == (0,-1)
  assert test_snake.location[0] == (10,12)
  test_snake.move(grow=False, direction='LEFT')
  assert test_snake.velocity == (-1,0)
  assert test_snake.location[0] == (9,12)
  test_snake.move(grow=False, direction='RIGHT')
  assert test_snake.velocity == (1,0)
  assert test_snake.location[0] == (10,12)
  assert len(test_snake.location) == 1

def test_snake_grow():
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  test_snake.move(grow=True, direction='UP')
  assert test_snake.velocity == (0,1)
  assert test_snake.location[0] == (10,13)
  assert test_snake.location[1] == (10,12)
  assert test_snake.render(10, 13) == '^'
  assert test_snake.render(10, 12) == 'O'
  test_snake.move(grow=True, direction='LEFT')
  assert test_snake.velocity == (-1,0)
  assert test_snake.location[0] == (9,13)
  assert test_snake.location[1] == (10,13)
  assert test_snake.location[2] == (10,12)
  assert test_snake.render(9, 13) == '<'
  assert test_snake.render(10, 13) == 'O'
  assert test_snake.render(10, 12) == 'O'
  test_snake.move(grow=True, direction='DOWN')
  assert test_snake.velocity == (0,-1)
  assert test_snake.location[0] == (9,12)
  assert test_snake.location[1] == (9,13)
  assert test_snake.location[2] == (10,13)
  assert test_snake.location[3] == (10,12)
  assert test_snake.render(9, 12) == 'v'
  assert test_snake.render(9, 13) == 'O'
  assert test_snake.render(10, 13) == 'O'
  assert test_snake.render(10, 12) == 'O'
  test_snake.move(grow=False, direction='DOWN')
  assert test_snake.velocity == (0,-1)
  assert test_snake.location[0] == (9,11)
  assert test_snake.location[1] == (9,12)
  assert test_snake.location[2] == (9,13)
  assert test_snake.location[3] == (10,13)
  assert test_snake.render(9, 11) == 'v'
  assert test_snake.render(9, 12) == 'O'
  assert test_snake.render(9, 13) == 'O'
  assert test_snake.render(10, 13) == 'O'
  assert test_snake.render(10, 12) is None
  test_snake.move(grow=True, direction='RIGHT')
  assert test_snake.velocity == (1,0)
  assert test_snake.location[0] == (10,11)
  assert test_snake.location[1] == (9,11)
  assert test_snake.location[2] == (9,12)
  assert test_snake.location[3] == (9,13)
  assert test_snake.location[4] == (10,13)
  assert test_snake.render(10, 11) == '>'
  assert test_snake.render(9, 11) == 'O'
  assert test_snake.render(9, 12) == 'O'
  assert test_snake.render(9, 13) == 'O'
  assert test_snake.render(10, 13) == 'O'
  assert test_snake.render(10, 12) is None
  assert len(test_snake.location) == 5
