import unittest
from juego.piezas import *

class TestPiezas(unittest.TestCase):

    # Ya no se usan num ni color_casilla.
    def setUp(self):
        self.__peon__ = Peon("P1", "blanca", (1, 7), u"\u2659", "Peon")
        self.__peon2__ = Peon("P2", "blanca", (2, 7), u"\u2659", "Peon", False)
        self.__peon3__ = Peon("p1", "negra", (1, 2), u"\u2659", "Peon")
        self.__peon4__ = Peon("p2", "negra", (2, 2), u"\u2659", "Peon", False)
        self.__caballo__ = Caballo("C1", "blanca", (2, 8), u"\u2658", "Caballo", 1)
        self.__alfil__ = Alfil("A1", "blanca", (3, 8), u"\u2657", "Alfil")
        self.__torre__ = Torre("T1", "blanca", (1, 8), u"\u2656", "Torre")
        self.__dama__ = Dama("D1", "blanca", (4, 8), u"\u2655", "Dama")
        self.__rey__ = Rey("R1", "blanca", (5, 8), u"\u2654", "Rey")
        self.__casilla__ = Espacio("B", "blanca", u"\u25A1")

    # Testeo que las piezas tienen las posibilidades de movimientos iniciales.
    # Para los peones, veo las opciones con __primera_posicion__

    def test_peon_blanco_movimientos_posibles_inicial(self):
        posibles_movimientos = self.__peon__.movimientos_posibles()
        self.assertIn((1, 5), posibles_movimientos)
    
    def test_peon_blanco_movimientos_posibles_posterior(self):
        posibles_movimientos = self.__peon2__.movimientos_posibles()
        self.assertIn((2, 6), posibles_movimientos)

    def test_peon_negro_movimientos_posibles_inicial(self):
        posibles_movimientos = self.__peon3__.movimientos_posibles()
        self.assertIn((1, 4), posibles_movimientos)

    def test_peon_negro_movimientos_posibles_posterior(self):
        posibles_movimientos = self.__peon4__.movimientos_posibles()
        self.assertIn((2, 3), posibles_movimientos)
    
    def test_caballo_movimientos_posibles(self):
        posibles_movimientos = self.__caballo__.movimientos_posibles()
        self.assertIn((3, 6), posibles_movimientos)
    
    def test_alfil_movimientos_posibles(self):
        posibles_movimientos = self.__alfil__.movimientos_posibles()
        self.assertIn((4, 7), posibles_movimientos)

    def test_torre_movimientos_posibles(self):
        posibles_movimientos = self.__torre__.movimientos_posibles()
        self.assertIn((1, 7), posibles_movimientos)

    def test_dama_movimientos_posibles(self):
        posibles_movimientos = self.__dama__.movimientos_posibles()
        self.assertIn((5, 7), posibles_movimientos)

    def test_rey_movimientos_posibles(self):
        posibles_movimientos = self.__rey__.movimientos_posibles()
        self.assertIn((5, 7), posibles_movimientos)
    
    # Testeo la función mover_pieza para una pieza normal y un peon.
    # Ya no se usa color_casilla.

    def test_mover_pieza(self):
        x, y = (3, 6)
        # nuevo_color_casilla = 'negra'
        self.__caballo__.mover((x, y))
        # Me aseguro de que se hallan actualizado los atributos de la pieza.
        # self.assertEqual(self.__caballo__.__color_casilla__, nuevo_color_casilla)
        self.assertEqual(self.__caballo__.__posicion__, (x, y))
    
    def test_mover_peon(self):
        x, y = (1, 6)
        # nuevo_color_casilla = 'negra'
        self.__peon__.mover((x, y))
        # self.assertEqual(self.__peon__.__color_casilla__, nuevo_color_casilla)
        self.assertEqual(self.__peon__.__posicion__, (x, y))

if __name__ == "__main__":
    unittest.main()
