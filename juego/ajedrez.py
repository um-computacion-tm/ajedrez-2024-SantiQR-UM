from juego.tablero import *

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "blanca"
        self.__lista_piezas__ = None
        self.__lista_instancias__ = None
        self.__lista_posibilidades__ = None
