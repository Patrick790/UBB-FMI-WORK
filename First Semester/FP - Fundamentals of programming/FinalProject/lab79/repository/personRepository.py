from repository.Repository import Repository

class PersonRepository(Repository):

    def __init__(self):
        super().__init__()

    def get_person_by_id(self, id):
        for i in range (0, len(self._list)):
            current_person = self._list[i]
            if current_person.get_id() == id:
                return current_person
        return -1

    def get_by_name(self, name):
        for i in range(0, len(self._list)):
            current_entity = self._list[i]
            if current_entity.get_name() == name:
                return current_entity
        return -1

    # def get_all(self):
    #     '''
    #     da lista de persoane
    #     :return: o lista de obiecte de tipul persoana
    #     '''
    #     return self.__all_persons
    #
    # def adauga(self, person):
    #     '''
    #     adauga o persoana
    #     :param person: obiect de tipul Persoana
    #     :return:
    #     '''
    #     if self.find_person_after_id(person.get_personID()) != -1:
    #         raise KeyError("There is already a person with the same id!")
    #     else:
    #         self.__all_persons.append(person)

    # def find_person_after_id(self, persID):
    #     '''
    #     cauta angajatul dupa id
    #     :param personID: string
    #     :return: un angaja, daca exista unul cu id-ul dat sau -1 in caz contrar
    #     '''
    #     for i in range (0, len(self.__all_persons)):
    #         current_person = self.__all_persons[i]
    #         if current_person.get_personID() == persID:
    #             return i
    #     return -1

    # def get_person_by_name(self, name):
    #     for i in range(0, len(self.__all_persons)):
    #         current_person = self.__all_persons[i]
    #         if current_person.get_name() == name:
    #             return current_person
    #     return -1
    #
    # def modifica(self, new_person):
    #     if self.find_person_after_id(new_person.get_personID()) == -1:
    #         raise KeyError("There isn't a person with the given id")
    #     i = self.find_person_after_id(new_person.get_personID)
    #     self.__all_persons[i]=new_person
    #
    #
    # def delete(self, personID):
    #     '''
    #     sterge un element dupa id
    #     :param personID:
    #     :return:
    #     '''
    #     if self.find_person_after_id(personID) == -1:
    #         raise KeyError("There is no person with the given id")
    #     else:
    #         i = self.find_person_after_id(personID)
    #         current_person = self.__all_persons[i]
    #         self.__all_persons.remove(current_person)
