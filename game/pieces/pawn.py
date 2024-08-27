from game.pieces.pieces import Piece

class Pawn(Piece):
    def __init__(self, id, color, position, name, first_move = True):
        super().__init__(id, color, position, name)
        # It indicates if it is the first time the piece is moved.
        self.__first_move__ = first_move  

    @property
    def first_move(self):
        return self.__first_move__
    
    # To return the symbol of the box.
    __white_str__ = "♙"
    __black_str__ = "♟"


    def possible_movements(self):
        # I combine the advance and capture movements for the pawn.
        return self.advance_movements() + self.capture_movements()


    def advance_movements(self):
        posible_positions = []
        x, y = self.__position__
        
        # Here I don't use the 'calculate_movements' function because the movements are specific.
        # I define the advance according to the color.
        doble_advance, simple_advance = (-2, -1) if self.__color__ == "white" else (2, 1)

        # If first move is True, it can move two squares.
        if self.__first_move__ and 1 <= y + doble_advance <= 8:
            posible_positions.append((x, y + doble_advance))

        # Simple advance.
        if 1 <= y + simple_advance <= 8:
            posible_positions.append((x, y + simple_advance))

        return posible_positions


    def capture_movements(self):
        # I define the diagonal movements according to the color.
        movements = [(-1, -1), (1, -1)] if self.__color__ == "white" else [(-1, 1), (1, 1)]
        # In this case I use the 'calculate_movements' function with 'limit' as True.
        limit = True
        return self.calculate_movements(self.__position__, movements, limit)


    # The move function, but more specific for the pawn. Since it changes the attribute
    # 'first_move'.
    def move(self, new_position):
        self.__position__ = new_position
        self.__first_move__ = False