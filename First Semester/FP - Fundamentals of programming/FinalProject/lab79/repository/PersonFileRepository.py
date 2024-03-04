from domain.Person import Person
from repository.personRepository import PersonRepository


class PersonFileRepository(PersonRepository):
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
        f = open(self.__file_name, "r")
        line = f.readline().strip("\n")
        while line != "":
            attributes_list = line.split(",")
            id = int(attributes_list[0])
            name = attributes_list[1]
            adress = attributes_list[2]
            person = Person(id, name, adress)
            super().add(person)
            line = f.readline().strip("\n")
        f.close()

    def write_in_file(self):
        f = open(self.__file_name, "w")
        all_persons = super().get_all()
        for person in all_persons:
            id = person.get_id()
            name = person.get_name()
            adress = person.get_adress()
            line = str(id) + "," + name + "," + adress + "\n"
            f.write(line)
        f.close()




