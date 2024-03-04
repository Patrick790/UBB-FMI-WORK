from domain.Event import Event
from repository.eventRepository import EventRepository


class EventService:

    def __init__(self, eventRepository: EventRepository):
        self.__eventRepository = eventRepository

    def get_all_events(self):
        '''
        function that return the list of events
        '''
        return self.__eventRepository.get_all()

    def add_event(self, evenid, date,time, description):
        event = Event(evenid, date,time, description)
        self.__eventRepository.add(event)

    def delete_event(self, Evenid):
        self.__eventRepository.delete(Evenid)

    def modify_event(self, EvenId, new_date, new_time, new_description):
        new_event = Event(EvenId, new_date, new_time, new_description)
        self.__eventRepository.modify(new_event)

    def size(self):
        return self.__eventRepository.__len__()