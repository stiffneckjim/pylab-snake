import pytest
import main

def test_game_board():
  test_game = main.Game(10, 10)
  assert test_game.height == 10
  assert test_game.width == 10
  assert len(test_game.board) == 10
  assert len(test_game.board[0]) == 10