from game.chess import Chess


# First, I create the game class that will handle the main communication with the facade.
class Game:
    def __init__(self):
        # I initialize an instance of the Chess class.
        self.__chess__ = Chess()
        

    def main(self):
        # This is the main loop of the game.
        while True:
            print("\nWhat do you want to do?")
            print("1. Start the game")
            print("2. Close")
            option = input("\nSelect an option: ")

            if option == "1":
                # Here I restart the game so that when you choose to end in a draw, 
                # the board is restarted.
                self.__init__()
                self.start_game()

            elif option == "2":
                print("\nClosing the game.\n")
                exit()

            else:
                print("\nNot valid option.\n")
                continue


    def start_game(self):
        # Here I made the secondary loop to handle the game of chess already initialized.
        while True:

            # I show the board with its pieces.
            UserInterface.print_board(self.__chess__)

            print("\n1. Move piece (" + self.__chess__.turn + "'s turn)")
            print("2. End game (Draw)")
            action = input("\nSelect an option: ")

            if action == "1":
                # I go to look for the chess piece selection options.
                self.__chess__ = Chess.play(self.__chess__)
                
                # I jump to the function that shows them.
                self.options_1()
                
                # I verify if the game is over.
                end_string = self.__chess__.check_end()
                if end_string != "":
                    print(end_string)
                    UserInterface.print_board(self.__chess__)
                    break
                
                # If its not, I change the turn.
                self.__chess__.change_turn()

            elif action == "2":
                print("\nGame over in a draw.\n")
                break

            else:
                print("\nNot valid option.\n")
                continue


    def options_1(self):
        # I show the options to select a piece.
        while True:

            # I show the board to always be able to see it.
            UserInterface.print_board(self.__chess__)

            # Muestro las opciones de piezas.
            print("\nOptions:")
            num = 1
            for piece in self.__chess__.pieces_list:
                print(f"{num}. {piece}")
                num += 1

            option = input("\nSelect an option: ")
            # I verify if the option entered is valid.
            option, isOK = UserInterface.check_option(option, num-1)

            if not isOK:
                continue
            
            # I jump to the function to show the instances of the selected piece.
            result = self.options_2(option)

            # If the movement was made, I return.
            if result:
                return

    def options_2(self, option):
        # I show the options for selecting piece instances.

        # I show the board again.
        UserInterface.print_board(self.__chess__)
        
        # I show the instances of the selected piece.
        print("\nInstances of the piece:")
        count = 1
        select = []
        for num in range(len(self.__chess__.instances_list)):

            # If the selected piece is equal to the piece in the instance list, I show it.
            if self.__chess__.pieces_list[option-1] == \
                self.__chess__.instances_list[num].name:

                # I convert the coordinates from numeric format to chess format.
                x, y = UserInterface.coordinates_conversion\
                    (self.__chess__.instances_list[num].position)
                
                # I show the instances of the piece.
                print(f"{count}. {self.__chess__.instances_list[num].name} {x}{y}")

                # I save the instances in a list to be able to select them.
                select.append(num)
                count += 1
        # I show an option to go back.
        print(f"{count}. Go back")

        option_2 = input("\nSelect a piece: ")
        # I check if the entered option is valid.
        option_2, isOK = UserInterface.check_option(option_2, count)
        if not isOK:
            return False
        
        # If the option to go back is chosen, I return.
        if option_2 == count:
            return False
        
        # If not, I ask for the new position.
        else:
            # I choose the instance of the piece, using the select list.
            num_instance = select[option_2-1]

            # I look for the final movement possibilities of the piece.
            final_possibilities = self.__chess__.possibilities_list[num_instance]

            # I search for the selected piece instance.
            selection = self.__chess__.board.DB_pieces.search(\
                self.__chess__.instances_list[num_instance].id)
            
            # I ask for the new position.
            new_position = input("Type the new position (eg. 'a3'): ")

            # Salto a la función para move la piece.
            result = self.move(selection, new_position, final_possibilities)

            # If the movement was made, I return.
            if result:
                return True


    def move(self, selection, new_position_str, final_possibilities):
        # I move a piece to a new position.

        # I convert the coordinates from chess format to numeric format.
        position = UserInterface.inverse_coordinates_conversion(new_position_str)
        # I check if the entered option is valid.
        if not position:
            return False
        
        new_position_int = position

        # I convert the coordinates from numeric format to chess format.
        position = UserInterface.coordinates_conversion(selection.position)
        # I check if the entered option is valid.
        if not position:
            return False
        
        old_position = position
        
        # I check if the new position is valid.
        if new_position_int not in final_possibilities:
            print("\nThis move is not possible.\n")
            return False
        
        # I move the piece.
        self.__chess__, move_string = self.__chess__.move_chess(selection, \
            new_position_str, new_position_int, old_position, final_possibilities)
        print(move_string)

        # I return that it was moved.
        return True


# Now, I create the UserInterface class that will handle the special functions of the client.
class UserInterface:
    # I use staticmethod to call the method without having to instantiate the class.
    @staticmethod
    def print_board(chess):
        # I show the chess board.
        chess.print_chess_board()


    @staticmethod
    def check_option(option, num):
        # I check if the entered option is valid.
        try:
            # I convert the option to an integer.
            option = int(option)

            # I check that it does not exceed the limit or is 0.
            if option > num or option == 0:
                print("\nNot valid option.\n")
                return option, False
            
            # If everything is fine, I return the option and True.
            return option, True
        
        # If it cannot be converted to an integer, I return False.
        except ValueError:
            print("\nNot valid option.\n")
            return option, False


    @staticmethod
    def coordinates_conversion(position):
        # I convert the coordinates from numeric format to chess format.
        columns = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        rows = {8: '1', 7: '2', 6: '3', 5: '4', 4: '5', 3: '6', 2: '7', 1: '8'}
        
        # I try to convert it.
        try:
            new_column, new_row = position
            x = columns[new_column]
            y = rows[new_row]

        # If it cannot be converted, I return False.
        except (KeyError, ValueError, TypeError, IndexError):
            print("\nIncorrect values.\n")
            return False
        
        # If I could, I return it.
        return x, y


    @staticmethod
    def inverse_coordinates_conversion(position):
        # I convert the coordinates from chess format to numeric format.
        columns = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        rows = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1}

        # I try to convert it.
        try:
            new_column, new_row = position[0], position[1]
            x = columns[new_column]
            y = rows[new_row]

        # If it cannot be converted, I return False.
        except (KeyError, ValueError, TypeError, IndexError):
            print("\nIncorrect values.\n")
            return False
        
        # If I could, I return it.
        return x, y


# I execute the game.
if __name__ == "__main__":
    game = Game()
    game.main()