import unittest
from game.pieces import *

class TestPieces(unittest.TestCase):

    # I create some pieces to test.
    def setUp(self):
        self.__pawn__ = Pawn("P1", "white", (1, 7), "Pawn")
        self.__pawn2__ = Pawn("P2", "white", (2, 7), "Pawn", False)
        self.__pawn3__ = Pawn("p1", "black", (1, 2), "Pawn")
        self.__pawn4__ = Pawn("p2", "black", (2, 2), "Pawn", False)
        self.__knight__ = Knight("H1", "white", (2, 8), "Knight", 1)
        self.__bishop__ = Bishop("B1", "white", (3, 8), "Bishop")
        self.__rook__ = Rook("R1", "white", (1, 8), "Rook")
        self.__queen__ = Queen("Q1", "white", (4, 8), "Queen")
        self.__king__ = King("K1", "white", (5, 8), "King")
        self.__box__ = Box("W", "white")

    # I test that the pieces have the initial movement possibilities.
    # For the pawns, I see the options with __primera_posicion__

    def test_pawn_white_inicial_possible_movements(self):
        possible_movements = self.__pawn__.possible_movements()
        self.assertIn((1, 5), possible_movements)
    
    def test_pawn_white_posterior_possible_movements(self):
        possible_movements = self.__pawn2__.possible_movements()
        self.assertIn((2, 6), possible_movements)

    def test_pawn_black_inicial_possible_movements(self):
        possible_movements = self.__pawn3__.possible_movements()
        self.assertIn((1, 4), possible_movements)

    def test_pawn_black_posterior_possible_movements(self):
        possible_movements = self.__pawn4__.possible_movements()
        self.assertIn((2, 3), possible_movements)
    
    def test_knight_possible_movements(self):
        possible_movements = self.__knight__.possible_movements()
        self.assertIn((3, 6), possible_movements)
    
    def test_bishop_possible_movements(self):
        possible_movements = self.__bishop__.possible_movements()
        self.assertIn((4, 7), possible_movements)

    def test_rook_possible_movements(self):
        possible_movements = self.__rook__.possible_movements()
        self.assertIn((1, 7), possible_movements)

    def test_queen_possible_movements(self):
        possible_movements = self.__queen__.possible_movements()
        self.assertIn((5, 7), possible_movements)

    def test_king_possible_movements(self):
        possible_movements = self.__king__.possible_movements()
        self.assertIn((5, 7), possible_movements)
    
    # I test the move_piece function for a normal piece and a pawn.

    def test_move_piece(self):
        x, y = (3, 6)
        self.__knight__.move((x, y))
        # I check that the position of the piece has been updated.
        self.assertEqual(self.__knight__.__position__, (x, y))
    
    def test_move_pawn(self):
        x, y = (1, 6)
        self.__pawn__.move((x, y))
        self.assertEqual(self.__pawn__.__position__, (x, y))

if __name__ == "__main__":
    unittest.main()
