import unittest
from unittest.mock import patch
from interfaz import main

class TestInterfaz(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
