# Solo la uso para iniciar Pieza y Espacio.
class Casilla:
    def __init__(self, id, color, sb, sn):
        self.__color__ = color
        self.__sb__ = sb # Símbolo unicode blanco de la casilla.
        self.__sn__ = sn # Símbolo unicode negro.
        self.__id__ = id # Nombre de la variable que almacena la casilla.

    # Para su uso en el método 'search' de la clase BD.
    def id(self):
        return self.__id__
    
    # Para devolver el símbolo de la casilla.
    def __str__(self):
        if self.__color__ == "blanca":
            return self.__sb__
        else:
            return self.__sn__


class Espacio(Casilla):
    def __init__(self, id, color, sb = u"\u25A1", sn = u"\u25A0"):
        super().__init__(id, color, sb, sn)


class Pieza(Casilla):
    def __init__(self, id, color, posicion, nom, sb, sn, vive = True):
        super().__init__(id, color, sb, sn)
        self.__posicion__ = posicion
        self.__nom__ = nom # Nombre de la pieza.
        self.__vive__ = vive
        
    # Para su uso en el método 'search' de la clase BD.
    def id(self):
        return self.__id__

    # Actualiza la posición de la pieza.
    def mover(self, nueva_posicion):
        self.__posicion__ = nueva_posicion
        
    # Método base para obtener las posibilidades de movimientos.
    def movimientos_posibles(self):
        diagonales = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        horizontales = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        nombre = self.__nom__

        if nombre == "Alfil":
            direcciones = diagonales
        elif nombre == "Torre":
            direcciones = horizontales
        elif nombre == "Dama":
            direcciones = diagonales + horizontales
        elif nombre == "Rey":
            direcciones = diagonales + horizontales
            limite = True
            return self.calcular_movimientos(self.__posicion__, direcciones, limite)
        
        return self.calcular_movimientos(self.__posicion__, direcciones)

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
    def __init__(self, id, color, posicion, nom, sb = u"\u2659", sn = u"\u265F", primera_posicion = True):
        super().__init__(id, color, posicion, nom, sb, sn)
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
    def __init__(self, id, color, posicion, nom, sb = u"\u2658", sn = u"\u265E"):
        super().__init__(id, color, posicion, nom, sb, sn)
        
    # Función especializada para el caballo.
    def movimientos_posibles(self):
        movimientos = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        limite = True
        return self.calcular_movimientos(self.__posicion__, movimientos, limite)


class Alfil(Pieza):
    def __init__(self, id, color, posicion, nom, sb = u"\u2657", sn = u"\u265D"):
        super().__init__(id, color, posicion, nom, sb, sn)


class Torre(Pieza):
    def __init__(self, id, color, posicion, nom, sb = u"\u2656", sn = u"\u265C"):
        super().__init__(id, color, posicion, nom, sb, sn)


class Dama(Pieza):
    def __init__(self, id, color, posicion, nom, sb = u"\u2655", sn = u"\u265B"):
        super().__init__(id, color, posicion, nom, sb, sn)
        

class Rey(Pieza):
    def __init__(self, id, color, posicion, nom, sb = u"\u2654", sn = u"\u265A"):
        super().__init__(id, color, posicion, nom, sb, sn)
