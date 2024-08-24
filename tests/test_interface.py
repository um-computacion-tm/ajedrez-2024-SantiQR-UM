import unittest
from unittest.mock import patch, MagicMock
from game.interface import *
from game.chess import *

class TestInterface(unittest.TestCase):

    def setUp(self):
        self.__game__ = Game()

    # I test that the main function works, can move a piece and then exit.
    @patch('builtins.input', side_effect=['1', '1', '1', '1', 'a3', '2', '2'])
    @patch('builtins.print') 
    @patch('sys.exit')
    def test_main_game_movement(self, mock_exit, mock_print, mock_input):
        # I test that it exits with sys.exit
        with self.assertRaises(SystemExit):
            self.__game__.main()

        # I confirm it asked for input 7 times.
        self.assertEqual(mock_input.call_count, 7)
        # I confirm that it gave the draw message.
        mock_print.assert_any_call("\nGame over in a draw.\n")
    
    # I test that it works, and that the check_victory function works.
    @patch('builtins.input', side_effect=['1', '1', '1', 'a3'])
    @patch('builtins.print') 
    def test_iniciate_victory_game(self, mock_print, mock_input):
        # I mock with MagicMock to return that response.
        self.__game__.__chess__.check_end = MagicMock(return_value="victory")
        self.__game__.start_game()
        
        # I confirm that it asked for input 4 times.
        self.assertEqual(mock_input.call_count, 4)
        # I confirm that it gave the victory message.
        mock_print.assert_any_call("victory")

    # I test that the errors are handled correctly and that it can exit.
    @patch('builtins.input', side_effect=['1', '3', '2', '2'])
    @patch('builtins.print') 
    @patch('sys.exit')
    def test_main_game_exit(self, mock_exit, mock_print, mock_input):
        
        with self.assertRaises(SystemExit):
            self.__game__.main()

        self.assertEqual(mock_input.call_count, 4)
        mock_print.assert_any_call("\nNot valid option.\n")
        mock_print.assert_any_call("\nGame over in a draw.\n")

    # I test that the errors are handled correctly and that it can exit.
    @patch('builtins.input', side_effect=['3', '2'])
    @patch('builtins.print')
    @patch('sys.exit')
    def test_close_game(self, mock_exit, mock_print, mock_input):
        
        with self.assertRaises(SystemExit):
            self.__game__.main()

        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_any_call("\nNot valid option.\n")
        mock_print.assert_any_call("\nClosing the game.\n")

    # I test that it can go back in the instance options.
    @patch('builtins.input', side_effect=['1', '9', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_main_2_back_and_white(self, mock_print, mock_input):

        self.__game__.__chess__ = Chess.play(self.__game__.__chess__)
        result = self.__game__.options_1()

        self.assertIsNone(result)
        self.assertEqual(mock_input.call_count, 5)

    # I test that it can handle all the possible errors of the user.
    @patch('builtins.input', side_effect=['a', '0', '1', 'a', '1', '0', '1', '1', '', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_main_1_errors(self, mock_print, mock_input):

        self.__game__.__chess__ = Chess.play(self.__game__.__chess__)
        result = self.__game__.options_1()

        self.assertIsNone(result)
        self.assertEqual(mock_input.call_count, 12)

        # I check that it has shown the error message 4 times.
        count = 0
        for call in mock_print.call_args_list:
            args, _ = call
            if len(args) > 0 and args[0] == "\nNot valid option.\n":
                count += 1
        self.assertEqual(count, 4)

    # I test that it shows the options well.
    @patch('builtins.input', side_effect=['1', '1', 'a3'])
    @patch('builtins.print')
    def test_options_1(self, mock_print, mock_input):

        self.__game__.__chess__ = Chess.play(self.__game__.__chess__)
        result = self.__game__.options_1()

        self.assertIsNone(result)
        self.assertEqual(mock_input.call_count, 3)

    # I test that it shows the instance options well.
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('builtins.print')
    def test_options_2(self, mock_print, mock_input):

        self.__game__.__chess__ = Chess.play(self.__game__.__chess__)
        result = self.__game__.options_2(1)

        self.assertFalse(result)

    # I test that the pieces can move with a fake piece.
    @patch('builtins.input', side_effect=['1', '1', 'a3'])
    @patch('builtins.print')
    def test_move_piece(self, mock_print,  mock_input):

        selection = MagicMock(spec = Pawn)
        selection.__position__ = (1, 7)
        selection.__name__ = 'Pawn'
        selection.__color__ = 'white'
        final_possibilities = [(1, 6)]
        result = self.__game__.move(selection, 'a3', final_possibilities)

        self.assertTrue(result)

    # I test that the errors are caught with two fake pieces.
    @patch('builtins.input', side_effect=['1', '1', 'a6'])
    @patch('builtins.print')
    def test_mover_errores(self, mock_print,  mock_input):

        selection = MagicMock(spec = Pawn)
        selection.__position__ = (1, 7)
        selection.__name__ = 'Pawn'
        selection.__color__ = 'white'
        final_possibilities = [(1, 6)]

        seleccion_error = MagicMock(spec = Pawn)
        seleccion_error.__position__ = (1)
        seleccion_error.__name__ = 'Pawn'
        seleccion_error.__color__ = 'white'
        posibilidades_finales_error = [(1, 6)]
        
        result = self.__game__.move(selection, 'a6', final_possibilities)
        self.assertFalse(result)

        result = self.__game__.move(selection, 'a', final_possibilities)
        self.assertFalse(result)

        result = self.__game__.move(seleccion_error, 'a6', posibilidades_finales_error)
        self.assertFalse(result)

    # I test that coordinates_conversion works.
    @patch('builtins.print')
    def test_coordinates_conversion(self, mock_print):
        x, y = UserInterface.coordinates_conversion((1, 8))
        self.assertEqual((x, y), ('a', '1'))

    # I test that inverse_coordinates_conversion works.
    @patch('builtins.print')
    def test_inverse_coordinates_conversion(self, mock_print):
        x, y = UserInterface.inverse_coordinates_conversion("a1")
        self.assertEqual((x, y), (1, 8))

if __name__ == '__main__':
    unittest.main()
