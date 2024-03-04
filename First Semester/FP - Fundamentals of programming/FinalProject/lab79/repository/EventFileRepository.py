from domain.Event import Event
from repository.eventRepository import EventRepository


class EventFileRepository(EventRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.read_from_file()

    def add(self, person):
        super().add(person)
        self.write_in_file()

    def modify(self, person):
        super().modify(person)
        self.write_in_file()

    def delete(self, id):
        super().delete(id)
        self.write_in_file()

    def read_from_file(self):
        try:
            f = open(self.__file_name, "r")
            line = f.readline().strip("\n")
            while line != "":
                attributes_list = line.split(",")
                id = int(attributes_list[0])
                date = attributes_list[1]
                time = attributes_list[2]
                description = attributes_list[3]
                event = Event(id, date, time, description)
                super().add(event)
                line = f.readline().strip("\n")
            f.close()
        except IOError:
            print("Error at the opening of the file " + self.__file_name)

    def write_in_file(self):
        try:
            f = open(self.__file_name, "w")
            all_events = super().get_all()
            for event in all_events:
                id = event.get_id()
                date = event.get_date()
                time = event.get_time()
                description = event.get_description()
                line = str(id) + "," + str(date) + "," + str(int(time)) + "," + str(description) + "\n"
                f.write(line)
            f.close()
        except IOError:
            print("Error at the closure of the file" + self.__file_name)





