
class Entity:

    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id
        
    def __str__(self):
        return "ID" + str(self.get_id()) + "\n"