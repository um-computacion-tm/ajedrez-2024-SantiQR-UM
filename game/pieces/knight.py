from game.pieces.pieces import Piece

class Knight(Piece):
    # To return the symbol of the box.
    __white_str__ = "♘"
    __black_str__ = "♞"

    # Función especializada para el caballo.
    def possible_movements(self):
        movements = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        limit = True
        return self.calculate_movements(self.__position__, movements, limit)