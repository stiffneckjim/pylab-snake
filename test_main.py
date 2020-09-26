import pytest
import main

@pytest.mark.parametrize("height, width",[(10,10),(8,12)])
def test_game_board(height, width):
  test_game = main.Game(height, width)
  assert test_game.height == height
  assert test_game.width == width
  assert len(test_game.board) == height
  assert len(test_game.board[0]) == width