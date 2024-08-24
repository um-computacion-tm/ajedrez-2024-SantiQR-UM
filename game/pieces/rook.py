from game.pieces.pieces import Piece

class Rook(Piece):

    # To return the rook symbol.
    def __str__(self):
        return "♖" if self.__color__ == "white" else "♜"