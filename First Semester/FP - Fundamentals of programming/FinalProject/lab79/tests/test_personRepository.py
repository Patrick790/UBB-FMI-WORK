from unittest import TestCase

from domain.Person import Person
from repository.personRepository import PersonRepository


class TestPersonRepository(TestCase):

    def setUp(self):
        self.persons = PersonRepository()
        self.__person1 = Person(1,"Ioana","Tache")
        self.__person2 = Person(2,"Adi","Bucegi")
        self.persons.add(self.__person1)
        self.persons.add(self.__person2)

    def test_get_person_by_id(self):
        id_person = self.__person2.get_id()
        self.assertEqual(self.persons.get_person_by_id(id_person), self.__person2)
        self.assertEqual(self.persons.get_person_by_id(5), -1)
        self.assertEqual(self.persons.get_person_by_id(1), self.__person1)

    def test_get_by_name(self):
        person_name = self.__person1.get_name()
        self.assertEqual(self.persons.get_by_name(person_name), self.__person1)
        self.assertEqual(self.persons.get_by_name("qwer"), -1)
