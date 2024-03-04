class PersonRepository:

    def __init__(self):
        self.all_persons = {}

    def get_all(self):
        '''
        da lista de persoane
        :return: o lista de obiecte de tipul persoana
        '''
        return list(self.all_persons.values())

    def adauga(self, person):
        '''
        adauga o persoana
        :param person: obiect de tipul Persoana
        :return:
        '''
        if person.get_personID() in self.all_persons:
            raise KeyError("There is already a person with the same id!")
        self.all_persons[person.get_personID()] = person

    def find_person_after_id(self, personID):
        '''
        cauta angajatul dupa id
        :param personID: string
        :return: un angajat, daca exista unul cu id-ul dat sau -1 in caz contrar
        '''
        if personID in self.all_persons:
            return self.all_persons[personID]

    def modifica(self, new_person):
        '''
        modifica persoana de la id-ul dat
        :param new_person: persoana modificata
        :return:
        '''
        if new_person.get_personID() not in self.all_persons:
            raise KeyError("There is no person with the given id!")
        self.all_persons[new_person.get_personID()] = new_person



    def delete(self, personID):
        '''
        sterge un element dupa id
        :param personID: id-ul persoanei pe care dorim sa o stergem
        :return:
        '''
        if personID not in self.all_persons:
            raise KeyError("There is no person with the given id")
        del self.all_persons[personID]