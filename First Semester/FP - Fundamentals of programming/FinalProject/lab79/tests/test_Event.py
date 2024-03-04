from unittest import TestCase

class TestEvent(TestCase):

    def setUp(self):
        from domain.Event import Event
        self.event = Event(11, 2022-12-20, 3, "Christmas Party")

    def test_get_date(self):
        self.assertTrue(self.event.get_date() == 2022 - 12 - 20, "Date of the event must be 2022-12-20")

    def test_get_time(self):
        self.assertTrue(self.event.get_time() == 3, "Duration of the event must 3")

    def test_get_description(self):
        self.assertTrue(self.event.get_description() == "Christmas Party","Description of the event must be Christmas Party")

    def test_set_date(self):
        self.event.set_date(2022 - 12 - 24)
        self.assertTrue(self.event.get_date() == 2022 - 12 - 24, "Date of the event must be 2022-12-24")

    def test_set_time(self):
        self.event.set_time(2)
        self.assertTrue(self.event.get_time() == 2, "Duration of the event must be 2")

    def test_set_description(self):
        self.event.set_description("CP")
        self.assertTrue(self.event.get_description() == "CP", "Description of the event must be CP")

    def test_str(self):
        self.assertTrue(self.event.__str__() == "Event " + str(self.event.get_id()) + " : " +\
                        str(self.event.get_date()) + " , "  +\
                        str(self.event.get_time()) + " , " +\
                        str(self.event.get_description()))