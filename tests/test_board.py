import unittest
from unittest.mock import patch, MagicMock
from game.board import *
from game.pieces.pieces import *
from game.pieces.pawn import Pawn
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.rook import Rook
from game.pieces.queen import Queen
from game.pieces.king import King
from game.database import *
import io
import sys

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__DB_pieces__ = DB()
        self.__DB_boxes__ = DB()

    # I test that the board is created with instances of DB.
    def test_create_initial_board(self):
        self.assertIsInstance(self.__board__.board, list)
        self.assertIsInstance(self.__board__.DB_pieces, DB)  
        self.assertIsInstance(self.__board__.DB_boxes, DB)  
    
    # I test that the method obtains movable pieces works for different pieces and colors.

    @patch('builtins.print') # Sometimes I use it to catch the output.
    def test_obtain_black_movable_pieces(self, mock_print):
        # It's the first time I use MagicMock, and the truth is that I found it very useful, but 
        # every once in a while it gave me some problems, haha.
        # As far as I understood it serves to simulate the behavior of an object, and it absorbs its
        # attributes and behaviors.
        # In this case, piece_mock is an object, that has not inherited anything of any class, 
        # thats later, with MagicMock(“spec = class”).
        mock_piece = MagicMock(spec=Pawn)
        mock_piece.name = "p"
        mock_piece.position = (1, 2)
        mock_piece.id.return_value = "p1"
        self.__board__.__DB_pieces__.add(mock_piece)
        
        # I set it to only return mock_piece and True.
        # I simulate that the peon can move to 'a3'.
        self.__board__.piece_instances = MagicMock(return_value = (mock_piece, True, [(1, 3)]))
        # I set it to return True.
        self.__board__.move_piece = MagicMock(return_value = True)  

        # I call it.
        result = self.__board__.obtain_movable_pieces("black")
        board, pieces_list, instances_list, possibilities_list = result

        # I check that it was selected.
        self.assertIn('p', pieces_list)
        self.assertIn(mock_piece, instances_list)
        self.assertIn([(1, 3)], possibilities_list)

    @patch('builtins.print')
    def test_obtain_white_movable_pieces(self, mock_print):
        # I set a white piece in the DB with MagicMock.
        mock_piece = MagicMock()
        mock_piece.name = "P"
        mock_piece.position = (7, 7)
        mock_piece.id.return_value = "P7"
        self.__board__.__DB_pieces__.add(mock_piece)

        # I set it so that the pawn can move to 'a6'.
        self.__board__.piece_instances = MagicMock(return_value = (mock_piece, True, [(7, 6)]))
        # I set it to return True.
        self.__board__.move_piece = MagicMock(return_value = True)  

        # I call obtain_movable_pieces.
        result = self.__board__.obtain_movable_pieces("white")
        board, pieces_list, instances_list, possibilities_list = result

        # I check that it was selected.
        self.assertIn('P', pieces_list)
        self.assertIn(mock_piece, instances_list)
        self.assertIn([(7, 6)], possibilities_list)

    # I also check if it can catch errors.
    @patch('builtins.print')
    def test_obtain_movable_pieces_errors(self, mock_print):
        mock_piece_1 = MagicMock()
        mock_piece_1.name = "Pawn"
        mock_piece_1.position = (1, 7)
        mock_piece_1.id.return_value = "P1"
        self.__board__.__DB_pieces__.add(mock_piece_1)

        mock_piece_2 = MagicMock()
        mock_piece_2.name = "Pawn"
        mock_piece_2.position = (2, 7)
        mock_piece_2.id.return_value = "P2"
        self.__board__.__DB_pieces__.add(mock_piece_2)
        
        # I use side_effect to toggle between returning False and True.
        # The desired sequence is: False once and True 15 times.
        # This because it has to go through the iteration I did in board.py 16 times.
        sequence = [(mock_piece_2, False, [])] + [(mock_piece_1, True, [(1, 6)])] * 15
        # I repeat the sequence 6 times, because that's the number of times that 
        # piece_instances.
        results = sequence * 6
        
        # Simulo que piece_instances devuelva la sequence de results.
        self.__board__.piece_instances = MagicMock(side_effect = results)

        self.__board__.move_piece = MagicMock(return_value = True)

        # I recieve the result of the function obtain_movable_pieces.

        result = self.__board__.obtain_movable_pieces("white")
        board, pieces_list, instances_list, possibilities_list = result

        # I check that it was selected.
        self.assertIn('Pawn', pieces_list)
        self.assertIn(mock_piece_1, instances_list)
        self.assertIn([(1, 6)], possibilities_list)

    # I test that piece_instances works.
    @patch('builtins.print')
    def test_piece_instances(self, mock_print):
        piece, movable, possibilities = self.__board__.piece_instances(self.__board__.__DB_pieces__, 'P', 1)
        self.assertIsInstance(piece, Pawn)
        self.assertTrue(movable)
        self.assertEqual(possibilities, [(1, 5), (1, 6)])

    # I test that movable works for different pieces.

    # For a vertical movement it is simple, because it can be applied at the beginning of the game.
    @patch('builtins.print')
    def test_movable_vertical_pawn(self, mock_print):
        # I search for the original piece and check that it can be moved.
        piece = self.__board__.__DB_pieces__.search('P1')
        movable, possibilities = self.__board__.movable(piece)
        self.assertTrue(movable)
        self.assertIn((1, 6), possibilities)
        self.assertNotIn((1, 4), possibilities)

    # For a diagonal movement it is more complicated, because you have to set a scenario in which
    # can be applied, since you need the enemy piece in the target position.
    @patch('builtins.print')
    def test_movable_diagonal_pawn(self, mock_print):
        # For that I am going to use an instance of Pawn. Here I use “spec” for the first time, because
        # in movable we call “isinstance” which requires to know what type of class it is.
        pawn_piece = MagicMock(spec = Pawn)
        pawn_piece.name = "Pawn"
        pawn_piece.color = "black"
        pawn_piece.position = (3, 3)
        pawn_piece.lives = True

        # I set the possibilites of the pawn.
        pawn_piece.possible_movements.return_value = [(2, 4), (4, 4)]

        # I create an empty mock board, filled with nothing but boxes, that I will change later.
        self.__board__.__board__ = [[MagicMock(spec=Box) for _ in range(10)] for _ in range(10)]
        
        # I set specific boxes to return instances of enemy Piece.
        # I have to pass it as [y][x] because the board mock is a list of lists!
        # I spent 2 hours like an idiot until I realized hahahaha.
        self.__board__.__board__[4][2] = MagicMock(spec=Piece, color="white")
        self.__board__.__board__[4][4] = MagicMock(spec=Piece, color="white")

        # I call the method.
        movable, possibilities = self.__board__.movable(pawn_piece)

        # I check that the movement is in the list of possibilities and that it is movable.
        self.assertIn((2, 4), possibilities)
        self.assertIn((4, 4), possibilities)
        self.assertTrue(movable)

    # For a knight it is similar to the previous test. I could do it with the original knight, but
    # I'm going to do it with a new knight instance so it has a chance to capture, and I can
    # test more things at once.
    @patch('builtins.print')
    def test_movable_knight(self, mock_print):
        knight_piece = MagicMock(spec=Knight)
        knight_piece.name = "Knight"
        knight_piece.color = "white"
        knight_piece.position = (4, 4)
        knight_piece.lives = True

        knight_piece.possible_movements.return_value = [(6, 5), (2, 5), (5, 6)]

        self.__board__.__board__ = [[MagicMock(spec=Box) for _ in range(10)] for _ in range(10)]

        # I set a piece in the target box, so that it can eat it, this allows the 
        # test to enter different parts of the code.
        self.__board__.__board__[5][2] = MagicMock(spec=Piece, color="black")

        movable, possibilities = self.__board__.movable(knight_piece)

        self.assertTrue(movable)
        self.assertIn((6, 5), possibilities)
        self.assertIn((2, 5), possibilities)
        self.assertIn((5, 6), possibilities)

    # The rook test will also allow me to test different iterations of the code that 
    # have to be done with normal pieces (no pawns or knights apply).
    @patch('builtins.print')
    def test_movable_rook(self, mock_print):
        rook_piece = MagicMock(spec=Rook)
        rook_piece.name = "Rook"
        rook_piece.color = "white"
        rook_piece.position = (1, 1)
        rook_piece.lives = True

        # Vertical and horizontal movements
        rook_piece.possible_movements.return_value = [(1, 4), (4, 1)] 

        self.__board__.__board__ = [[MagicMock(spec=Box) for _ in range(10)] for _ in range(10)]

        # I set a piece that blocks the path of the rook, so I can take one of the possibilities.
        self.__board__.__board__[3][1] = MagicMock(spec=Piece, color="white")

        movable, possibilities = self.__board__.movable(rook_piece)

        self.assertTrue(movable)
        # In this case I check that it cannot move to the position (1, 4) because its blocked.
        self.assertNotIn((1, 4), possibilities)
        self.assertIn((4, 1), possibilities)
    
    # I also test the cases of error for the movable method.
    @patch('builtins.print')
    def test_movable_errors(self, mock_print):
        # I create a piece with a non-living state and a position outside the board.

        dead_piece = MagicMock(spec=Pawn)
        dead_piece.name = "P"
        dead_piece.color = "white"
        dead_piece.position = (3, 3)
        dead_piece.lives = False

        outside_piece = MagicMock(spec=Pawn)
        outside_piece.name = "P"
        outside_piece.color = "white"
        outside_piece.position = (3, 3)
        outside_piece.lives = True
        outside_piece.possible_movements = MagicMock(return_value=[(0, 0), (9, 9)])

        self.__board__.__board__ = [[MagicMock(spec=Box) for _ in range(10)] for _ in range(10)]

        # Test dead piece
        movable, possibilities = self.__board__.movable(dead_piece)
        self.assertFalse(movable)
        self.assertEqual(possibilities, [])

        # Test outside piece
        movable, possibilities = self.__board__.movable(outside_piece)
        self.assertFalse(movable)
        self.assertEqual(possibilities, [])

    # I test that move_piece works, for normal course, eating and error cases.
    
    @patch('builtins.print')
    def test_move_piece(self, mock_print):
        # In this case we can also use the original instance.
        piece = self.__board__.__DB_pieces__.search('P1')
        moved = self.__board__.move_piece(piece, 'a3', (1, 6), ('a','2'), [(1, 6)])
        self.assertTrue(moved)
    

    @patch('builtins.print')
    def test_move_piece_eat(self, mock_print):
        mock_piece = MagicMock(spec=Pawn)
        mock_piece.name = "Pawn"
        mock_piece.color = "white"
        mock_piece.position = (3, 3)
        mock_piece.lives = True
        self.__DB_pieces__.add(mock_piece)
        
        moved = self.__board__.move_piece(mock_piece, 'd7', (4, 2), ('c','6'), [(4, 2)])
        self.assertTrue(moved)

        

if __name__ == "__main__":
    unittest.main()
