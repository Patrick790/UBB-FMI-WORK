from unittest import TestCase
class TestPerson(TestCase):

    def setUp(self):
        from domain.Person import Person
        self.person = Person(1,"Ioana","Tache")

    def test_get_name(self):
        self.assertTrue(self.person.get_name() == "Ioana", "Person name must be Ioana")
        # self.person.set_name("Ana")
        # self.assertTrue(self.person.get_name() == "Ana", "Name of the person must be Ana")

    def test_get_adress(self):
        self.assertTrue(self.person.get_adress() == "Tache", "Person adress must be Tache")
        self.person.set_adress("Eroilor")
        self.assertTrue(self.person.get_adress() == "Eroilor", "Person adress must be Eroilor")

    def test_set_name(self):
        self.person.set_name("Ana")
        self.assertTrue(self.person.get_name() == "Ana", "Name of the person must be Ana")

    def test_set_adress(self):
        self.person.set_adress("Eroilor")
        self.assertTrue(self.person.get_adress() == "Eroilor", "Person adress must be Eroilor")

    def test_str(self):
        self.assertTrue(self.person.__str__() == "Person" + str(self.person.get_id()) +\
                        " : " + str(self.person.get_name()) + \
                        " , " + str(self.person.get_adress()))