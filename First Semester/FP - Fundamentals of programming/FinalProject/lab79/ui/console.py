from datetime import datetime
from service import *
from service.dtoService import PersonEventService
from service.enrollService import EnrollService
from service.personService import PersonService
from service.eventService import EventService

class Console:
    def __init__(self, personService: PersonService, eventService: EventService, enrollService: EnrollService, personeventService):
        self.__personService = personService
        self.__eventService = eventService
        self.__enrollService = enrollService
        self.__personEventService = personeventService

    def add_person(self):
        try:
            personID = int(input("Enter the person id: "))
            name = input("Enter the name of the person: ")
            adress = input("Enter the adress of the person: ")
            self.__personService.add_person(personID, name, adress)
        except ValueError:
            print("Invalid input, try again")
        except KeyError as ke:
            print(ke)

    def modify_person(self):
        try:
            personID = int(input("Enter the id of the person you want to modify: "))
            new_name = input("Enter the new name of the person: ")
            new_adress = input("Enter the new adress of the person: ")
            self.__personService.modify_person(personID, new_name, new_adress)
        except KeyError as e:
            print(e)

    def delete_person(self):
        try:
            personID = int(input("Enter the id of the person you want to remove: "))
            self.__personService.delete_person(personID)
        except KeyError as e:
            print(e)

    def print_persons(self):
        all_persons = self.__personService.get_all_persons()
        if len(all_persons) == 0:
            print("List is empty")
        for person in all_persons:
            print(person)

    def add_event(self):
        try:
            eventid = int(input("Enter the id of the event : "))
            str_date = str(input("Enter the date and time (yyyy-mm-dd) "))
            date = datetime.strptime(str_date, "%Y-%m-%d")
            time = int(input("Enter the duration of the event: "))
            description = input("Enter the description of the event: ")
            self.__eventService.add_event(eventid, date, time, description)
        except ValueError:
            print("Invalid input, try again")
        except KeyError as ke:
            print(ke)

    def print_events(self):
        all_events = self.__eventService.get_all_events()
        if len(all_events) == 0:
            print("List is empty")
        for event in all_events:
            print(event)

    def modify_event(self):
        try:
            evenid = int(input("Enter the id of the event you want to modify: "))
            str_date = str(input("Enter the new date and time (yyyy-mm-dd) "))
            date = datetime.strptime(str_date, "%Y-%m-%d")
            time = int(input("Enter the new duration of the event: "))
            description = str(input("Enter the new description of the event: "))
            self.__eventService.modify_event(evenid, date, time, description)
        except KeyError as e:
            print (e)

    def delete_event(self):
        try:
            evenid = int(input("Enter the id of the event you want too delete: "))
            self.__eventService.delete_event(evenid)
        except KeyError as e:
            print(e)

    def print_enrolls(self):
        enrolls = self.__enrollService.get_all()
        if len(enrolls) == 0:
            print("List is empty")
        for enroll in enrolls:
            print(enroll)

    def add_enrolls(self):
        try:
            id = int(input("Enter the id: "))
            person_id = int(input("Enter the ID for the person: "))
            event_id = int(input("Enter the ID for the event: "))
            self.__enrollService.add(id, person_id, event_id)
        except ValueError:
            print("Invalid data!")
        except KeyError as ke:
            print(ke)

    def events_for_person_ordered_after_date(self):
        try:
            person = input("Name of the person: ")
            events = self.__personEventService.return_person_enrolled_at_event_after_date()
            print(events)
        except KeyError as ke:
            print (ke)

    def person_with_most_events(self):
        all_persons = self.__enrollService.person_most_events()
        for person in all_persons:
            print(person)

    def first_20(self):
        print(self.__personEventService.first_20())


    def persons_enrolled_at_event(self):
        try:
            description_event = input("Description \ Name of the event: ")
            all_persons = self.__enrollService.person_enrolled_at_event(description_event)
            print(all_persons)
        except:
            print("Invalid data!")


    def print_meniu_general(self):
        print("Working with: a- persons\n"
              "              b- events\n")

    def print_meniu_person(self):
        print("1. Add person: ")
        print("2. Modifiy person: ")
        print("3. Delete person: ")
        print("a. Show all persons: ")
        print()

    def print_meniu_event(self):
        print("1. Add event: ")
        print("2. Modify event: ")
        print("3. Delete event: ")
        print("4. Enroll person to the event: ")
        print("5. Print all enrollments")
        print("6. List of events a person is enrolled to ordered by description, date")
        print("7. Persons enrolled at most events:")
        print("8. First 20% events with the most enrolled people")
        print("a. Show all events")



    def meniu(self):
        while True:
            self.print_meniu_general()
            option1= input("Select the class you want to work with:\n")
            if option1 == "a":
                self.print_meniu_person()
                option= input("Select an option:\n")
                if option == "1":
                    self.add_person()
                elif option == "2":
                    self.modify_person()
                elif option == "3":
                    self.delete_person()
                elif option == "a":
                    self.print_persons()
                elif option == "x":
                    break
                else:
                    print("Invalid option, try again")
            elif option1 == "b":
                self.print_meniu_event()
                option = input("Select an option\n")
                if option == "1":
                    self.add_event()
                elif option == "2":
                    self.modify_event()
                elif option == "3":
                    self.delete_event()
                elif option == "4":
                    self.add_enrolls()
                elif option == "5":
                    self.print_enrolls()
                elif option == "6":
                    self.events_for_person_ordered_after_date()
                elif option == "7":
                    self.person_with_most_events()
                elif option == "8":
                    self.first_20()
                elif option == "a":
                    self.print_events()
                elif option == "x":
                    break
                else:
                    print("Invalid option, try again")





