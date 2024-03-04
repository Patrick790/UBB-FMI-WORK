from unittest import TestCase

from domain.Event import Event
from domain.Person import Person
from exeption.exeption import RepoError
from repository.personRepository import PersonRepository
from service.personService import PersonService


class TestPersonService(TestCase):

    def setUp(self):
        self.PersonRepository = PersonRepository()
        self.persons = PersonService(self.PersonRepository)
        self.person1 = Person(5, "Ioana", "Tache")
        self.person2 = Person(6, "Adi", "Bucegi")
        self.event1 = Event(1, 2022 - 12 - 20, 3, "Christmas Party")
        self.event2 = Event(2, 2022 - 12 - 27, 1, "UNO")

    def test_add_person(self):
        self.assertEqual(self.persons.size(), 0)
        self.persons.add_person(5, "Ana", "Maniu")
        self.assertEqual(self.persons.size(), 1)
        try:
            self.persons.add_person(5, 'Ioana', 'Tache')
            assert False
        except RepoError as e:
            assert (str(e) == "There already is an entity with this id!")

    def test_get_all(self):
        self.persons.add_person(5, 'Ioana', 'Tache')
        list = []
        self.assertEqual(len(list), 0)
        list = self.persons.get_all_persons()
        self.assertEqual(len(list), 1)

    def test_modify_person(self):
        self.persons.add_person(1, "Ioana", "Tache")
        list = self.persons.get_all_persons()
        new_list = []
        for person in list:
            new_list.append(str(person))
        assert (str(new_list) == str(["Person1 : Ioana , Tache"]))
        self.persons.modify_person(1, "Pop", "Tache")
        list = self.persons.get_all_persons()
        new_list = []
        for person in list:
            new_list.append(str(person))
        assert (str(new_list) == "['Person1 : Pop , Tache']")
        try:
            self.persons.modify_person(3, 'Pop', 'Tache')
            assert False
        except RepoError as e:
            assert (str(e) == "Entity does not exist!")

    def test_delete_person(self):
        self.persons.add_person(1, "Ioana", "Tache")
        self.persons.delete_person(1)
        try:
            self.persons.delete_person(1)
            assert False
        except RepoError as e:
            assert (str(e) == "There is not an entity with this id!")

    def test_size(self):
        self.assertEqual(self.persons.size(), 0)
        self.persons.add_person(1, "Ioana", "Tache")
        self.assertEqual(self.persons.size(), 1)