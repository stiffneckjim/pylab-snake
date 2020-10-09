''' Pytest unit tests for game and snake, relying on the rendering of the snake as ASCII characters
'''
import pytest
import main

@pytest.mark.parametrize("height, width",[(10,10),(8,12)])
def test_game_board(height, width):
    "Test a new board is the expected height and width"
    test_game = main.Game(height, width)
    assert test_game.height == height
    assert test_game.width == width

@pytest.mark.parametrize("height, width, snake_x, snake_y",[
    (10, 10, 5, 5),
    (9,  12, 4, 6)
])
def test_snake_start(height, width, snake_x, snake_y):
    "Test a snake is in the correct starting location with correct starting parameters"
    t_game = main.Game(height, width)
    assert t_game.snake.location[0] == (snake_x, snake_y)
    assert t_game.snake.velocity == (0,1)
    del t_game

def test_snake_move():
    "Test a snake's location and velocity with each direction"
    t_snake = main.Snake(start=(10,12))
    t_snake.move(grow=False, direction='UP')
    assert t_snake.velocity == (0,1)
    assert t_snake.location[0] == (10,13)
    assert t_snake.render(10, 13) == '^'
    t_snake.move(grow=False, direction='DOWN')
    assert t_snake.velocity == (0,-1)
    assert t_snake.location[0] == (10,12)
    assert t_snake.render(10, 12) == 'v'
    t_snake.move(grow=False, direction='LEFT')
    assert t_snake.velocity == (-1,0)
    assert t_snake.location[0] == (9,12)
    assert t_snake.render(9, 12) == '<'
    t_snake.move(grow=False, direction='RIGHT')
    assert t_snake.velocity == (1,0)
    assert t_snake.location[0] == (10,12)
    assert len(t_snake.location) == 1
    assert t_snake.render(10, 12) == '>'

def test_snake_grow():
    "Test a snake's body location as it moves and grows"
    t_snake = main.Snake((10,12))
    t_snake.move(grow=True, direction='UP')
    assert t_snake.velocity == (0,1)
    assert t_snake.location[0] == (10,13)
    assert t_snake.location[1] == (10,12)
    assert t_snake.render(10, 13) == '^'
    assert t_snake.render(10, 12) == 'O'
    t_snake.move(grow=True, direction='LEFT')
    assert t_snake.velocity == (-1,0)
    assert t_snake.location[0] == (9,13)
    assert t_snake.location[1] == (10,13)
    assert t_snake.location[2] == (10,12)
    assert t_snake.render(9, 13) == '<'
    assert t_snake.render(10, 13) == 'O'
    assert t_snake.render(10, 12) == 'O'
    t_snake.move(grow=True, direction='DOWN')
    assert t_snake.velocity == (0,-1)
    assert t_snake.location[0] == (9,12)
    assert t_snake.location[1] == (9,13)
    assert t_snake.location[2] == (10,13)
    assert t_snake.location[3] == (10,12)
    assert t_snake.render(9, 12) == 'v'
    assert t_snake.render(9, 13) == 'O'
    assert t_snake.render(10, 13) == 'O'
    assert t_snake.render(10, 12) == 'O'
    t_snake.move(grow=False, direction='DOWN')
    assert t_snake.velocity == (0,-1)
    assert t_snake.location[0] == (9,11)
    assert t_snake.location[1] == (9,12)
    assert t_snake.location[2] == (9,13)
    assert t_snake.location[3] == (10,13)
    assert t_snake.render(9, 11) == 'v'
    assert t_snake.render(9, 12) == 'O'
    assert t_snake.render(9, 13) == 'O'
    assert t_snake.render(10, 13) == 'O'
    assert t_snake.render(10, 12) is None
    t_snake.move(grow=True, direction='RIGHT')
    assert t_snake.velocity == (1,0)
    assert t_snake.location[0] == (10,11)
    assert t_snake.location[1] == (9,11)
    assert t_snake.location[2] == (9,12)
    assert t_snake.location[3] == (9,13)
    assert t_snake.location[4] == (10,13)
    assert t_snake.render(10, 11) == '>'
    assert t_snake.render(9, 11) == 'O'
    assert t_snake.render(9, 12) == 'O'
    assert t_snake.render(9, 13) == 'O'
    assert t_snake.render(10, 13) == 'O'
    assert t_snake.render(10, 12) is None
    assert len(t_snake.location) == 5
