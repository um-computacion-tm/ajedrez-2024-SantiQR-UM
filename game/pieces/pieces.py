from game import COLOR_WHITE
# I only use it to start Piece and Space.
class Space:
    def __init__(self, id, color):
        self.__color__ = color
        self.__id__ = id # Id of the thing that stores the box.

    @property
    def color(self):
        return self.__color__

    # For use in the 'search' method of the DB class.
    @property
    def id(self):
        return self.__id__
    
    def __str__(self):
        return self.__white_str__ if self.__color__ == COLOR_WHITE else self.__black_str__


class Box(Space):
    def __init__(self, id, color):
        super().__init__(id, color)

    # To return the symbol of the box.
    __white_str__ = "□"
    __black_str__ = "■"


class Piece(Space):
    def __init__(self, id, color, position, name, lives = True):
        super().__init__(id, color)
        self.__position__ = position
        self.__name__ = name
        self.__lives__ = lives

    @property
    def position(self):
        return self.__position__
    
    @property
    def name(self):
        return self.__name__
    
    @property
    def lives(self):
        return self.__lives__
    
    def kill(self):
        self.__lives__ = False

    # It updates the position of the piece.
    def move(self, new_position):
        self.__position__ = new_position
        
    # Method base to get the possibilities of movements.
    def possible_movements(self):        
        return self.calculate_movements(self.__position__, self.directions)

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