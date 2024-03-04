import unittest
from unittest import TestCase

from domain.Person import Person
from exeption.exeption import RepoError
from repository.PersonFileRepository import PersonFileRepository
from repository.Repository import Repository



class TestPersonFileRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.repository = PersonFileRepository("person.txt")
        self.person = Person(8, "Ioana", "Tache")
        self.new_person = Person(9, "Adi", "Bucium")
        # self.personFileRepository = PersonFileRepository()
        # self.repository = Repository()
        # self.person1modified = Person(8, "Ionela", "Ionescu")

    def test_add_person(self):
        with self.assertRaises(RepoError):
            self.repository.add(self.person)
            self.repository.add(self.person)

    def test_modify(self):
        new_person = Person(6,"ana","ana")
        with self.assertRaises(RepoError):
            self.repository.modify(new_person)
        test_person = Person(7,"aaa","aaa")
        with self.assertRaises(RepoError):
            self.repository.add(test_person)
        new_test_person = Person(7,"BBB","ghj")
        self.repository.modify(new_test_person)

    def test_delete(self):
        with self.assertRaises(RepoError):
            self.repository.delete(self.person.get_id())
            self.repository.delete(self.person.get_id())

    def test_read_from_file(self):
        with self.assertRaises(RepoError):
            self.person = self.repository.modify(self.new_person)
        self.assertEqual(self.person.get_name(),"Ioana")

    def test_write_in_file(self):
        with self.assertRaises(RepoError):
            self.repository.add(self.person)
            self.repository.add(self.person)
        with open("person.txt", "r") as file:
            content = file.read()
        self.assertIn("Ioana", content)

    def tearDown(self) -> None:
        pass



