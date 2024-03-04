from Business.service import tipareste_cheltuieli_dupa_tip, suma_totala_tip, total_cheltuieli_id, \
    sorteaza_lista_cheltuieli_dupa_tip, suma_apartament, lista_apartamente
from domeniu.cheltuiala import initializeaza_cheltuiala, get_tip, set_suma, get_suma, get_id
from infrastructura.repository import adauga_cheltuiala, modifica_cheltuiala, sterge_cheltuiala_id, \
    sterge_cheltuiala_tip, sterge_cheltuiala_id_consecutiv
from ui.ui import ui_tipareste_cheltuieli


def test():
    cheltuiala = initializeaza_cheltuiala(11, 123, "apa")
    assert cheltuiala == { "id": 11, "suma": 123, "tip": "apa" }
    assert get_tip(cheltuiala) == "apa"
    set_suma(cheltuiala, 144.5)
    assert get_suma(cheltuiala) == 144.5
    assert get_id(cheltuiala) == 11

    lista_cheltuieli = []
    cheltuiala1 = initializeaza_cheltuiala(11, 123, "apa")
    adauga_cheltuiala(lista_cheltuieli, cheltuiala1)
    assert len(lista_cheltuieli) == 1
    modifica_cheltuiala(lista_cheltuieli, 11, 165, "gaz")
    assert len(lista_cheltuieli) == 1
    assert get_tip(lista_cheltuieli[0]) == "gaz"
    sterge_cheltuiala_id(lista_cheltuieli, 11)
    assert len(lista_cheltuieli) == 0

    lista_cheltuieli = []
    cheltuiala1 = initializeaza_cheltuiala(11, 123, "apa")
    adauga_cheltuiala(lista_cheltuieli, cheltuiala1)
    assert len(lista_cheltuieli) == 1
    sterge_cheltuiala_tip(lista_cheltuieli,"apa")
    assert len(lista_cheltuieli) == 0

    lista_cheltuieli = []
    cheltuiala2 = initializeaza_cheltuiala(15, 110, "gaz")
    cheltuiala3 = initializeaza_cheltuiala(16, 114, "canal")
    cheltuiala4 = initializeaza_cheltuiala(17, 123.23, "gaz")
    cheltuiala5 = initializeaza_cheltuiala(17, 78.36, "apa")
    adauga_cheltuiala(lista_cheltuieli, cheltuiala2)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala3)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala4)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala5)
    assert len(lista_cheltuieli) == 4

    assert tipareste_cheltuieli_dupa_tip(lista_cheltuieli, "gaz") == [cheltuiala2, cheltuiala4]
    #assert suma_totala_tip(lista_cheltuieli, "gaz") == 233.23
    assert total_cheltuieli_id(lista_cheltuieli, 17) == 2
    assert sterge_cheltuiala_id_consecutiv(lista_cheltuieli, 16, 17) == [cheltuiala2]
    adauga_cheltuiala(lista_cheltuieli, cheltuiala3)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala4)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala5)
    assert suma_apartament(lista_cheltuieli, 17) == 201.59
    assert suma_apartament(lista_cheltuieli, 15) == 110

    assert lista_apartamente(lista_cheltuieli, 112) == [cheltuiala3, cheltuiala4, cheltuiala5]



    print("Testele au trecut!")