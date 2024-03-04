
from domain.Event import Event
from domain.Person import Person
from repository.EnrollFileRepository import EnrollFileRepository
from repository.EventFileRepository import EventFileRepository
from repository.PersonFileRepository import PersonFileRepository
from repository.dtoRepository import PersonEventRepository, EventNrRepository
from repository.enrollRepository import EnrollRepository
from repository.eventRepository import EventRepository
from repository.personRepository import PersonRepository
from service.dtoService import PersonEventService
from service.enrollService import EnrollService
from service.eventService import EventService
from service.personService import PersonService
from repository import dtoRepository
from service import dtoService
# from tests.tests import tests
from ui.console import Console


def main():
    personRepository = PersonFileRepository("person.txt")
    eventRepository = EventFileRepository("event.txt")
    enrollRepository = EnrollFileRepository("enroll.txt", personRepository, eventRepository)
    personService = PersonService(personRepository)
    eventService = EventService(eventRepository)
    person_event_repository = PersonEventRepository
    event_nr_repository = EventNrRepository
    personeventService = PersonEventService(person_event_repository,  event_nr_repository)
    enrollService = EnrollService(enrollRepository, personRepository, eventRepository)
    console = Console(personService, eventService, enrollService, personeventService)
    console.meniu()



# tests()
main()
