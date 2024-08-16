from juego.tablero import *

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "blanca"
        self.__lista_piezas__ = None
        self.__lista_instancias__ = None
        self.__lista_posibilidades__ = None

    def cambiar_turno(self):
        self.__turno__ = "negra" if self.__turno__ == "blanca" else "blanca"

    def jugar(self):
        
        color = self.__turno__

        # Acá está la lógica para mover piezas
        self.__tablero__, lista_piezas, lista_instancias, lista_posibilidades = \
            self.__tablero__.obtener_piezas_movibles(color)
        
        self.__lista_piezas__ = lista_piezas
        self.__lista_instancias__ = lista_instancias
        self.__lista_posibilidades__ = lista_posibilidades

        return self