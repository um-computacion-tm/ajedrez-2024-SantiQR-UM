import unittest
from juego.BD import *
from juego.piezas import *
from juego.piezas import *

class TestBD(unittest.TestCase):

    def setUp(self):
        self.__bd__ = BD()
        self.__peon__ = Peon("P1", "blanca", (1, 7), u"\u2659", "negra", "Peon")
        self.__casilla__ = Espacio("N" , "negra", u"\u25A0")
        self.__bd__.add(self.__peon__)
        self.__bd__.add(self.__casilla__)

    # Testeo añadir una pieza.
    def test_add(self):
        # Con assertIn compruebo que la pieza está en la BD.
        self.assertIn("P1", self.__bd__.__base_datos__)

    # Testeo buscar una pieza.
    def test_search(self):
        pieza = self.__bd__.search("P1")
        # Con assertEqual compruebo que la pieza es la esperada.
        self.assertEqual(pieza, self.__peon__)

    # Testeo buscar una casilla por color.
    # Test por si se quiere usar esta función
    # def test_search_espacio(self):
    #     var = self.__bd__.search_espacio("negra")
    #     self.assertEqual(var, "N")

if __name__ == "__main__":
    unittest.main()
