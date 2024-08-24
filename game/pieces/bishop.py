from game.pieces.pieces import Piece

class Bishop(Piece):

    # To return the bishop symbol.
    def __str__(self):
        return "♗" if self.__color__ == "white" else "♝"