from game.pieces.pieces import Piece

class Queen(Piece):
        
    # To return the queen symbol.
    def __str__(self):
        return "♕" if self.__color__ == "white" else "♛"