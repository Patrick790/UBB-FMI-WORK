from domain.person import Person
from infrastructura.personRepository import PersonRepository


class PersonService:

    def __init__(self, personRepository: PersonRepository):
        self.personRepository = personRepository

    def get_all_persons(self):
        '''
        da toata lista de persoane
        :return: o lista de obiecte de tipul Person
        '''
        return self.personRepository.get_all()

    def add_person(self, personID, name, adress):
        '''
        adauga o persoana
        :param personID: int
        :param name: string
        :param adress: string
        :return:
        '''
        person = Person(personID, name, adress)
        self.personRepository.adauga(person)

    def modify_person(self, personID, new_name, new_adress):
        '''
        modifica o persoana
        :param personID: id-ul persoanei pe care dorim sa o modificam
        :param new_name: noul nume al persoanei
        :param new_adress: noua adresa a persoanei
        :return:
        '''
        person = Person(personID, new_name, new_adress)
        self.personRepository.modifica(person)

    def delete_person(self, personID):
        '''
        sterge persoana dupa id
        :param personID: id-ul persoanei pe care dorim sa o stergem
        :return:
        '''
        self.personRepository.delete(personID)