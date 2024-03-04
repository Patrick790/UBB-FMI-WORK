from unittest import TestCase

from domain.Enroll import Enroll
from domain.Event import Event
from domain.Person import Person
from exeption.exeption import RepoError
from repository.Repository import Repository
from repository.enrollRepository import EnrollRepository
from repository.eventRepository import EventRepository
from repository.personRepository import PersonRepository


class TestEnrollRepository(TestCase):

    def setUp(self):
        self.repository = Repository()
        self.personrepository = PersonRepository()
        self.eventrepository = EventRepository()
        self.enrolls = EnrollRepository(self.personrepository, self.eventrepository)
        self.event1 = Event(11,"2022-12-27",1,"Catan")
        self.person1 = Person(1,"Ioana","Tache")
        self.eventrepository.add(self.event1)
        self.personrepository.add(self.person1)
        self.enroll1 = Enroll(101,1,11)

    # def test_add_enroll(self):
    #     enroll = Enroll(109,7,18)
    #     self.assertRaises(ValueError, self.enrolls.add, enroll)
    #     self.enrolls.add(self.enroll1)
    #     enroll2 = Enroll(103,6,17)
    #     self.assertRaises(ValueError, self.enrolls.add, enroll2)
    #     # try:
    #     #     self.enrolls.add(self.enroll1)
    #     # except RepoError as e:
    #     #     assert (str(e) )
    #     with self.assertRaises(RepoError):
    #         self.enrolls.add(self.enroll1)
    #     test_person_id = self.personrepository.get_by_id(6)
    #     test_event_id = self.eventrepository.get_by_id(17)
    #     # self.assertIsNone(test_person_id)
    #     # self.assertIsNone(test_event_id)
    #     # test_enroll = \
    #     #     self.enrolls.find_enroll_after_person_id_and_event_id(1,1)
    #     # self.assertIsNone(test_enroll)
    #     # list_enrolls = self.enrolls.get_all()
    #     # self.assertIsNone(list_enrolls, [])


    def test_add(self):

        self.event2 = Event(12, "2022-12-30", 1, "UNO")
        self.person2 = Person(2, "ANA", "ana.")
        self.enroll2 = Enroll(102, 2, 12)
        self.enrolls.add(self.enroll1)
        # self.personrepository.add(self.person2)
        # self.eventrepository.add(self.event2)
        try:
            self.enrolls.add(self.enroll2)
        except RepoError as e:
            assert (str(e) == "The person or the event does not exist!")
        try:
            self.enroll4 = Enroll(103,1,11)
            self.enrolls.add(self.enroll4)
            # assert False
        except RepoError as e:
            assert (str(e) == "The person is already enrolled at the event")
        # self.assertEqual(self.enrolls.__len__(),1)
        try:
            # self.enroll2 = Enroll(102,self.enroll2.get_personID(),self.enroll2.get_evenId())
            self.enroll3 = Enroll(102, 2, 19)
            self.enrolls.add(self.enroll2)
            assert False
        except RepoError as e:
            assert (str(e) == "The person or the event does not exist!")

        # try:
        #     self.enroll3 = Enroll(104,1,11)
        #     self.enrolls.add(self.enroll3)
        # except ValueError as ke:
        #     assert (str(ke) == "The person is already enrolled at the event")
        # self.assertEqual(self.enrolls.__len__(), 2)



    # def test_find_enroll_after_person_id_and_event_id(self):
    #     self.event2 = Event(12, "2022-12-30", 1, "UNO")
    #     self.person2 = Person(2, "ANA", "ana.")
    #     self.eventrepository.add(self.event2)
    #     self.personrepository.add(self.person2)
    #     self.enroll2 = Enroll(102, 2, 12)
    #     self.enrolls.add(self.enroll2)
    #     test_enroll = self.enrolls.find_enroll_after_person_id_and_event_id(2,12)
    #     # enroll = self.enrolls.find_enroll_after_person_id_and_event_id(2,12)
    #     # self.assertEqual(enroll, 0)
    #     list = self.enrolls.get_all()
    #     self.assertEqual(list, [])

    def test_exist_enroll_event(self):
        self.enrolls.add(self.enroll1)
        list = self.enrolls.get_all()
        # for el in list:
        #     current_enroll = list[el]
            # if
        # self.assertEqual(self.enrolls.__len__(),1)
        # self.assertEqual(self.enrolls.exist_enroll_event(11), True)

    def test_delete_enrolls_event(self):
        self.enrolls.add(self.enroll1)
        # enrolls = self.enrolls.get_all()
        # self.assertEqual(enrolls[0], self.enroll1)
        # self.enrolls.delete(self.enroll1.get_id())
        # self.assertEqual(self.enrolls.__len__(), 1)
        # self.enrolls.delete(11)
        # self.assertEqual(self.enrolls.__len__(),0)

