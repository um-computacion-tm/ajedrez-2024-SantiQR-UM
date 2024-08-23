# En la BD almaceno las instancias de pieza y los espacios para buscarlos.
class BD():
    def __init__(self):
        self.__base_datos__ = {}

    # Añade una cosa a la BD, con key como su id, que lo busca con id().
    def add(self, cosa):
        self.__base_datos__[str(cosa.id())] = cosa

    def search(self, id):
        return self.__base_datos__[id]

