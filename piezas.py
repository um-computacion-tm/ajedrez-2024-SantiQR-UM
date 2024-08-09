# Solo la uso para iniciar Pieza y Espacio.
class Casilla:
    def __init__(self, var, color, s):
        self.__color__ = color
        self.__s__ = s # Símbolo unicode de la casilla.
        self.__var__ = var # Nombre de la variable que almacena la casilla.

    # Para su uso en el método 'search' de la clase BD.
    def var(self):
        return self.__var__


class Espacio(Casilla):
    pass


class Pieza(Casilla):
    def __init__(self, var, color, posicion, s, color_casilla, nom, vive = True):
        super().__init__(var, color, s)
        self.__posicion__ = posicion
        self.__color_casilla__ = color_casilla
        self.__vive__ = vive
        self.__nom__ = nom # Nombre de la pieza.

    # Para su uso en el método 'search' de la clase BD.
    def var(self):
        return self.__var__

    # Actualiza la posición de la pieza.
    def mover(self, nueva_posicion, nuevo_color_casilla):
        self.__posicion__ = nueva_posicion
        self.__color_casilla__ = nuevo_color_casilla


class Peon(Pieza):
    def __init__(self, var, color, posicion, s, color_casilla, nom, primera_posicion = True):
        super().__init__(var, color, posicion, s, color_casilla, nom)
        self.__primera_posicion__ = primera_posicion # Indica si es la primera vez que se mueve la pieza.
     
    def movimientos_posibles(self):
        # Lógica para los movimientos de los peones.
        posiciones_posibles = []
        x, y = self.__posicion__
        
        if self.__color__ == "blanca":

            # Movimiento hacia adelante (restar en la posición y).
            if self.__primera_posicion__:

                # Puede moverse 1 o 2 casillas hacia adelante si está en la posición inicial.
                if 1 <= y - 2 <= 8:
                    posiciones_posibles.append((x, y - 2))
                if 1 <= y - 1 <= 8:
                    posiciones_posibles.append((x, y - 1))

            else:
                # Puede moverse una casilla.
                if 1 <= y - 1 <= 8:
                    posiciones_posibles.append((x, y - 1))

            # Captura diagonal.
            if 1 <= x - 1 <= 8 and 1 <= y - 1 <= 8:
                posiciones_posibles.append((x - 1, y - 1))
            if 1 <= x + 1 <= 8 and 1 <= y - 1 <= 8:
                posiciones_posibles.append((x + 1, y - 1))

        elif self.__color__ == "negra":

            # Movimiento hacia adelante (sumar en la posición y).
            if self.__primera_posicion__:

                # Puede moverse 1 o 2 casillas hacia adelante si está en la posición inicial.
                if 1 <= y + 2 <= 8:
                    posiciones_posibles.append((x, y + 2))
                if 1 <= y + 1 <= 8:
                    posiciones_posibles.append((x, y + 1))

            else:
                # Puede moverse una casilla.
                if 1 <= y + 1 <= 8:
                    posiciones_posibles.append((x, y + 1))

            # Captura diagonal.
            if 1 <= x - 1 <= 8 and 1 <= y + 1 <= 8:
                posiciones_posibles.append((x - 1, y + 1))
            if 1 <= x + 1 <= 8 and 1 <= y + 1 <= 8:
                posiciones_posibles.append((x + 1, y + 1))
        
        return posiciones_posibles
    
    # El método esta repetido porque acá especificamente cambia el atributo 'primera_posicion'.
    def mover(self, nueva_posicion, nuevo_color_casilla):
        self.__posicion__ = nueva_posicion
        self.__color_casilla__ = nuevo_color_casilla
        self.__primera_posicion__ = False


class Caballo(Pieza):
    def movimientos_posibles(self):
        posiciones_posibles = []
        x, y = self.__posicion__
        
        movimientos = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dx, dy in movimientos:
            nueva_x, nueva_y = x + dx, y + dy
            if 1 <= nueva_x <= 8 and 1 <= nueva_y <= 8:
                posiciones_posibles.append((nueva_x, nueva_y))
        
        return posiciones_posibles


class Alfil(Pieza):
    def movimientos_posibles(self):
        posiciones_posibles = []
        x, y = self.__posicion__

        direcciones = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in direcciones:
            nueva_x, nueva_y = x, y
            while True:
                nueva_x += dx
                nueva_y += dy
                if 1 <= nueva_x <= 8 and 1 <= nueva_y <= 8:
                    posiciones_posibles.append((nueva_x, nueva_y))
                else:
                    break

        return posiciones_posibles


class Torre(Pieza):
    def movimientos_posibles(self):
        posiciones_posibles = []
        x, y = self.__posicion__

        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in direcciones:
            nueva_x, nueva_y = x, y
            while True:
                nueva_x += dx
                nueva_y += dy
                if 1 <= nueva_x <= 8 and 1 <= nueva_y <= 8:
                    posiciones_posibles.append((nueva_x, nueva_y))
                else:
                    break

        return posiciones_posibles


class Dama(Pieza):
    def movimientos_posibles(self):
        posiciones_posibles = []
        x, y = self.__posicion__

        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1),
                       (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in direcciones:
            nueva_x, nueva_y = x, y
            while True:
                nueva_x += dx
                nueva_y += dy
                if 1 <= nueva_x <= 8 and 1 <= nueva_y <= 8:
                    posiciones_posibles.append((nueva_x, nueva_y))
                else:
                    break

        return posiciones_posibles


class Rey(Pieza):
    def movimientos_posibles(self):
        posiciones_posibles = []
        x, y = self.__posicion__

        movimientos = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dx, dy in movimientos:
            nueva_x, nueva_y = x + dx, y + dy
            if 1 <= nueva_x <= 8 and 1 <= nueva_y <= 8:
                posiciones_posibles.append((nueva_x, nueva_y))

        return posiciones_posibles