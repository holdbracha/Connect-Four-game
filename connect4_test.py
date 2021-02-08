from connect_four import ConnectFour
import pytest


def test_class():
  assert ConnectFour() != None, "has class"


def test_board_size():
  game = ConnectFour()
  player = 1
  game.player = player
  with pytest.raises(IndexError):
    game.insert_disc(8)

  with pytest.raises(IndexError):
    for _ in range(8):
      game.insert_disc(0)


def test_insert_disc():
  game = ConnectFour()
  col = 1
  player = 1
  game.player = player
  game.insert_disc(col)
  msg = "insert disc into (0,0)"
  assert game.get_board_cell(0, col) == player, msg

def test_insert_disc_on_top():
  game = ConnectFour()
  player = 1
  game.player = player
  col = 2
  for _ in range(3):
    game.insert_disc(col)
  msg = "insert disc of player 1 into (2,2)"
  assert game.get_board_cell(2, col) == player, msg




