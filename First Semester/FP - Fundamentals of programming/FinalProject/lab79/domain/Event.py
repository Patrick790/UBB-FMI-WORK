# <ID>, <dată>, <timp>, <descriere>
from domain.Entity import Entity


class Event(Entity):

    def __init__(self, id, date, time, description):
        super().__init__(id)
        self.__evenid = id
        self.__date = date
        self.__time = time
        self.__description = description

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    def set_date(self, date):
        self.__date = date

    def set_time(self, new_time):
        self.__time = new_time

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return "Event " + str(self.get_id()) + " : " + str(self.get_date()) + " , " + str(self.get_time()) + " , " + str(self.get_description())
