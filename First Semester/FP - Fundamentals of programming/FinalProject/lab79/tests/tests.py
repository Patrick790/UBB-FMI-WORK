from unittest import TestCase
import unittest

from exeption.exeption import RepoError
from repository import personRepository, eventRepository, enrollRepository, Repository

import self as self

from domain.Enroll import Enroll
from domain.Event import Event
from domain.Person import Person
from repository.enrollRepository import EnrollRepository
from repository.eventRepository import EventRepository
from repository.personRepository import PersonRepository
from service.enrollService import EnrollService
from service.eventService import EventService
from service.personService import PersonService
from service import dtoService

# class TestEntity(unittest.TestCase):
#
#     def setUp(self):
#         from domain.Entity import Entity
#         self.entity = Entity(1)
#
#     def test_id(self):
#         self.assertTrue(self.entity.get_id() == 1)
#         self.entity.set_id(2)
#         self.assertTrue(self.entity.get_id() == 2)
#
#     def test_str(self):
#         self.assertTrue(self.entity.__str__() == "ID" + str(self.entity.get_id()) + "\n")


# class TestEvent(unittest.TestCase):
#
#     def setUp(self):
#         from domain.Event import Event
#         self.event = Event(11, 2022-12-20, 3, "Christmas Party")
#
#     def test_id(self):
#         self.assertTrue(self.event.get_id() == 11, "The event id must be 11")
#         self.event.set_id(12)
#         self.assertTrue(self.event.get_id() == 12, "Event id must be 12")
#
#     def test_date(self):
#         self.assertTrue(self.event.get_date() == 2022-12-20, "Date of the event must be 2022-12-20")
#         self.event.set_date(2022-12-24)
#         self.assertTrue(self.event.get_date() == 2022-12-24, "Date of the event must be 2022-12-24")
#
#     def test_description(self):
#         self.assertTrue(self.event.get_description() == "Christmas Party", "Description of the event must be Christmas Party")
#         self.event.set_description("CP")
#         self.assertTrue(self.event.get_description() == "CP", "Description of the event must be CP")
#
#     def test_time(self):
#         self.assertTrue(self.event.get_time() == 3, "Duration of the event must 3")
#         self.event.set_time(2)
#         self.assertTrue(self.event.get_time() == 2, "Duration of the event must be 2")
#
#     def test_str(self):
#         self.assertTrue(self.event.__str__() == "Event " + str(self.event.get_id()) + " : " +\
#                         str(self.event.get_date()) + " , "  +\
#                         str(self.event.get_time()) + " , " +\
#                         str(self.event.get_description()))


# class TestPerson(unittest.TestCase):
#
#     def setUp(self):
#         from domain.Person import Person
#         self.person = Person(1,"Ioana","Tache")
#
#     def test_id(self):
#         self.assertTrue(self.person.get_id() == 1, "Person id must be 1")
#         self.person.set_id(2)
#         self.assertTrue(self.person.get_id() == 2, "Person id must be 2")
#
#     def test_name(self):
#         self.assertTrue(self.person.get_name() == "Ioana", "Person name must be Ioana")
#         self.person.set_name("Ana")
#         self.assertTrue(self.person.get_name() == "Ana", "Name of the person must be Ana")
#
#     def test_adress(self):
#         self.assertTrue(self.person.get_adress() == "Tache", "Person adress must be Tache")
#         self.person.set_adress("Eroilor")
#         self.assertTrue(self.person.get_adress() == "Eroilor", "Person adress must be Eroilor")
#
#     def test_str(self):
#         self.assertTrue(self.person.__str__() == "Person" + str(self.person.get_id()) +\
#                         " : " + str(self.person.get_name()) + \
#                         " , " + str(self.person.get_adress()))


# class TestEnroll(TestCase):
#     def setUp(self):
#         from domain.Enroll import Enroll
#         self.enroll = Enroll(101, 1, 11)
#
#     def test_id(self):
#         self.assertTrue(self.enroll.get_id() == 101, "Enroll id must be 101")
#         self.enroll.set_id(102)
#         self.assertTrue(self.enroll.get_id() == 102, "Enroll id must be 102")
#
#     def test_person_id(self):
#         self.assertTrue(self.enroll.get_personID() == 1, "Id of the person enrolled must be 1")
#         self.enroll.set_personID(2)
#         self.assertTrue(self.enroll.get_personID() == 2, "Id of the person enrolled must be 2")
#
#     def test_event_id(self):
#         self.assertTrue(self.enroll.get_evenId() == 11, "Event of the event must be 11")
#         self.enroll.set_evenId(12)
#         self.assertTrue(self.enroll.get_evenId() == 12, "ID of the event must be 11")
#
#     def test_str(self):
#         self.assertTrue(self.enroll.__str__() == "Enroll: " + str(self.enroll.get_id()) +\
#                         "\nPerson ID: " + str(self.enroll.get_personID()) + \
#                         "\nEvent ID: " + str(self.enroll.get_evenId()) + "\n")
#
#     def tearDown(self) -> None:
#         pass

# class TestRepositoryPerson(TestCase):
#
#     def setUp(self):
#         self.persons = PersonRepository()
#         self.__person1 = Person(1,"Ioana","Tache")
#         self.__person2 = Person(2,"Adi","Bucegi")
#         self.persons.add(self.__person1)
#         self.persons.add(self.__person2)
#
#     def test_lenght(self):
#         self.assertEqual(self.persons.__len__(), 2)
#
#     def test_add_person(self):
#         try:
#             self.persons.add(self.__person1)
#             assert False
#         except RepoError as e:
#             assert(str(e) == "There already is an entity with this id!")
#
#     def test_modify(self):
#         new_person = Person(1,"Diana","Tache")
#         self.persons.modify(new_person)
#         new_innexistent_person = Person(3,"Diana","Tache")
#         try:
#             self.persons.modify(new_innexistent_person)
#             assert False
#         except RepoError as e:
#             assert (str(e) == "Entity does not exist!")
#
#     def test_get_all(self):
#         list = []
#         self.assertEqual(len(list), 0)
#         list = self.persons.get_all()
#         self.assertEqual(len(list), 2)
#
#     def test_delete(self):
#         self.assertEqual(self.persons.__len__(), 2)
#         self.persons.delete(1)
#         # self.persons.delete(4)
#         self.assertEqual(self.persons.__len__(), 1)
#         try:
#             self.persons.delete(1)
#             assert False
#         except RepoError as e:
#             assert(str(e) == ("There is not an entity with this id!"))
#
#     def test_get_by_id(self):
#         id_person = self.__person2.get_id()
#         self.assertEqual(self.persons.get_by_id(id_person), self.__person2)
#         self.assertEqual(self.persons.get_by_id(1),self.__person1)
#         self.assertEqual(self.persons.get_by_id(8), -1)

    # def test_get_person_by_id(self):
    #     id_person = self.__person2.get_id()
    #     self.assertEqual(self.persons.get_person_by_id(id_person), self.__person2)
    #     self.assertEqual(self.persons.get_person_by_id(5), -1)
    #     self.assertEqual(self.persons.get_person_by_id(1), self.__person1)
    #
    # def test_get_by_name(self):
    #     person_name = self.__person1.get_name()
    #     self.assertEqual(self.persons.get_by_name(person_name), self.__person1)
    #     self.assertEqual(self.persons.get_by_name("qwer"), -1)

# class TestRepositoryEvent(unittest.TestCase):
#
#     def setUp(self):
#         self.events = EventRepository()
#         self.event1 = Event(1,2022-12-20,3,"Christmas Party")
#         self.event2 = Event(2,2022-12-27,1,"UNO")
#         self.events.add(self.event1)
#         self.events.add(self.event2)
#
#     def test_get_event_by_id(self):
#         event_id = self.event1.get_id()
#         self.assertEqual(self.events.get_event_by_id(event_id), self.event1)
#         self.assertEqual(self.events.get_event_by_id(4), -1)

# class TestRepositoryEnroll(unittest.TestCase):
#
#     def setUp(self):
#         self.personrepository = PersonRepository
#         self.eventrepository = EventRepository
#         self.enrolls = EnrollRepository(self.personrepository, self.eventrepository)
#         self.event1 = Event(11,2022-12-20,3,"Christmas Party")
#         self.event2 = Event(12,2022-12-27,1,"UNO")
#         self.event3 = Event(13,2022-12-29,6,"Catan")
#         self.__person1 = Person(1,"Ioana","Tache")
#         self.__person2 = Person(2,"Adi","Bucegi")
#         self.__person3 = Person(3,"Codruta","Bologa")
#         self.enroll1 = Enroll(102, self.__person1, self.event1)
#         self.enroll2 = Enroll(103, self.__person2, self.event2)
#         self.enroll3 = Enroll(104, self.__person3, self.event3)
#         self.enrolls.add(self.enroll1)
#         self.enrolls.add(self.enroll2)
#         self.enrolls.add(self.enroll3)


    # def test_add(self):
        # id_person1 = self.__person1.get_id()
        # id_event1 = self.event1.get_id()
        # enroll = Enroll()
        # self.assertEqual
        # person_id = self.enroll1.get_personID()
        # event_id = self.enroll1.get_evenId()
        # list = []
        # self.assertEqual(len(list), 0)
        # enroll4 = Enroll(111, self.__person1, self.event)
        # self.enrolls.add

        # self.enrolls.add(self.enroll1)
        # self.enrolls.add(self.enroll2)
        # try:
        #     self.enrolls.add(self.enroll1)
        #     assert False
        # except RepoError as e:
        #     assert(str(e) ==)

    # def test_get_all(self):
    #     list = self.enrolls.get_all()
    #     self.assertEqual(len(list), 3)

# class TestServicePersons(unittest.TestCase):

    # def setUp(self):
    #     self.PersonRepository = PersonRepository()
    #     self.persons = PersonService(self.PersonRepository)
    #     self.person1 = Person(5,"Ioana","Tache")
    #     self.person2 = Person(6,"Adi","Bucegi")
    #     self.event1 = Event(1,2022-12-20,3,"Christmas Party")
    #     self.event2 = Event(2,2022-12-27,1,"UNO")
    #
    # def test_add_person(self):
    #     self.assertEqual(self.persons.size(), 0)
    #     self.persons.add_person(5,"Ana","Maniu")
    #     self.assertEqual(self.persons.size(), 1)
    #     try:
    #         self.persons.add_person(5,'Ioana','Tache')
    #         assert False
    #     except RepoError as e:
    #         assert (str(e) == "There already is an entity with this id!")
    #
    # def test_get_all(self):
    #     self.persons.add_person(5,'Ioana','Tache')
    #     list= []
    #     self.assertEqual(len(list), 0)
    #     list = self.persons.get_all_persons()
    #     self.assertEqual(len(list), 1)
    #
    # def test_modify_person(self):
    #     self.persons.add_person(1,"Ioana","Tache")
    #     list = self.persons.get_all_persons()
    #     new_list = []
    #     for person in list:
    #         new_list.append(str(person))
    #     assert(str(new_list) ==  str(["Person1 : Ioana , Tache"]))
    #     self.persons.modify_person(1,"Pop","Tache")
    #     list = self.persons.get_all_persons()
    #     new_list = []
    #     for person in list:
    #         new_list.append(str(person))
    #     assert(str(new_list) == "['Person1 : Pop , Tache']")
    #     try:
    #         self.persons.modify_person(3, 'Pop', 'Tache')
    #         assert False
    #     except RepoError as e:
    #         assert (str(e) == "Entity does not exist!")
    #
    # def test_delete_person(self):
    #     self.persons.add_person(1,"Ioana","Tache")
    #     self.persons.delete_person(1)
    #     try:
    #         self.persons.delete_person(1)
    #         assert False
    #     except RepoError as e:
    #         assert(str(e) == "There is not an entity with this id!")
    #
    # def test_size(self):
    #     self.assertEqual(self.persons.size(), 0)
    #     self.persons.add_person(1,"Ioana","Tache")
    #     self.assertEqual(self.persons.size(), 1)

# class TestEventService(unittest.TestCase):

    # def setUp(self):
    #     self.eventrepository = EventRepository()
    #     self.events = EventService(self.eventrepository)
    #     self.event1 = Event(1,2022-12-27,1,"UNO")
    #
    # def test_add_event(self):
    #     self.assertEqual(self.events.size(), 0)
    #     self.events.add_event(1,2022-12-29,6,"Catan")
    #     self.assertEqual(self.events.size(), 1)
    #     try:
    #         self.events.add_event(1,"2022-12-29",6,"Catan")
    #         assert False
    #     except RepoError as e:
    #         assert(str(e) == "There already is an entity with this id!")
    #
    # def test_get_all(self):
    #     self.events.add_event(1,"2022-12-27",1,"UNO")
    #     list = []
    #     self.assertEqual(len(list), 0)
    #     list = self.events.get_all_events()
    #     self.assertEqual(len(list), 1)
    #
    # def test_test_delete_events(self):
    #     self.events.add_event(1,"2022-12-27",1,"UNO")
    #     self.assertEqual(self.events.size(), 1)
    #     self.events.delete_event(1)
    #     self.assertEqual(self.events.size(), 0)
    #     try:
    #         self.events.delete_event(3)
    #         assert False
    #     except RepoError as e:
    #         assert(str(e) == "There is not an entity with this id!")
    #
    # def test_modify_event(self):
    #     self.events.add_event(1,"2022-12-27",1,"UNO")
    #     list = self.events.get_all_events()
    #     new_list = []
    #     for event in list:
    #         new_list.append(str(event))
    #     assert(str(new_list) == str(["Event 1 : 2022-12-27 , 1 , UNO"]))
    #     self.events.modify_event(1,"2022-12-30",2,"Poker")
    #     list = self.events.get_all_events()
    #     new_list = []
    #     for event in list:
    #         new_list.append(str(event))
    #     assert(str(new_list) == str(["Event 1 : 2022-12-30 , 2 , Poker"]))
    #     try:
    #         self.events.modify_event(3,"2022-12-30",2,"Poker")
    #         assert False
    #     except RepoError as e:
    #         assert(str(e) == "Entity does not exist!")

# class TestEnrollService(unittest.TestCase):
#
#     def setUp(self):
#         self.personrepository = PersonRepository()
#         self.eventrepository = EventRepository()
#         self.enrollrepository = EnrollRepository(self.personrepository ,self.eventrepository)
#         self.enrolls = EnrollService(self.enrollrepository, self.personrepository, self.eventrepository, self.personeventService)
#         self.person1 = Person(8,"Ioana","Tache")
#         self.person2 = Person(9,"Adi","Bucegi")
#         self.personrepository.add(self.person1)
#         self.personrepository.add(self.person2)
#         self.event1 = Event(18,"2022-12-20",3,"Christmas Party")
#         self.event2 = Event(19,"2022-12-27",1,"UNO")
#         self.eventrepository.add(self.event1)
#         self.eventrepository.add(self.event2)
#
#     def test_add(self):
#         self.assertEqual(self.enrolls.size(), 0)
#         self.enrolls.add(111,self.person1.get_id(), self.event1.get_id())
#         self.assertEqual(self.enrolls.size(), 1)
#         self.enrolls.add(2, self.person2.get_id(), self.event2.get_id())
#         self.assertEqual(self.enrolls.size(), 2)
#
#     def test_get_all(self):
#         self.enrolls.add(111,self.person1.get_id(), self.event1.get_id())
#         list = []
#         self.assertEqual(len(list), 0)
#         list = self.enrolls.get_all()
#





























