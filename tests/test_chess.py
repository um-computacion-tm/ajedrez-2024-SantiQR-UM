import unittest
from unittest.mock import MagicMock, patch
from game.board import *
from game.chess import *
import sys
from io import StringIO

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()
        self.__board__ = Board()

    # I test that the turn can be changed.
    def test_change_turn(self):
        self.assertEqual(self.chess.turn, "white")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "black")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "white")

    # I test that the lists are filled.
    def test_play(self):
        self.chess.play()
        self.assertIsNotNone(self.chess.pieces_list)
        self.assertIsNotNone(self.chess.instances_list)
        self.assertIsNotNone(self.chess.possibilities_list)

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
        selection.name = "Pawn"
        selection.color = "black"
        selection.position = (2, 2)
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
    
    # I test that victory can be verified, for different cases.
    # I use assertEqual to check that the returned string is the expected one.

    @patch('builtins.print')
    def test_victory_movements_draw(self, mock_print):
        # All the pieces remain without possible movements.
        for piece in self.__board__.__DB_pieces__.__data_base__.values():
            if piece.color == 'white':
                piece.possible_movements = MagicMock(return_value=[])
            if piece.color == 'black':
                piece.possible_movements = MagicMock(return_value=[])

        result = Rules.check_victory(self.__board__)
        self.assertEqual(result, "Draw by movements!")


    @patch('builtins.print')
    def test_victory_movements_black_win(self, mock_print):
        # All the pieces are white and have possible movements.
        for piece in self.__board__.__DB_pieces__.__data_base__.values():
            if piece.color == 'white':
                piece.possible_movements = MagicMock(return_value=[])
            if piece.color == 'black':
                piece.possible_movements = MagicMock(return_value=[(3, 3)])

        result = Rules.check_victory(self.__board__)
        self.assertEqual(result, "The player black has won by movements!")


    @patch('builtins.print')
    def test_victory_movements_white_win(self, mock_print):
        # All the pieces are black and have possible movements.
        for piece in self.__board__.__DB_pieces__.__data_base__.values():
            if piece.color == 'black':
                piece.possible_movements = MagicMock(return_value=[])
            if piece.color == 'white':
                piece.possible_movements = MagicMock(return_value=[(2, 2)])

        result = Rules.check_victory(self.__board__)
        self.assertEqual(result, "The player white has won by movements!")


    @patch('builtins.print')
    def test_victory_pieces_black_win(self, mock_print):
        # The white king is eaten.
        for piece in self.__board__.__DB_pieces__.__data_base__.values():
            if piece.color == 'white':
                piece.__lives__ = False

        result = Rules.check_victory(self.__board__)
        self.assertEqual(result, "The player black has won by capturing the white king!")


    @patch('builtins.print')
    def test_victory_pieces_white_win(self, mock_print):
        # The black king is eaten.
        for piece in self.__board__.__DB_pieces__.__data_base__.values():
            if piece.color == 'black':
                piece.__lives__ = False

        result = Rules.check_victory(self.__board__)
        self.assertEqual(result, "The white player has won by capturing the black king!")


    @patch('builtins.print')
    def test_check_victory_none(self, mock_print):
        # I set that all the pieces are alive and have possible movements.
        for piece in self.__board__.__DB_pieces__.__data_base__.values():
            piece.__lives__ = True
        
        for piece in self.__board__.__DB_pieces__.__data_base__.values():
            if piece.color == 'black':
                piece.possible_movements = MagicMock(return_value=[(3 ,3)])
            if piece.color == 'white':
                piece.possible_movements = MagicMock(return_value=[(2, 2)])

        result = Rules.check_victory(self.__board__)
        self.assertEqual(result, "")



if __name__ == '__main__':
    unittest.main()