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
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  assert test_snake.location[0] == (10,12)
  assert test_snake.speed == 1
  assert test_snake.velocity == (0,1)

def test_snake_directions():
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  test_snake.set_velocity(0,'UP')
  assert test_snake.velocity == (0,1)
  test_snake.set_velocity(0,'DOWN')
  assert test_snake.velocity == (0,-1)
  test_snake.set_velocity(0,'LEFT')
  assert test_snake.velocity == (-1,0)
  test_snake.set_velocity(0,'RIGHT')
  assert test_snake.velocity == (1,0)

@pytest.mark.parametrize("speed",[1,2])
def test_snake_velocity(speed):
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  test_snake.set_velocity(speed,'UP')
  assert test_snake.velocity == (0,speed)
  test_snake.set_velocity(speed,'DOWN')
  assert test_snake.velocity == (0,-speed)
  test_snake.set_velocity(speed,'LEFT')
  assert test_snake.velocity == (-speed,0)
  test_snake.set_velocity(speed,'RIGHT')
  assert test_snake.velocity == (speed,0)

def test_snake_move():
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  test_snake.set_velocity(1,'UP')
  test_snake.move()
  assert test_snake.location[0] == (10,13)
  test_snake.set_velocity(2,'DOWN')
  test_snake.move()
  assert test_snake.location[0] == (10,11)
  test_snake.set_velocity(1,'LEFT')
  test_snake.move()
  assert test_snake.location[0] == (9,11)
  test_snake.set_velocity(2,'RIGHT')
  test_snake.move()
  assert test_snake.location[0] == (11,11)
  assert len(test_snake.location) == 1

def test_snake_grow():
  test_game = main.Game(20,24)
  test_snake = test_game.snake
  test_snake.set_velocity(1,'UP')
  test_snake.move(grow=True)
  assert test_snake.location[0] == (10,13)
  assert test_snake.location[1] == (10,12)
  assert len(test_snake.location) == 2
  test_snake.set_velocity(1,'LEFT')
  test_snake.move(grow=True)
  assert test_snake.location[0] == (9,13)
  assert test_snake.location[1] == (10,13)
  assert test_snake.location[2] == (10,12)
  assert len(test_snake.location) == 3
  test_snake.set_velocity(1,'DOWN')
  test_snake.move(grow=True)
  assert test_snake.location[0] == (9,12)
  assert test_snake.location[1] == (9,13)
  assert test_snake.location[2] == (10,13)
  assert test_snake.location[3] == (10,12)
  assert len(test_snake.location) == 4
#  test_snake.set_velocity(1,'RIGHT')
#  test_snake.move(grow=True)
#  assert test_snake.location[0] == (10,12)
#  assert len(test_snake.location) == 1
