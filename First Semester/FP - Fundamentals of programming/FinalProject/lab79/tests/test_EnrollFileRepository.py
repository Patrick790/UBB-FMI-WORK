from unittest import TestCase

from domain.Enroll import Enroll
from domain.Event import Event
from domain.Person import Person
from exeption.exeption import RepoError
from repository.EnrollFileRepository import EnrollFileRepository
from repository.eventRepository import EventRepository
from repository.personRepository import PersonRepository


class TestEnrollFileRepository(TestCase):

    def setUp(self) ->None:
        self.person_repository = PersonRepository()
        self.event_repository = EventRepository()
        self.repository = EnrollFileRepository("enroll.txt", self.person_repository, self.event_repository)
        self.person1 = Person(1,"Ioana","Tache")
        self.person2 = Person(2, "Diana", "Bucium")
        self.event1= Event(11,"2022-12-20",2,"Uno")
        self.event2= Event(12,"2022-11-11",2,"Catan")
        self.enroll = Enroll(101,1,11)
        self.new_enroll = Enroll(102,1,12)

    def test_add(self):
        with self.assertRaises(RepoError):
            self.repository.add(self.enroll)

    def test_modify(self):
        with self.assertRaises(RepoError):
            self.enroll = self.repository.modify(self.new_enroll)

    def test_delete(self):
        with self.assertRaises(RepoError):
            self.repository.delete(self.enroll.get_id())
            self.repository.delete(self.enroll.get_id())

    def test_read_from_file(self):
        with self.assertRaises(RepoError):
            self.repository.add(self.enroll)

    def test_write_in_file(self):
        with self.assertRaises(RepoError):
            self.repository.add(self.enroll)
            self.repository.add(self.enroll)
