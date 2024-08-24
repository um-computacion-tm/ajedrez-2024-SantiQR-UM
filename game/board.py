from game.pieces import *
from game.database import *

class Board:
    def __init__(self):
        self.__board__, self.__DB_pieces__, self.__DB_boxes__ = self.create_initial_board()

    # Method to create the initial board.
    def create_initial_board(self):
        # I create the pieces and boxes:

        # White pieces.
        info_pieces = [
        ("P1" , "white", (1,7), "Pawn"), # ♙
        ("P2" , "white", (2,7), "Pawn"), # ♙
        ("P3" , "white", (3,7), "Pawn"), # ♙
        ("P4" , "white", (4,7), "Pawn"), # ♙
        ("P5" , "white", (5,7), "Pawn"), # ♙
        ("P6" , "white", (6,7), "Pawn"), # ♙
        ("P7" , "white", (7,7), "Pawn"), # ♙
        ("P8" , "white", (8,7), "Pawn"), # ♙
        ("H1" , "white", (2,8), "Knight"), # ♘
        ("H2" , "white", (7,8), "Knight"), # ♘
        ("B1" , "white", (3,8), "Bishop"), # ♗
        ("B2" , "white", (6,8), "Bishop"), # ♗
        ("R1" , "white", (1,8), "Rook"), # ♖
        ("R2" , "white", (8,8), "Rook"), # ♖
        ("Q1" , "white", (4,8), "Queen"), # ♕
        ("K1" , "white", (5,8), "King"), # ♔
        
        # Black pieces.
        ("p1" , "black", (1,2), "Pawn"), # ♟
        ("p2" , "black", (2,2), "Pawn"), # ♟
        ("p3" , "black", (3,2), "Pawn"), # ♟                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        ("p4" , "black", (4,2), "Pawn"), # ♟
        ("p5" , "black", (5,2), "Pawn"), # ♟
        ("p6" , "black", (6,2), "Pawn"), # ♟
        ("p7" , "black", (7,2), "Pawn"), # ♟
        ("p8" , "black", (8,2), "Pawn"), # ♟
        ("h1" , "black", (2,1), "Knight"), # ♞
        ("h2" , "black", (7,1), "Knight"), # ♞                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        ("b1" , "black", (3,1), "Bishop"), # ♝
        ("b2" , "black", (6,1), "Bishop"), # ♝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        ("r1" , "black", (1,1), "Rook"), # ♜
        ("r2" , "black", (8,1), "Rook"), # ♜
        ("q1" , "black", (4,1), "Queen"), # ♛
        ("k1" , "black", (5,1), "King") # ♚
        ]
        
        # Boxes.
        info_boxes = [
        ("W" , "white"), # White box □
        ("B" , "black") # Black box ■
        ]
        
        # I create the databases.
        DB_pieces = DB()
        DB_boxes = DB()
        
        # I add the pieces to the DB.
        for id, color, position, name in info_pieces:
            
            # I use globals() to get the class from the name (string) of the piece.
            piece_class = globals().get(name)
            
            if piece_class:
                piece = piece_class(id, color, position, name)
                DB_pieces.add(piece)
    
        # I add the boxes to the DB.
        for id, color in info_boxes:
            box = Box(id, color)
            DB_boxes.add(box)
        
        # I create the empty board.
        board = [[" " for _ in range(10)] for _ in range(10)]
        
        # I put the coordinates of the board.
        letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]
        for i in range(10):
            # The letters:
            board[0][i] = board[9][i] = letters[i]
            # The numbers:
            board[i][0] = board[i][9] = str(9 - i) if i > 0 and i < 9 else " "
        
        # I put the pieces on the board according to their position.
        for piece in DB_pieces.__data_base__.values():
            x, y = piece.__position__
            # Important: x and y are inverted because the board is a list of lists.
            board[y][x] = piece
        
        # I put the boxes in the empty spaces.
        for y in range(3, 7):
            for x in range(1, 9):
                # Here the same, x and y inverted!
                board[y][x] = DB_boxes.search('W' if (x + y) % 2 == 0 else 'B')
        
        # I return the board and the DBs for the interface.
        return board, DB_pieces, DB_boxes
    
    # Method to convert the board into a string.
    def __str__(self):
        board_string = "\n"
        for row in self.__board__:
            for space in row:
                # If it is a piece or a box, I show the symbol.
                if isinstance(space, Piece) or isinstance(space, Box):
                    board_string += (str(space.__str__()) + (" "))
                else:
                    board_string += (str(space) + (" "))
            board_string += ("\n")
        return board_string
    
    # Method to get the movable pieces.
    # It calls submethods.
    def obtain_movable_pieces(self, color):
        # I return a list of the names of the pieces that can move for the given color.
        # Then a list of the instances of those pieces.
        # And then I ask for the position to which you want to move.

        pieces_list = []  # List for the names of the pieces that I am going to show.
        instances_list = []  # List for the instances of the pieces that I am going to show.
        possibilities_list = []  # List for the possibilities of each of the pieces.

        # For the 16 pieces of the player:
        pieces = [
            (1, 8, "P", "p"),  # Pawns
            (9, 10, "H", "h"),  # Knights
            (11, 12, "B", "b"),  # Bishops
            (13, 14, "R", "r"),  # Rooks
            (15, 15, "Q", "q"),  # Queen
            (16, 16, "K", "k")  # King
        ]

        # For each of the 16 pieces:
        for num in range(1, 17):
            # I send to search the letter and the quantity of the piece according to its range.
            letter, count = self.get_letter_and_quantity(pieces, num, color)

            # I send to search the instances of the pieces.
            result, movable, possibilities = self.piece_instances\
                                            (self.__DB_pieces__, letter, count)

            # I append the pieces to the corresponding lists.
            if movable:
                if result.__name__ not in pieces_list:
                    pieces_list.append(result.__name__)
                if result not in instances_list:
                    instances_list.append(result)
                    possibilities_list.append(possibilities)

        # I return the board, the lists of pieces, instances and possibilities.
        return self, pieces_list, instances_list, possibilities_list

    # Method to get the letter and the quantity of the piece according to its range.
    def get_letter_and_quantity(self, pieces, num, color):
        for start, end, white_letter, black_letter in pieces:
            if start <= num <= end:
                count = num - start + 1
                letter = white_letter if color == "white" else black_letter
                return letter, count

    # Method to get the movable instances of the pieces.
    def piece_instances(self, DB_pieces, letter, num):
        
        # I use the 'search' method to review the DB of pieces, where the instances are,
        # delivering the id value (using the letter plus the piece number).
        piece = DB_pieces.search(letter + str(num))
        # I check if it can move.
        movable, possibilities = self.movable(piece)  
        
        # I return the instance of the piece, if it is movable (bool) and the possibilities.
        return piece, movable, possibilities
        
    # Primary method to check if a piece can move.
    # This calls submethods.
    def movable(self, piece):
        # I check if the piece is alive and get the possible moves.
        # Then, filter the possible moves according to the rules of the game.
        # Finally, I check if the path between the origin and the destination is free.
        lives, possibilities = self.check_lives_and_movements(piece)
        
        if not lives:
            return False, []
        
        possibilities_checked = self.filter_movements(piece, possibilities)
        possibilities_double_checked = self.check_free_path(piece, possibilities_checked)

        return bool(possibilities_double_checked), possibilities_double_checked

    # Part 1 of the method movable.
    def check_lives_and_movements(self, piece):
        # I check if the piece is alive. If it is not, I return False and an empty list.
        # If it is alive, I return True and the list of possible movements of the piece.
        if not piece.__lives__:
            return False, []
        
        return True, piece.possible_movements()

    # Part 2 of the method movable.
    def filter_movements(self, piece, possibilities):
        # I filter movements according to the rules of the game.
        possibilities_checked = []

        for position in possibilities:
            x, y = position
            
            # Although the verification is already done in the 'possible_movements' method, I do it
            # again just in case:
            if not (1 <= x <= 8 and 1 <= y <= 8):
                continue

            space = self.__board__[y][x]

            # First, if the piece is not a pawn:
            if not isinstance(piece, Pawn):
                # If the space is empty.
                if isinstance(space, Box):
                    possibilities_checked.append(position)
                # If the space has a piece of a different color.
                elif isinstance(space, Piece) and space.__color__ != piece.__color__:
                    possibilities_checked.append(position)
            # If the piece is a pawn:
            else:
                # I go to check according to the type of movement.
                if self.filter_vertical_pawn_movement(piece, x, y, space):
                    possibilities_checked.append(position)
                elif self.filter_diagonal_pawn_movement(piece, x, y, space):
                    possibilities_checked.append(position)

        return possibilities_checked

    # Part 1 of the method filter_movements.
    def filter_vertical_pawn_movement(self, pawn, x, y, space):
        # It checks if the vertical movement of the pawn is valid.
        # First, it checks if it is in the possibilities and then if it is empty.
        flag = True
        if abs(pawn.__position__[0] - x) != 0:
            flag = False
        if abs(pawn.__position__[1] - y) not in [1, 2]:
            flag = False
        if not isinstance(space, Box):
            flag = False
        return flag

    # Part 2 of the method filter_movements.
    def filter_diagonal_pawn_movement(self, pawn, x, y, space):
        # It checks if the diagonal movement of the pawn is valid.
        # First, it checks if it is in the possibilities and then if there is a piece of another color.
        flag = True
        if abs(pawn.__position__[0] - x) != 1:
            flag = False
        if abs(pawn.__position__[1] - y) != 1:
            flag = False
        if not isinstance(space, Piece):
            flag = False
        if space.__color__ == pawn.__color__:
            flag = False
        return flag

    # Part 3 of the method movable.
    def check_free_path(self, piece, possibilities_checked):
        # I verify if the path between the origin and the destination is free.
        possibilities_double_checked = []

        # For each of the positions:
        for position in possibilities_checked:
            # I send to check in the next function.
            if self.is_free_path(piece, position):
                possibilities_double_checked.append(position)

        return possibilities_double_checked

    # Part 1 of the method check_free_path.
    def is_free_path(self, piece, position):
        # Checks if the path is free for a specific piece.
        # If it is a knight, it directly returns True.
        if isinstance(piece, Knight):
            return True

        # Defines start and end.
        x_start, y_start = piece.__position__
        x_end, y_end = position

        # Defines the directions.
        dx = self.calculate_direction(x_start, x_end)
        dy = self.calculate_direction(y_start, y_end)

        # I send to check in the next function.
        parameters = (x_start, y_start, x_end, y_end, dx, dy)
        return self.check_free_boxes(parameters)

    # Part 2 of the method check_free_path.
    def calculate_direction(self, start, end):
        # It calculates the direction of the movement.
        # It returns 0 if the start and end are the same.
        if end == start:
            return 0
        return 1 if end > start else -1

    # Part 3 of the method check_free_path.
    def check_free_boxes(self, parameters):
        # It checks if all the boxes in the path are free.
        x_start, y_start, x_end, y_end, dx, dy = parameters

        # It defines where the advance is.
        x_advance, y_advance = x_start + dx, y_start + dy

        # While there isnt something, it keeps going.
        while x_advance != x_end or y_advance != y_end:
            # Si hay algo devuelve False.
            if isinstance(self.__board__[y_advance][x_advance], Piece):
                return False
            x_advance += dx
            y_advance += dy

        return True             

    # This is the method that is called to move a piece.
    def move_piece(self, piece, new_position_str, new_position_int, \
                    old_position, possibilities):
        # Here is the logic to move the piece.
        
        # I get the destination space.
        x, y = new_position_int
        target = self.__board__[y][x]

        x_vieja, y_vieja = old_position
        
        # I check if there is a piece in the target space.
        # If target is an instance of Piece, I say that it was captured.
        move_string = ""
        if isinstance(target, Piece):
            move_string += f"\nMovement made: {piece.__color__} {piece.__name__} {x_vieja}{y_vieja}"
            move_string += f" has captured {target.__color__} {target.__name__} in {new_position_str}\n"
        
            # I update the state of the captured piece.
            target.__lives__ = False
        # If it is an empty space.
        else:
            move_string += f"\nMovement made: {piece.__color__} {piece.__name__} {x_vieja}{y_vieja}"
            move_string += f" has moved to {new_position_str}\n"

        # I update the board with the new position of the piece.
        # I take out the old coordinates.
        x_actual, y_actual = piece.__position__
        # I restore the space with the corresponding box.
        self.__board__[y_actual][x_actual] = self.__DB_boxes__.search\
                                               ('W' if (x_actual + y_actual) % 2 == 0 else 'B')
        # I place the piece in its new position.
        self.__board__[y][x] = piece  

        # I update the attributes of the piece with the new position of the piece.
        piece.move((x, y))

        return move_string # I return the string with the movement made.

    # This is the main method to check if the game has ended.
    def check_victory(self):
        # I check if the game has ended.

        # If its a victory by pieces, 
        # I check if the king of each player is alive.
        end_string, white_pieces_alive, black_pieces_alive = self.victory_by_pieces()

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
    def victory_by_pieces(self):
        # I check if the king of each player is alive.
        white_king_alive = any(piece.__name__ == "King" and piece.__color__ == 'white' 
                    and piece.__lives__ for piece in self.__DB_pieces__.__data_base__.values())
        
        black_king_alive = any(piece.__name__ == "King" and piece.__color__ == 'black'
                    and piece.__lives__ for piece in self.__DB_pieces__.__data_base__.values())

        # I create the empty string.
        end_string = ""

        if not white_king_alive:
            end_string += "The player black has won by capturing the white king!"

        if not black_king_alive:
            end_string += "The white player has won by capturing the black king!"
        
        # I check each of the living pieces of each player
        white_pieces_alive = [piece for piece in self.__DB_pieces__.__data_base__.values() if \
                                piece.__color__ == 'white' and piece.__lives__]
        black_pieces_alive = [piece for piece in self.__DB_pieces__.__data_base__.values() if \
                                piece.__color__ == 'black' and piece.__lives__]

        # I return the victory message and the living pieces of each player.
        return end_string, white_pieces_alive, black_pieces_alive