import unittest
from unittest.mock import patch, MagicMock
from juego.interfaz import *
from juego.tablero import *
from juego.BD import *

class TestInterfaz(unittest.TestCase):

    def setUp(self):
        self.__tablero__ = Tablero()

    # Testeo que el programa termina con exit en segunda opcion, y errores.
    @patch('builtins.input', side_effect=['1', '3', '2'])
    @patch('builtins.print') 
    @patch('sys.exit')
    def test_main_juego(self, mock_exit, mock_print, mock_input):
        # Con assertRaises, se comprueba que el programa termina con exit
        with self.assertRaises(SystemExit):
            main()
        # Con assertEqual, se comprueba que se llama al método input 3 veces
        self.assertEqual(mock_input.call_count, 3)
        # Con assert_any_call, se comprueba que se llama al método print alguna vez
        mock_print.assert_any_call("\nOpción no válida.\n")
        mock_print.assert_any_call("\nJuego finalizado en empate.\n")

    # Testeo que el programa termina con exit en primera opcion, y errores.
    @patch('builtins.input', side_effect=['3', '2'])
    @patch('builtins.print')
    @patch('sys.exit')
    def test_cerrar_juego(self, mock_exit, mock_print, mock_input):
        main()

        self.assertEqual(mock_input.call_count, 2)

        mock_print.assert_any_call("\nOpción no válida.\n")
        mock_print.assert_any_call("\nCerrando el juego.\n")

    # Testeo que se puede volver hacia atras y que después funciona.
    @patch('builtins.input', side_effect=['1', '9', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_main_2_atras_y_blancas(self, mock_print, mock_input):

        resultado = main_2(self.__tablero__, "blanca")

        # Verifico que el resultado es None. Lo que significa que se movió la pieza.
        self.assertIsNone(resultado)
        # En este caso verifico que se ha llamado a input 5 veces.
        self.assertEqual(mock_input.call_count, 5)

    # También testeo que se pueden atrapar los errores.
    @patch('builtins.input', side_effect=['a', '0', '1', 'a', '1', '0', '1', '1', '', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_main_2_errores(self, mock_print, mock_input):
        
        resultado = main_2(self.__tablero__, "blanca")

        # Verifico que el resultado es None. Lo que significa que se movió la pieza.
        self.assertIsNone(resultado)
        # En este caso verifico que se ha llamado a input 12 veces.
        self.assertEqual(mock_input.call_count, 12)
        # Verifico que se ha llamado a print 5 veces con ese mensaje.
        count = 0
        for call in mock_print.call_args_list:
            args, _ = call
            if len(args) > 0 and args[0] == "\nOpción no válida.\n":
                count += 1
        self.assertEqual(count, 5)


if __name__ == '__main__':
    unittest.main()
