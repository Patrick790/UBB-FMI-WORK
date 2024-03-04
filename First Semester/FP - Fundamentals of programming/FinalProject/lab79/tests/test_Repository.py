from unittest import TestCase

from domain.Person import Person
from exeption.exeption import RepoError
from repository.personRepository import PersonRepository


class TestRepository(TestCase):
    def setUp(self):
        self.persons = PersonRepository()
        self.__person1 = Person(1,"Ioana","Tache")
        self.__person2 = Person(2,"Adi","Bucegi")
        self.persons.add(self.__person1)
        self.persons.add(self.__person2)

    def test_lenght(self):
        self.assertEqual(self.persons.__len__(), 2)

    def test_add_person(self):
        try:
            self.persons.add(self.__person1)
            assert False
        except RepoError as e:
            assert(str(e) == "There already is an entity with this id!")

    def test_modify(self):
        new_person = Person(1,"Diana","Tache")
        self.persons.modify(new_person)
        new_innexistent_person = Person(3,"Diana","Tache")
        try:
            self.persons.modify(new_innexistent_person)
            assert False
        except RepoError as e:
            assert (str(e) == "Entity does not exist!")

    def test_get_all(self):
        list = []
        self.assertEqual(len(list), 0)
        list = self.persons.get_all()
        self.assertEqual(len(list), 2)

    def test_delete(self):
        self.assertEqual(self.persons.__len__(), 2)
        self.persons.delete(1)
        # self.persons.delete(4)
        self.assertEqual(self.persons.__len__(), 1)
        try:
            self.persons.delete(1)
            assert False
        except RepoError as e:
            assert(str(e) == ("There is not an entity with this id!"))

    def test_get_by_id(self):
        id_person = self.__person2.get_id()
        self.assertEqual(self.persons.get_by_id(id_person), self.__person2)
        self.assertEqual(self.persons.get_by_id(1),self.__person1)
        self.assertEqual(self.persons.get_by_id(8), -1)
