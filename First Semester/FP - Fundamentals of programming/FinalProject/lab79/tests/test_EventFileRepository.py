from unittest import TestCase

from domain.Event import Event
from exeption.exeption import RepoError
from repository.EventFileRepository import EventFileRepository


class TestEventFileRepository(TestCase):
    def setUp(self):
        self.repository = EventFileRepository("event.txt")
        self.event = Event(14,"2022-12-27",1,"UNO")
        self.new_event = Event(15,"2022-12-20",2,"Catan")

    def test_add(self):
        with self.assertRaises(RepoError):
            self.repository.add(self.event)

    def test_modify(self):
        new_event = Event(16, "ana",1, "ana")
        with self.assertRaises(RepoError):
            self.repository.modify(new_event)
        test_event = Event(17, "aaa",2, "aaa")
        with self.assertRaises(RepoError):
            self.repository.add(test_event)
        new_test_event = Event(17, "BBB",3, "ghj")
        self.repository.modify(new_test_event)
        # self.event = self.repository.modify(self.new_event)

    def test_delete(self):
        with self.assertRaises(RepoError):
            self.repository.delete(self.event.get_id())
            self.repository.delete(self.event.get_id())

    def test_read_from_file(self):
        with self.assertRaises(RepoError):
            self.repository.modify(self.event)

    def test_write_in_file(self):
        with self.assertRaises(RepoError):
            self.repository.add(self.event)
            self.repository.add(self.event)

