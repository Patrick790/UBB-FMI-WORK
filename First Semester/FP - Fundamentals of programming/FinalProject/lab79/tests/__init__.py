from unittest import TestCase

from Domain.carte import Carte
from Domain.client import Client
from Domain.inchiriere import Inchiriere
from Repository.bookRepository import BookRepository
from Repository.clientRepository import ClientRepository
from Repository.inchiriereRepository import InchiriereRepository
from Repository.repository import Repository
from Repository.repository_exception import DuplicateIDException, InexistentIDException


class TestInchiriereRepository(TestCase):
    def setUp(self) -> None:
        self.repository = Repository()
        self.book_repository = BookRepository()
        self.client_repository = ClientRepository()
        self.inchiriere_repository = InchiriereRepository(self.book_repository, self.client_repository)
        self.carte = Carte(1, "Mara", "povesti", "Ioan Slavici")
        self.book_repository.add(self.carte)
        self.client = Client(1, "Maria", "11111")
        self.client_repository.add(self.client)
        self.inchiriere1 = Inchiriere(1, 1, 1, "Mara")

    def test_add_inchiriere(self):
        inchiriere = Inchiriere(4, 6, 8, "")
        self.assertRaises(ValueError, self.inchiriere_repository.add_inchiriere, inchiriere)
        self.inchiriere_repository.add_inchiriere(self.inchiriere1)
        inchiriere2 = Inchiriere(3, 1, 1, "Mara")
        self.assertRaises(ValueError, self.inchiriere_repository.add_inchiriere, inchiriere2)
        with self.assertRaises(DuplicateIDException):
            self.inchiriere_repository.add_inchiriere(self.inchiriere1)
        test_client_id = self.client_repository.get_position_by_id(8)
        test_book_id = self.book_repository.get_position_by_id(2)
        self.assertIsNone(test_book_id)
        self.assertIsNone(test_client_id)
        test_inchiriere_dupa_id_carte = \
            self.inchiriere_repository.gaseste_inchiriere_dupa_client_id_si_carte_id(2, 2)
        self.assertIsNone(test_inchiriere_dupa_id_carte)
        # self.inchiriere_repository.add_inchiriere(self.inchiriere1)
        lista_inchirieri = self.inchiriere_repository.get_all()
        self.assertIsNot(lista_inchirieri, [])

    def test_gaseste_inchiriere_dupa_id(self):
        self.inchiriere_repository.add_inchiriere(self.inchiriere1)

    def test_gaseste_inchiriere_dupa_client_id_si_carte_id(self):
        self.inchiriere_repository.add_inchiriere(self.inchiriere1)
        i = self.inchiriere_repository.gaseste_inchiriere_dupa_client_id_si_carte_id(1, 1)
        self.assertEqual(i, 0)

    def test_sterge_inchirieri_carte(self):
        with self.assertRaises(InexistentIDException):
            self.inchiriere_repository.add_inchiriere(self.inchiriere1)
            inchiririeri = self.inchiriere_repository.get_all()
            self.assertEqual(inchiririeri[0], self.inchiriere1)
            self.inchiriere_repository.sterge_inchirieri_carte(self.inchiriere1.get_id())
            self.inchiriere_repository.sterge_inchirieri_carte(4)