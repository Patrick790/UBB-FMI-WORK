from dataclasses import dataclass

@dataclass
class PersonEventDTO:
    name: str
    nr_events: int

@dataclass
class EventNrDTO:
    description: str
    nr_enrolls: int

class PersonEventDTOAssembler:
    @staticmethod
    def create_person_dto(person,enrolls):
        name = person.get_name()
        nr_events = 0
        for enroll in enrolls:
            if person.get_id() == enroll.get_personID():
                nr_events += 1
        return PersonEventDTO(name,nr_events)

class EventNrDTOAssembler:
    @staticmethod
    def create_event_dto(event,enrolls):
        description = event.set_description()
        nr_enrolls = 0
        for enroll in enrolls:
            if event.get_id() == enroll.get_evenId():
                nr_enrolls += 1
        return EventNrDTOAssembler(description,nr_enrolls)


