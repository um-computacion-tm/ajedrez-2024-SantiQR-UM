import unittest
from game.database import *
from game.pieces.pieces import *
from game.pieces.pawn import *


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.__db__ = DB()
        self.__pawn__ = Pawn("P1", "white", (1, 7), "Pawn")
        self.__box__ = Box("B" , "black")
        self.__db__.add(self.__pawn__)
        self.__db__.add(self.__box__)

    # I test adding a piece.
    def test_add(self):
        # With assertIn I check that the piece is in the DB.
        self.assertIn("P1", self.__db__.data_base)

    # I test searching for a piece.
    def test_search(self):
        piece = self.__db__.search("P1")
        # With assertEqual I check that the piece is the expected one.
        self.assertEqual(piece, self.__pawn__)


if __name__ == "__main__":
    unittest.main()
