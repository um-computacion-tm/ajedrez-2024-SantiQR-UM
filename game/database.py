# In the DB I store the instances of the pieces and the spaces to search them.
class DB():
    def __init__(self):
        self.__data_base__ = {}

    # Adds something to the BD, with key as its id, which is searched with id().
    def add(self, thing):
        self.__data_base__[str(thing.id())] = thing

    def search(self, id):
        return self.__data_base__[id]

