import unittest
from unittest.mock import patch, MagicMock
from juego.tablero import *
from juego.piezas import *
from juego.BD import *
import io
import sys

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.__tablero__ = Tablero()
        self.__BD_piezas__ = BD()
        self.__BD_espacios__ = BD()

    # Testeo que el tablero se crea con instancias de BD.
    def test_crear_tablero_inicial(self):
        self.assertIsInstance(self.__tablero__.__tablero__, list)
        self.assertIsInstance(self.__tablero__.__BD_piezas__, BD)  
        self.assertIsInstance(self.__tablero__.__BD_espacios__, BD)  

    # Testeo que imprimir_tablero funciona.
    def test_imprimir_tablero(self):
        tablero = Tablero()
        captured_output = io.StringIO()  # Creo un buffer en memoria.
        sys.stdout = captured_output  # Redirijo el stdout al buffer.
        tablero.imprimir_tablero()  # Llamo al método.
        sys.stdout = sys.__stdout__  # Restauro el stdout.
        assert '''  a b c d e f g h   
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8 
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7 
6 □ ■ □ ■ □ ■ □ ■ 6 
5 ■ □ ■ □ ■ □ ■ □ 5 
4 □ ■ □ ■ □ ■ □ ■ 4 
3 ■ □ ■ □ ■ □ ■ □ 3 
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 2 
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1 
  a b c d e f g h   ''' in captured_output.getvalue()  # Es medio feo, pero funciona jajaja.

    # Testeo que obtener_piezas_movibles funciona para diferentes piezas y colores.

    @patch('builtins.print') # A veces lo uso para que atrape el output.
    def test_obtener_piezas_movibles_negras(self, mock_print):
        # Es la primera vez que uso MagicMock, y la verdad que me parecio muy útil, pero cada tanto
        # me da ciertos problemitas, jaja.
        # Por lo que entendí sirve para simular el comportamiento de un objeto, y absorbe sus
        # atributos y comportamientos.
        # En este caso, pieza_mock es un objeto, que no ha heredado nada de ninguna clase, eso lo 
        # uso más adelante, con MagicMock("spec = clase").
        pieza_mock = MagicMock()
        pieza_mock.__nom__ = "p"
        pieza_mock.__posicion__ = (1, 2)
        pieza_mock.var.return_value = "p1"
        self.__BD_piezas__.add(pieza_mock)
        
        # Seteo a que instancias_piezas solo pueda devolver pieza_mock y True.
        # Simulo que el peón puede moverse a 'a3'.
        self.__tablero__.instancias_piezas = MagicMock(return_value=(pieza_mock, True, [(1, 3)]))
        # Simulo que el movimiento de la pieza es correcto.
        self.__tablero__.mover_pieza = MagicMock(return_value=True)  

        # Recibo el resultado de la función obtener_piezas_movibles.
        resultado = self.__tablero__.obtener_piezas_movibles("negra")
        tablero, lista_piezas, lista_instancias, lista_posibilidades = resultado

        # Verifico que la pieza fue seleccionada.
        self.assertIn('p', lista_piezas)
        self.assertIn(pieza_mock, lista_instancias)
        self.assertIn([(1, 3)], lista_posibilidades)

    @patch('builtins.print')
    def test_obtener_piezas_movibles_blancas(self, mock_print):
        # Configuro pieza blanca en la BD con MagicMock.
        pieza_mock = MagicMock()
        pieza_mock.__nom__ = "P"
        pieza_mock.__posicion__ = (7, 7)
        pieza_mock.var.return_value = "P7"
        self.__BD_piezas__.add(pieza_mock)

        # Simulo que el peón puede moverse a 'a6'.
        self.__tablero__.instancias_piezas = MagicMock(return_value=(pieza_mock, True, [(7, 6)]))
        # Simulo que el movimiento de la pieza es correcto.
        self.__tablero__.mover_pieza = MagicMock(return_value=True)  

        # Recibo el resultado de la función obtener_piezas_movibles.
        resultado = self.__tablero__.obtener_piezas_movibles("blanca")
        tablero, lista_piezas, lista_instancias, lista_posibilidades = resultado

        # Verifico que la pieza fue seleccionada.
        self.assertIn('P', lista_piezas)
        self.assertIn(pieza_mock, lista_instancias)
        self.assertIn([(7, 6)], lista_posibilidades)

    # También testeo que se pueden atrapar los errores.
    @patch('builtins.print')
    def test_obtener_piezas_movibles_errores(self, mock_print):
        pieza_mock_1 = MagicMock()
        pieza_mock_1.__nom__ = "Peon"
        pieza_mock_1.__posicion__ = (1, 7)
        pieza_mock_1.var.return_value = "P1"
        self.__BD_piezas__.add(pieza_mock_1)

        pieza_mock_2 = MagicMock()
        pieza_mock_2.__nom__ = "Peon"
        pieza_mock_2.__posicion__ = (2, 7)
        pieza_mock_2.var.return_value = "P2"
        self.__BD_piezas__.add(pieza_mock_2)
        
        # Uso side_effect para alternar entre que retorne False y True.
        # La secuencia deseada es: False una vez y True 15 veces.
        # Esto porque tiene que pasar 16 veces por la iteración que hice en tablero.py.
        secuencia = [(pieza_mock_2, False, [])] + [(pieza_mock_1, True, [(1, 6)])] * 15
        # Repito la secuencia 6 veces, porque es la cantidad de veces que se llama a 
        # instancias_piezas.
        resultados = secuencia * 6
        
        # Simulo que instancias_piezas devuelva la secuencia de resultados.
        self.__tablero__.instancias_piezas = MagicMock(side_effect=resultados)

        self.__tablero__.mover_pieza = MagicMock(return_value=True)

         # Recibo el resultado de la función obtener_piezas_movibles.
        resultado = self.__tablero__.obtener_piezas_movibles("blanca")
        tablero, lista_piezas, lista_instancias, lista_posibilidades = resultado

        # Verifico que la pieza fue seleccionada.
        self.assertIn('Peon', lista_piezas)
        self.assertIn(pieza_mock_1, lista_instancias)
        self.assertIn([(1, 6)], lista_posibilidades)

    # Testeo que instancias_piezas funciona.
    @patch('builtins.print')
    def test_instancias_piezas(self, mock_print):
        pieza, movible, posibilidades = self.__tablero__.instancias_piezas(self.__tablero__.__BD_piezas__, 'P', 1)
        self.assertIsInstance(pieza, Peon)

    # Testeo que movible funciona para las diferentes piezas.

    # Para un movimiento vertical es sencillo, porque se puede aplicar al principio de la partida.
    @patch('builtins.print')
    def test_movible_peon_vertical(self, mock_print):
        # Busco la pieza original y verifico que se puede mover.
        pieza = self.__tablero__.__BD_piezas__.search('P1')
        movible, posibilidades = self.__tablero__.movible(pieza)
        self.assertTrue(movible)

    # Para un movimiento diagonal es más complicado, porque hay que setear un escenario en el que
    # se pueda aplicar, ya que se necesita la pieza enemiga en la posicion de destino.
    @patch('builtins.print')
    def test_movible_peon_diagonal(self, mock_print):
        # Para eso voy a usar una instancia de Peon. Acá uso "spec" por primera vez, ya que
        # en movible se llama a "isinstance" que requiere conocer que tipo de clase es.
        pieza_peon = MagicMock(spec = Peon)
        pieza_peon.__nom__ = "Peon"
        pieza_peon.__color__ = "negra"
        pieza_peon.__posicion__ = (3, 3)
        pieza_peon.__vive__ = True

        # Simulo la posibilidad de movimientos diagonales del peón.
        pieza_peon.movimientos_posibles.return_value = [(2, 4), (4, 4)]

        # Creo un mock del tablero vacío, lleno de espacios, que despues voy a cambiar.
        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]
        
        # Configuro casillas específicas para que devuelvan instancias de Pieza enemiga.
        # ¡Tengo que pasarlo como [y][x] porque el mock de tablero es una lista de listas!
        # Estuve 2 horas como boludo hasta que me di cuenta jajajaja.
        self.__tablero__.__tablero__[4][2] = MagicMock(spec=Pieza, __color__="blanca")
        self.__tablero__.__tablero__[4][4] = MagicMock(spec=Pieza, __color__="blanca")

        # Llamo al método.
        movible, posibilidades = self.__tablero__.movible(pieza_peon)

        # Verifico que el movimiento está en la lista de posibilidadesb y que es movible.
        self.assertIn((2, 4), posibilidades)
        self.assertIn((4, 4), posibilidades)
        self.assertTrue(movible)

    # Para un caballo es parecido al test anterior. Podría hacerlo con el caballo original, pero
    # voy a hacerlo con una instancia de caballo nueva así tiene la posibilidad de capturar, y puedo 
    # testear más cosas a la vez.
    @patch('builtins.print')
    def test_movible_caballo(self, mock_print):
        pieza_caballo = MagicMock(spec=Caballo)
        pieza_caballo.__nom__ = "Caballo"
        pieza_caballo.__color__ = "blanco"
        pieza_caballo.__posicion__ = (4, 4)
        pieza_caballo.__vive__ = True

        pieza_caballo.movimientos_posibles.return_value = [(6, 5), (2, 5), (5, 6)]

        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]

        # Configuro una pieza en la casilla destino, para que la pueda comer, esto permite que
        # el test entre en diferentes partes del código.
        self.__tablero__.__tablero__[5][2] = MagicMock(spec=Pieza, __color__="blanca")

        movible, posibilidades = self.__tablero__.movible(pieza_caballo)

        self.assertTrue(movible)
        self.assertIn((6, 5), posibilidades)
        self.assertIn((2, 5), posibilidades)
        self.assertIn((5, 6), posibilidades)

    # El test con torre también me va a permitir probar diferentes iteraciones del código que 
    # tienen que ser hechos con piezas normales (no aplican peones ni caballos).
    @patch('builtins.print')
    def test_movible_torre(self, mock_print):
        pieza_torre = MagicMock(spec=Torre)
        pieza_torre.__nom__ = "Torre"
        pieza_torre.__color__ = "blanco"
        pieza_torre.__posicion__ = (1, 1)
        pieza_torre.__vive__ = True

        # Movimiento vertical y horizontal
        pieza_torre.movimientos_posibles.return_value = [(1, 4), (4, 1)] 

        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]

        # Configuro una pieza que bloquee el camino de la torre, para sacar una de las posibilidades.
        self.__tablero__.__tablero__[3][1] = MagicMock(spec=Pieza, __color__="blanca")

        movible, posibilidades = self.__tablero__.movible(pieza_torre)

        self.assertTrue(movible)
        # En este caso verifico que no se pueda mover a la posición (1, 4) porque está bloqueada.
        self.assertNotIn((1, 4), posibilidades)
        self.assertIn((4, 1), posibilidades)
    
    # También testeo los casos de error para el método movible.
    @patch('builtins.print')
    def test_movible_errores(self, mock_print):
        # Creo una pieza con estado no viva y una que tiene posiciones fuera del tablero.

        pieza_no_viva = MagicMock(spec=Peon)
        pieza_no_viva.__nom__ = "P"
        pieza_no_viva.__color__ = "blanco"
        pieza_no_viva.__posicion__ = (3, 3)
        pieza_no_viva.__vive__ = False

        pieza_fuera_tablero = MagicMock(spec=Peon)
        pieza_fuera_tablero.__nom__ = "P"
        pieza_fuera_tablero.__color__ = "blanco"
        pieza_fuera_tablero.__posicion__ = (3, 3)
        pieza_fuera_tablero.__vive__ = True
        pieza_fuera_tablero.movimientos_posibles = MagicMock(return_value=[(0, 0), (9, 9)])

        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]

        # Test pieza no viva
        movible, posibilidades = self.__tablero__.movible(pieza_no_viva)
        self.assertFalse(movible)
        self.assertEqual(posibilidades, [])

        # Test pieza fuera del tablero
        movible, posibilidades = self.__tablero__.movible(pieza_fuera_tablero)
        self.assertFalse(movible)
        self.assertEqual(posibilidades, [])

    # Testeo que mover_pieza funciona, para curso normal, comer y casos de error.
    
    @patch('builtins.print')
    def test_mover_pieza(self, mock_print):
        # En este caso también se puede usar la instancia original.
        pieza = self.__tablero__.__BD_piezas__.search('P1')
        movido = self.__tablero__.mover_pieza(pieza, 'a3', [(1, 6)])
        self.assertTrue(movido)
    
    @patch('builtins.print')
    def test_mover_pieza_comer(self, mock_print):
        pieza_mock = MagicMock(spec=Peon)
        pieza_mock.__nom__ = "Peon"
        pieza_mock.__color__ = "blanca"
        pieza_mock.__posicion__ = (3, 3)
        pieza_mock.__vive__ = True
        self.__BD_piezas__.add(pieza_mock)
        
        movido = self.__tablero__.mover_pieza(pieza_mock, 'd7', [(4, 2)])
        self.assertTrue(movido)

    @patch('builtins.print')
    def test_mover_pieza_errores(self, mock_print):
        pieza_mock = MagicMock(spec=Peon)
        pieza_mock.__nom__ = "Peon"
        pieza_mock.__color__ = "blanca"
        pieza_mock.__posicion__ = (3, 3)
        pieza_mock.__vive__ = True
        self.__BD_piezas__.add(pieza_mock)
        
        # No se puedo mover, porque la posición no es válida.
        movido = self.__tablero__.mover_pieza(pieza_mock, 'a3', [(1, 8)])
        self.assertFalse(movido)
        # No se puede mover, porque la posición no existe.
        movido = self.__tablero__.mover_pieza(pieza_mock, 'a', [(1, 6)])
        self.assertRaises(ValueError)

    # Testeo que conversion_coordenadas funciona.

    @patch('builtins.print')
    def test_conversion_coordenadas(self, mock_print):
        x, y = self.__tablero__.conversion_coordenadas(1, 8)
        self.assertEqual((x, y), ('a', '1'))
    
    # Testeo que verificar_victoria funciona, para los diferentes casos.
    # En los de que terminan con exit, uso assertRaises, y en el que termina con return,
    # uso assertIsNone para verificar que sea nulo.

    @patch('builtins.print')
    def test_victoria_por_movimientos_empate(self, mock_print):
        # Todas las piezas se quedan sin movimientos posibles.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    @patch('builtins.print')
    def test_victoria_por_movimientos_negras_ganan(self, mock_print):
        # Todas las piezas blancas se quedan sin movimientos posibles.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[(3, 3)])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    @patch('builtins.print')
    def test_victoria_por_movimientos_blancas_ganan(self, mock_print):
        # Todas las piezas negras se quedan sin movimientos posibles.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[(2, 2)])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    @patch('builtins.print')
    def test_victoria_por_piezas_blancas_ganan(self, mock_print):
        # Todas las piezas negras son comidas.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.__vive__ = False

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    @patch('builtins.print')
    def test_victoria_por_piezas_negras_ganan(self, mock_print):
        # Todas las piezas blancas son comidas.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.__vive__ = False

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    @patch('builtins.print')
    def test_verificar_victoria_none(self, mock_print):
        # Seteo que todas las piezas vivan y tengan movimientos.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            pieza.__vive__ = True
        
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[(3 ,3)])
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[(2, 2)])

        resultado = self.__tablero__.verificar_victoria()
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
