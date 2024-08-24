from game.pieces.pieces import Piece

class King(Piece):

    # To return the king symbol.
    def __str__(self):
        return "♔" if self.__color__ == "white" else "♚"