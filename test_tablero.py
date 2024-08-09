import unittest
from unittest.mock import patch, MagicMock
from tablero import Tablero
from piezas import Pieza, Espacio, Peon, Torre, Caballo
from BD import BD
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

    @patch('builtins.input', side_effect=['1', '1', 'a6'])  # Simulo el input del usuario.
    @patch('builtins.print') # A veces lo uso para que atrape el output.
    def test_obtener_piezas_movibles_negras(self, mock_print, mock_input):
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
        resultado = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "negra")
        
        # Verifico que la pieza fue seleccionada y se intentó mover.
        # Verifico que vuelvo a interfaz con return None.
        self.assertIsNone(resultado) 
        # Verifico que se ha llamado a mover_pieza con la pieza y la posición correcta
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock, 'a6', [(1, 3)]) 

    @patch('builtins.input', side_effect=['1', '1', 'g3'])
    @patch('builtins.print')
    def test_obtener_piezas_movibles_blancas(self, mock_print, mock_input):
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

        resultado = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "blanca")
        
        # Verifico que la pieza fue seleccionada y se intentó mover
        self.assertIsNone(resultado)
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock, 'g3', [(7, 6)])

    # Testeo que se puede volver hacia atras y que después funciona.
    @patch('builtins.input', side_effect=['1', '2', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_obtener_piezas_movibles_atras_y_blancas(self, mock_print, mock_input):
        pieza_mock = MagicMock()
        pieza_mock.__nom__ = "Peon"
        pieza_mock.__posicion__ = (1, 7)
        pieza_mock.var.return_value = "P1"
        self.__BD_piezas__.add(pieza_mock)
        
        self.__tablero__.instancias_piezas = MagicMock(return_value=(pieza_mock, True, [(1, 6)])) 
        self.__tablero__.mover_pieza = MagicMock(return_value=True) 

        resultado = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "blanca")

        self.assertIsNone(resultado)
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock, 'a3', [(1, 6)])
        # En este caso verifico que se ha llamado a input 5 veces.
        self.assertEqual(mock_input.call_count, 5)

    # También testeo que se pueden atrapar los errores.
    @patch('builtins.input', side_effect=['a', '0', '1', 'a', '1', '0', '1', '1', '', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_obtener_piezas_movibles_errores(self, mock_print, mock_input):
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

        resultado = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "blanca")

        self.assertIsNone(resultado)
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock_1, 'a3', [(1, 6)])
        # En este caso verifico que se ha llamado a input 12 veces.
        self.assertEqual(mock_input.call_count, 12)
        
        # Verifico que se ha llamado a print 5 veces con ese mensaje.
        count = 0
        for call in mock_print.call_args_list:
            args, _ = call
            if len(args) > 0 and args[0] == "\nOpción no válida.\n":
                count += 1
        self.assertEqual(count, 5)

    # Testeo que instancias_piezas funciona.

    def test_instancias_piezas(self):
        pieza, movible, posibilidades = self.__tablero__.instancias_piezas(self.__tablero__.__BD_piezas__, 'P', 1)
        self.assertIsInstance(pieza, Peon)

    # Testeo que movible funciona para las diferentes piezas.

    # Para un movimiento vertical es sencillo, porque se puede aplicar al principio de la partida.
    def test_movible_peon_vertical(self):
        # Busco la pieza original y verifico que se puede mover.
        pieza = self.__tablero__.__BD_piezas__.search('P1')
        movible, posibilidades = self.__tablero__.movible(pieza)
        self.assertTrue(movible)

    # Para un movimiento diagonal es más complicado, porque hay que setear un escenario en el que
    # se pueda aplicar, ya que se necesita la pieza enemiga en la posicion de destino.
    def test_movible_peon_diagonal(self):
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
    def test_movible_caballo(self):
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
    def test_movible_torre(self):
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
    def test_movible_errores(self):
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

    def test_mover_pieza(self):
        # En este caso también se puede usar la instancia original.
        pieza = self.__tablero__.__BD_piezas__.search('P1')
        movido = self.__tablero__.mover_pieza(pieza, 'a3', [(1, 6)])
        self.assertTrue(movido)
    
    def test_mover_pieza_comer(self):
        pieza_mock = MagicMock(spec=Peon)
        pieza_mock.__nom__ = "Peon"
        pieza_mock.__color__ = "blanca"
        pieza_mock.__posicion__ = (3, 3)
        pieza_mock.__vive__ = True
        self.__BD_piezas__.add(pieza_mock)
        
        movido = self.__tablero__.mover_pieza(pieza_mock, 'd7', [(4, 2)])
        self.assertTrue(movido)

    def test_mover_pieza_errores(self):
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

    def test_conversion_coordenadas(self):
        x, y = self.__tablero__.conversion_coordenadas(1, 8)
        self.assertEqual((x, y), ('a', '1'))
    
    # Testeo que verificar_victoria funciona, para los diferentes casos.
    # En los de que terminan con exit, uso assertRaises, y en el que termina con return,
    # uso assertIsNone para verificar que sea nulo.

    def test_victoria_por_movimientos_empate(self):
        # Todas las piezas se quedan sin movimientos posibles.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_movimientos_negras_ganan(self):
        # Todas las piezas blancas se quedan sin movimientos posibles.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[(3, 3)])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_movimientos_blancas_ganan(self):
        # Todas las piezas negras se quedan sin movimientos posibles.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[(2, 2)])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_piezas_blancas_ganan(self):
        # Todas las piezas negras son comidas.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.__vive__ = False

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_piezas_negras_ganan(self):
        # Todas las piezas blancas son comidas.
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.__vive__ = False

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_verificar_victoria_none(self):
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
