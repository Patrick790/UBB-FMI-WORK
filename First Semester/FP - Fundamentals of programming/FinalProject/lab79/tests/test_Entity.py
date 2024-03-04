from unittest import TestCase


class TestEntity(TestCase):

    def setUp(self):
        from domain.Entity import Entity
        self.entity = Entity(1)

    def test_get_id(self):
        self.assertTrue(self.entity.get_id() == 1)

    def test_set_id(self):
        self.entity.set_id(2)
        self.assertTrue(self.entity.get_id() == 2)

    def test_str(self):
        self.assertTrue(self.entity.__str__() == "ID" + str(self.entity.get_id()) + "\n")
