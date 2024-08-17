import unittest
from unittest.mock import MagicMock
from juego.tablero import Tablero
from juego.ajedrez import Ajedrez
import sys
from io import StringIO

class TestAjedrez(unittest.TestCase):
    def setUp(self):
        self.ajedrez = Ajedrez()

if __name__ == '__main__':
    unittest.main()