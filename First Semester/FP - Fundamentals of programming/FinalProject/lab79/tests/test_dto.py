import unittest
from domain import Person, Event, Enroll
from domain.dto import EventNrDTO
from repository import eventRepository

from repository.Repository import Repository
from repository import personRepository
from repository import enrollRepository
from repository import dtoRepository
class TestPersonEventDTOAssembler(unittest.TestCase):
    def _init_(self, methodName: str = ...):
        super().__init__(methodName)
        self.PersonEventDTO = None

    def setUp(self):
        self.nr_event = 0
        self.dto_event = EventNrDTo("UNO",2)
        self.dto_person = Person("Ioana",2)
        self.person = Person(1,"Ioana","Tache")
        self.event = Event(14,"2022-12-27",1,"UNO")
        self.enroll = Enroll(101,1,14)
        self.repository = Repository()
        self.eventRepository = eventRepository()
        self.eventRepository.add(self.event)
        self.personRepository = personRepository()
        self.personRepository.add(self.person)
        self.enrollRepository = enrollRepository(self.personRepository, self.eventRepository)
        self.enrolls = self.enroll.get_all()


