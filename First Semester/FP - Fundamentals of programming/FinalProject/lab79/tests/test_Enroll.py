from unittest import TestCase

class TestEnroll(TestCase):

    def setUp(self):
        from domain.Enroll import Enroll
        self.enroll = Enroll(101, 1, 11)

    def test_id(self):
        self.assertTrue(self.enroll.get_id() == 101, "Enroll id must be 101")
        self.enroll.set_id(102)
        self.assertTrue(self.enroll.get_id() == 102, "Enroll id must be 102")

    def test_get_person_id(self):
        self.assertTrue(self.enroll.get_personID() == 1, "Id of the person enrolled must be 1")

    def test_get_even_id(self):
        self.assertTrue(self.enroll.get_evenId() == 11, "Event of the event must be 11")

    def test_set_person_id(self):
        self.enroll.set_personID(2)
        self.assertTrue(self.enroll.get_personID() == 2, "Id of the person enrolled must be 2")

    def test_set_even_id(self):
        self.enroll.set_evenId(12)
        self.assertTrue(self.enroll.get_evenId() == 12, "ID of the event must be 11")

    def test_str(self):
        self.assertTrue(self.enroll.__str__() == "Enroll: " + str(self.enroll.get_id()) +\
                        "\nPerson ID: " + str(self.enroll.get_personID()) + \
                        "\nEvent ID: " + str(self.enroll.get_evenId()))