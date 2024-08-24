# I only use it to start Piece and Space.
class Space:
    def __init__(self, id, color, sw, sb):
        self.__color__ = color
        self.__sw__ = sw # Unicode white space symbol.
        self.__sb__ = sb # Unicode black space symbol.
        self.__id__ = id # Id of the thing that stores the box.

    # For use in the 'search' method of the DB class.
    def id(self):
        return self.__id__
    
    # To return the symbol of the box.
    def __str__(self):
        if self.__color__ == "white":
            return self.__sw__
        else:
            return self.__sb__


class Box(Space):
    def __init__(self, id, color, sw = u"\u25A1", sb = u"\u25A0"):
        super().__init__(id, color, sw, sb)


class Piece(Space):
    def __init__(self, id, color, position, name, sw, sb, lives = True):
        super().__init__(id, color, sw, sb)
        self.__position__ = position
        self.__name__ = name
        self.__lives__ = lives

    # It updates the position of the piece.
    def move(self, new_position):
        self.__position__ = new_position
        
    # Method base to get the possibilities of movements.
    def possible_movements(self):
        diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        non_diagonals = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        name = self.__name__

        if name == "Bishop":
            directions = diagonals
        elif name == "Rook":
            directions = non_diagonals
        elif name == "Queen":
            directions = diagonals + non_diagonals
        elif name == "King":
            directions = diagonals + non_diagonals
            limit = True
            return self.calculate_movements(self.__position__, directions, limit)
        
        return self.calculate_movements(self.__position__, directions)

    # Common function to calculate movements based on directions and individual movements.
    def calculate_movements(self, position, movements, limit = False):
        # I calculate the possible positions based on given movements or directions.
        # If 'limit' is False, it goes through all the directions until it reaches the edge of the board.
        # If 'limit' is True, it only calculates one step in the given direction.
        posible_positions = []
        x, y = position

        for dx, dy in movements:
            new_x, new_y = x, y
            while True:
                new_x += dx
                new_y += dy
                if 1 <= new_x <= 8 and 1 <= new_y <= 8:
                    posible_positions.append((new_x, new_y))
                    # If the movement has only one step (like in King or Knight).
                    if limit:  
                        break
                else:
                    break

        return posible_positions


class Pawn(Piece):
    def __init__(self, id, color, position, name, sw = u"\u2659", sb = u"\u265F", first_move = True):
        super().__init__(id, color, position, name, sw, sb)
        # It indicates if it is the first time the piece is moved.
        self.__first_move__ = first_move  


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


class Knight(Piece):
    def __init__(self, id, color, position, name, sw = u"\u2658", sb = u"\u265E"):
        super().__init__(id, color, position, name, sw, sb)
        
    # Función especializada para el caballo.
    def possible_movements(self):
        movements = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        limit = True
        return self.calculate_movements(self.__position__, movements, limit)


class Bishop(Piece):
    def __init__(self, id, color, position, name, sw = u"\u2657", sb = u"\u265D"):
        super().__init__(id, color, position, name, sw, sb)


class Rook(Piece):
    def __init__(self, id, color, position, name, sw = u"\u2656", sb = u"\u265C"):
        super().__init__(id, color, position, name, sw, sb)


class Queen(Piece):
    def __init__(self, id, color, position, name, sw = u"\u2655", sb = u"\u265B"):
        super().__init__(id, color, position, name, sw, sb)
        

class King(Piece):
    def __init__(self, id, color, position, name, sw = u"\u2654", sb = u"\u265A"):
        super().__init__(id, color, position, name, sw, sb)
