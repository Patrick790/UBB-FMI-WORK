from domeniu.cheltuiala import get_id, initializeaza_cheltuiala, set_suma, set_tip, get_tip


def adauga_cheltuiala(lista_cheltuieli, cheltuiala_noua):
   '''
   functie care adauga o cheltuiala in lista de cheltuieli
   :param lista_cheltuieli: lista de cheltuieli
   :param cheltuiala_noua: cheltuiala care se doreste a fi adaugata in lista
   :return:
   '''
   lista_cheltuieli.append(cheltuiala_noua)

def sterge_cheltuiala_id(lista_cheltuieli, id):
    '''
    Functie care sterge o cheltuiala dupa id
    :param lista_cheltuieli: lista de cheltuieli
    :param id: idul cheltuielii
    :return:
    '''
    i = 0
    while i < len(lista_cheltuieli):
        chelt = lista_cheltuieli[i]
        if get_id(chelt) == id:
            lista_cheltuieli.remove(chelt)
            i = i - 1
        i = i + 1

def sterge_cheltuiala_id_consecutiv(lista_cheltuieli, id1, id2):
    '''
    functie care sterge cheltuielile de la apartamente consecutive
    :param lista_cheltuieli: lista de cheltuieli cu id intreg
    :param id1: id1
    :param id2: id2
    :return:
    '''
    i = 0
    while i < len(lista_cheltuieli):
        chelt = lista_cheltuieli[i]
        if get_id(chelt) >= id1 and get_id(chelt) <= id2:
            lista_cheltuieli.remove(chelt)
            i = i-1
        i = i + 1
    return lista_cheltuieli



def sterge_cheltuiala_tip(lista_cheltuieli, tip):
    '''
    functie care sterge cheltuielile de un anumit tip de la fiecare apartament
    :param lista_cheltuieli: lista de cheltuieli
    :param tip: tip
    :return:
    '''
    for cheltuiala in lista_cheltuieli:
        if get_tip(cheltuiala) == tip:
            lista_cheltuieli.remove(cheltuiala)


def modifica_cheltuiala(lista_cheltuieli, id, suma_noua, tip_nou):
    '''
    Functie care modifica proprietatile unei cheltuieli
    :param lista_cheltuieli: lista de cheltuieli
    :param id_nou: id nou
    :param suma_noua: suma noua
    :param tip_nou: tip nou
    :return:
    '''
    for i in range(0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        if get_id(cheltuiala_curenta) == id:
            set_suma(cheltuiala_curenta, suma_noua)
            set_tip(cheltuiala_curenta, tip_nou)