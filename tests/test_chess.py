import unittest
from unittest.mock import MagicMock
from game.board import *
from game.chess import *
import sys
from io import StringIO

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    # I test that the turn can be changed.
    def test_change_turn(self):
        self.assertEqual(self.chess.__turn__, "white")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "black")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "white")

    # I test that the lists are filled.
    def test_play(self):
        self.chess.play()
        self.assertIsNotNone(self.chess.__pieces_list__)
        self.assertIsNotNone(self.chess.__instances_list__)
        self.assertIsNotNone(self.chess.__possibilities_list__)

    # I test that the chess board can be printed.
    def test_imprimir_tablero_ajedrez(self):
        # I redirected the output to compare it.
        captured_output = StringIO()
        sys.stdout = captured_output

        # I print the chess board.
        self.chess.print_chess_board()

        sys.stdout = sys.__stdout__
        assert '''  a b c d e f g h   
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8 
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7 
6 □ ■ □ ■ □ ■ □ ■ 6 
5 ■ □ ■ □ ■ □ ■ □ 5 
4 □ ■ □ ■ □ ■ □ ■ 4 
3 ■ □ ■ □ ■ □ ■ □ 3 
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 2 
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1 
  a b c d e f g h   ''' in captured_output.getvalue()  # Its a bit ugly, but it works, hahaha.

    # I test that the data is passed well and that a piece can be moved.
    def test_move_chess(self):
        selection = MagicMock()
        selection.__name__ = "Pawn"
        selection.__color__ = "black"
        selection.__position__ = (2, 2)
        new_position_str = "b5"
        new_position_int = (2, 4)
        old_position = ('b', '7')
        final_possibilities = [(2, 3), (2, 4)]

        chess, move_string = \
            self.chess.move_chess(selection, new_position_str,
                                        new_position_int, old_position,
                                        final_possibilities)

        self.assertEqual(move_string, "\nMovement made: black Pawn b7 has moved to b5\n")

    # I test that the end can be verified.
    def test_check_end(self):
        self.chess.__board__ = Board()
        self.assertFalse(self.chess.check_end())


if __name__ == '__main__':
    unittest.main()