from unittest import TestCase

from domain.Event import Event
from repository.eventRepository import EventRepository


class TestEventRepository(TestCase):

    def setUp(self):
        self.events = EventRepository()
        self.event1 = Event(1, 2022 - 12 - 20, 3, "Christmas Party")
        self.event2 = Event(2, 2022 - 12 - 27, 1, "UNO")
        self.events.add(self.event1)
        self.events.add(self.event2)

    def test_get_event_by_id(self):
        event_id = self.event1.get_id()
        self.assertEqual(self.events.get_event_by_id(event_id), self.event1)
        self.assertEqual(self.events.get_event_by_id(4), -1)
