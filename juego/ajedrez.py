from juego.tablero import *

# Esta es la fachada del juego, esta clase para lo único que sirve es para redirigir 
# parámetros y datos. Y para cambiar el turno de los jugadores.
class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "blanca"
        self.__lista_piezas__ = None
        self.__lista_instancias__ = None
        self.__lista_posibilidades__ = None

    # No hace falta mucha explicación de lo que hace esto, no?
    def cambiar_turno(self):
        self.__turno__ = "negra" if self.__turno__ == "blanca" else "blanca"

    # Esta función es la que se encarga de buscar las piezas que se pueden mover.
    def jugar(self):
        
        color = self.__turno__

        # Mando a buscar todo a la funcion obtener_piezas_movibles.
        self.__tablero__, lista_piezas, lista_instancias, lista_posibilidades = \
            self.__tablero__.obtener_piezas_movibles(color)
        
        # Guardo los datos en la clase.
        self.__lista_piezas__ = lista_piezas
        self.__lista_instancias__ = lista_instancias
        self.__lista_posibilidades__ = lista_posibilidades

        return self
    
    # Llamo a buscar el string que está en tablero.py.
    def imprimir_tablero_ajedrez(self):
        print(self.__tablero__.__str__())

    # Esta función es la que se encarga de mover las piezas.
    def mover_ajedrez(self, seleccion, nueva_posicion_str, \
                      nueva_posicion_int, vieja_posicion, posibilidades_finales):
        
        string_movimiento = self.__tablero__.mover_pieza(seleccion, nueva_posicion_str, \
                      nueva_posicion_int,vieja_posicion, posibilidades_finales)
        
        return self, string_movimiento

    # Esta función es la que se encarga de verificar si el juego terminó.
    def verificar_fin(self):
        return self.__tablero__.verificar_victoria()

            