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

    @property
    def board(self):
        return self.__board__
    
    @property
    def turn(self):
        return self.__turn__
    
    @property
    def pieces_list(self):
        return self.__pieces_list__
    
    @property
    def instances_list(self):
        return self.__instances_list__
    
    @property
    def possibilities_list(self):
        return self.__possibilities_list__

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
        return Rules.check_victory(self.__board__)



class Rules:
    # This is the main method to check if the game has ended.
    @staticmethod
    def check_victory(self):
        # I check if the game has ended.

        # If its a victory by pieces, 
        # I check if the king of each player is alive.
        end_string, white_pieces_alive, black_pieces_alive = Rules.victory_by_pieces(self)

        if end_string != "":
            return end_string

        # If its a victory by movements, 
        # I check if there is at least one possible movement for each player.
        white_movements = any(self.movable(piece)[0] for piece in white_pieces_alive)
        black_movements = any(self.movable(piece)[0] for piece in black_pieces_alive)

        if not white_movements and not black_movements:
            end_string += "Draw by movements!"

        elif not white_movements:
            end_string += "The player black has won by movements!"

        elif not black_movements:
            end_string += "The player white has won by movements!"

        return end_string # I return the string with the end of the game.
    
    # Submethod of check_victory
    @staticmethod
    def victory_by_pieces(self):
        # I check if the king of each player is alive.
        white_king_alive = Rules.king_alive(self, 'white') 
        black_king_alive = Rules.king_alive(self, 'black') 

        # I create the empty string.
        end_string = ""

        if not white_king_alive:
            end_string += "The player black has won by capturing the white king!"

        if not black_king_alive:
            end_string += "The white player has won by capturing the black king!"
        
        # I check each of the living pieces of each player
        white_pieces_alive = Rules.pieces_alive(self, 'white')
        black_pieces_alive = Rules.pieces_alive(self, 'black')

        # I return the victory message and the living pieces of each player.
        return end_string, white_pieces_alive, black_pieces_alive
    
    @staticmethod
    def king_alive(self, color):
        return True if any(piece.name == "King" and piece.color == color \
                    and piece.lives for piece in self.__DB_pieces__.data_base.values())\
        else False
    
    @staticmethod
    def pieces_alive(self, color):
        return [piece for piece in self.__DB_pieces__.data_base.values() if \
                                piece.color == color and piece.lives]