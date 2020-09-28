import pytest
import main

@pytest.mark.parametrize("height, width",[(10,10),(8,12)])
def test_game_board(height, width):
  test_game = main.Game(height, width)
  assert test_game.height == height
  assert test_game.width == width
  assert len(test_game.board) == height
  assert len(test_game.board[0]) == width

def test_snake():
  test_snake = main.Snake((10,12))
  assert test_snake.location[0] == (10,12)

def test_snake_move():
  test_snake = main.Snake((10,12))
  test_snake.move('UP', 1)
  assert test_snake.location[0] == (10,13)
  test_snake.move('DOWN', 2)
  assert test_snake.location[0] == (10,11)
  test_snake.move('LEFT', 1)
  assert test_snake.location[0] == (9,11)
  test_snake.move('RIGHT', 2)
  assert test_snake.location[0] == (11,11)
  assert len(test_snake.location) == 1
