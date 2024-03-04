from domain.Entity import Entity
class Person(Entity):

    def __init__(self, id, name, adress):
        super().__init__(id)
        self.__personID = id
        self.__name = name
        self.__adress = adress

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def set_name(self, name_new):
        self.__name = name_new

    def set_adress(self, adress_new):
        self.__adress = adress_new

    def __str__(self):
        return "Person" + str(self.get_id()) + " : " + str(self.get_name()) + " , " + str(self.get_adress())


