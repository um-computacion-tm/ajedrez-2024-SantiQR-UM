from game.board import *

# This is the facade of the game, this class is only useful to redirect parameters and data.
# And to change the turn of the players.
class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "white"
        self.__pieces_list__ = None
        self.__instances_list__ = None
        self.__possibilities_list__ = None

    # There isnt much explanation needed for this, right?
    def change_turn(self):
        self.__turn__ = "black" if self.__turn__ == "white" else "white"

    # This function is responsible for finding the pieces that can be moved.
    def play(self):
        
        color = self.__turn__

        # I call the function to find all the pieces that can be moved.
        self.__board__, pieces_list, instances_list, possibilities_list = \
            self.__board__.obtain_movable_pieces(color)
        
        # I save the data in the class.
        self.__pieces_list__ = pieces_list
        self.__instances_list__ = instances_list
        self.__possibilities_list__ = possibilities_list

        return self
    
    # I call to search the string that is in board.py.
    def print_chess_board(self):
        print(self.__board__.__str__())

    # This function is responsible for moving the pieces.
    def move_chess(self, selection, new_position_str, \
                      new_position_int, old_position, final_possibilities):
        
        move_string = self.__board__.move_piece(selection, new_position_str, \
                      new_position_int, old_position, final_possibilities)
        
        return self, move_string

    # This function is responsible for verifying if the game is over.
    def check_end(self):
        return self.__board__.check_victory()

            