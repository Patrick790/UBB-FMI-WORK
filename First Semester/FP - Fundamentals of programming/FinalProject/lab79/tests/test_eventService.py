
from unittest import TestCase

from domain.Event import Event
from exeption.exeption import RepoError
from repository.eventRepository import EventRepository
from service.eventService import EventService


class TestEventService(TestCase):

    def setUp(self):
        self.eventrepository = EventRepository()
        self.events = EventService(self.eventrepository)
        self.event1 = Event(1, 2022 - 12 - 27, 1, "UNO")

    def test_add_event(self):
        self.assertEqual(self.events.size(), 0)
        self.events.add_event(1, 2022 - 12 - 29, 6, "Catan")
        self.assertEqual(self.events.size(), 1)
        try:
            self.events.add_event(1, "2022-12-29", 6, "Catan")
            assert False
        except RepoError as e:
            assert (str(e) == "There already is an entity with this id!")

    def test_get_all(self):
        self.events.add_event(1, "2022-12-27", 1, "UNO")
        list = []
        self.assertEqual(len(list), 0)
        list = self.events.get_all_events()
        self.assertEqual(len(list), 1)

    def test_test_delete_events(self):
        self.events.add_event(1, "2022-12-27", 1, "UNO")
        self.assertEqual(self.events.size(), 1)
        self.events.delete_event(1)
        self.assertEqual(self.events.size(), 0)
        try:
            self.events.delete_event(3)
            assert False
        except RepoError as e:
            assert (str(e) == "There is not an entity with this id!")

    def test_modify_event(self):
        self.events.add_event(1, "2022-12-27", 1, "UNO")
        list = self.events.get_all_events()
        new_list = []
        for event in list:
            new_list.append(str(event))
        assert (str(new_list) == str(["Event 1 : 2022-12-27 , 1 , UNO"]))
        self.events.modify_event(1, "2022-12-30", 2, "Poker")
        list = self.events.get_all_events()
        new_list = []
        for event in list:
            new_list.append(str(event))
        assert (str(new_list) == str(["Event 1 : 2022-12-30 , 2 , Poker"]))
        try:
            self.events.modify_event(3, "2022-12-30", 2, "Poker")
            assert False
        except RepoError as e:
            assert (str(e) == "Entity does not exist!")
