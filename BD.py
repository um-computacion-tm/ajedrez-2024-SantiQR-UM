from piezas import Espacio

class BD():
    def __init__(self):
        self.__base_datos__ = {}

    # Añade una cosa a la BD, con key como su var, que lo busca con var().
    def add(self, cosa):
        self.__base_datos__[str(cosa.var())] = cosa

    def search(self, var):
        return self.__base_datos__[var]
    
    # Para buscar un espacio de un color dado y que devuelva su var.
    # Al final no se usa, pero si se quiere, puede usar esto.
    # def search_espacio(self, color):
    #     for key, obj in self.__base_datos__.items():
    #         if isinstance(obj, Espacio) and obj.__color__ == color:
    #             return obj.var()
