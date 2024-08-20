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
    def __init__(self, var, color, posicion, s, nom, vive = True):
        super().__init__(var, color, s)
        self.__posicion__ = posicion
        self.__vive__ = vive
        self.__nom__ = nom # Nombre de la pieza.

    # Para su uso en el método 'search' de la clase BD.
    def var(self):
        return self.__var__

    # Actualiza la posición de la pieza.
    def mover(self, nueva_posicion):
        self.__posicion__ = nueva_posicion


    # Función común para calcular movimientos basados en direcciones y movimientos individuales.
    def calcular_movimientos(self, posicion, movimientos, limite = False):
        # Calculo las posiciones posibles basadas en movimientos o direcciones dadas.
        # Si 'limite' es False, recorre todas las direcciones hasta que llegue al borde del tablero.
        # Si 'limite' es True, solo calcula un paso en la dirección dada.
        posiciones_posibles = []
        x, y = posicion

        for dx, dy in movimientos:
            nueva_x, nueva_y = x, y
            while True:
                nueva_x += dx
                nueva_y += dy
                if 1 <= nueva_x <= 8 and 1 <= nueva_y <= 8:
                    posiciones_posibles.append((nueva_x, nueva_y))
                    # Si el movimiento tiene un solo paso (como en Rey o Caballo).
                    if limite:  
                        break
                else:
                    break

        return posiciones_posibles


class Peon(Pieza):
    def __init__(self, var, color, posicion, s, nom, primera_posicion = True):
        super().__init__(var, color, posicion, s, nom)
        # Indica si es la primera vez que se mueve la pieza.
        self.__primera_posicion__ = primera_posicion  

    def movimientos_posibles(self):
        # Combino los movimientos de avance y captura para el peón.
        return self.movimientos_avance() + self.movimientos_captura()

    def movimientos_avance(self):
        posiciones_posibles = []
        x, y = self.__posicion__

        # Acá no uso la función 'calcular_movimientos' porque los movimientos son específicos.
        # Defino el avance según el color.
        avance_doble, avance_simple = (-2, -1) if self.__color__ == "blanca" else (2, 1)

        # Avance inicial de dos casillas.
        if self.__primera_posicion__ and 1 <= y + avance_doble <= 8:
            posiciones_posibles.append((x, y + avance_doble))

        # Avance simple.
        if 1 <= y + avance_simple <= 8:
            posiciones_posibles.append((x, y + avance_simple))

        return posiciones_posibles

    def movimientos_captura(self):
        # Defino los movimientos diagonales según el color.
        movimientos = [(-1, -1), (1, -1)] if self.__color__ == "blanca" else [(-1, 1), (1, 1)]
        # En este caso uso la función 'calcular_movimientos' con 'limite' en True.
        limite = True
        return self.calcular_movimientos(self.__posicion__, movimientos, limite)

    # La función mover, pero más específica para el peón. Ya que cambia el atributo 
    # 'primera_posicion'.
    def mover(self, nueva_posicion):
        self.__posicion__ = nueva_posicion
        self.__primera_posicion__ = False


class Caballo(Pieza):
    def movimientos_posibles(self):
        movimientos = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        limite = True
        return self.calcular_movimientos(self.__posicion__, movimientos, limite)


class Alfil(Pieza):
    def movimientos_posibles(self):
        direcciones = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        return self.calcular_movimientos(self.__posicion__, direcciones)


class Torre(Pieza):
    def movimientos_posibles(self):
        direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return self.calcular_movimientos(self.__posicion__, direcciones)


class Dama(Pieza):
    def movimientos_posibles(self):
        direcciones = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        return self.calcular_movimientos(self.__posicion__, direcciones)


class Rey(Pieza):
    def movimientos_posibles(self):
        movimientos = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        limite = True
        return self.calcular_movimientos(self.__posicion__, movimientos, limite)
