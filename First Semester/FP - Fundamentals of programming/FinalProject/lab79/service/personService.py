from domain.Person import Person
from repository.personRepository import PersonRepository


class PersonService:

    def __init__(self, personRepository: PersonRepository):
        self.__personRepository = personRepository

    def get_all_persons(self):
        '''
        da toata lista de persoane
        :return: o lista de obiecte de tipul Person
        '''
        return self.__personRepository.get_all()

    def add_person(self, personID, name, adress):
        '''
        adauga o persoana
        :param personID: sting
        :param name: string
        :param adress: string
        :return:
        '''
        person = Person(personID, name, adress)
        self.__personRepository.add(person)

    def modify_person(self, personID, new_name, new_adress):
        person = Person(personID, new_name, new_adress)
        self.__personRepository.modify(person)

    def delete_person(self, personID):
        self.__personRepository.delete(personID)

    def size(self):
        return self.__personRepository.__len__()



