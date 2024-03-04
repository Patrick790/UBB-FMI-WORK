from domain.Enroll import Enroll
from repository.enrollRepository import EnrollRepository


class EnrollFileRepository(EnrollRepository):
    def __init__(self, file_name, personRepository, enrollRepository):
        super().__init__(personRepository, enrollRepository)
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
            personID = int(attributes_list[1])
            evenId = int(attributes_list[2])
            enroll = Enroll(id, personID, evenId)
            super().add(enroll)
            line = f.readline().strip("\n")
        f.close()

    def write_in_file(self):
        f = open(self.__file_name, "w")
        all_enrolls = super().get_all()
        for enroll in all_enrolls:
            id = enroll.get_id()
            personID = enroll.get_personID()
            evenId = enroll.get_evenId()
            line = str(id) + "," + str(personID) + "," + int(evenId) + "\n"
            f.write(line)
        f.close()





