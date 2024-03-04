from domain.Entity import Entity


class Enroll(Entity):

    def __init__(self, id, personID, evenId):
        super().__init__(id)
        self.__id = id
        self.__personID = personID
        self.__evenId = evenId

    def get_personID(self):
        return self.__personID

    def get_evenId(self):
        return self.__evenId

    def set_personID(self, new_personID):
        self.__personID = new_personID

    def set_evenId(self, new_evenId):
        self.__evenId = new_evenId

    def __str__(self):
        return "Enroll: " + str(self.get_id()) + "\n" + "Person ID: " + str(self.get_personID()) + "\n" + "Event ID: " + str(self.get_evenId())


