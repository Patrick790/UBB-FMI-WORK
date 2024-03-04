from domeniu.cheltuiala import get_id, get_tip, get_suma


def tipareste_cheltuieli_dupa_tip(lista_cheltuieli, tip):

    '''
    functie care returneaza lista cheltuielilor de un anumit tip
    :param lista_cheltuieli: lista de cheltuieli
    :param tip: tipul cheltuielii
    :return: lista cheltuielilor de un anumit tip
    '''

    lista_cheltuieli_tip = []
    for i in range (0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        if get_tip(cheltuiala_curenta) == tip:
            lista_cheltuieli_tip.append(cheltuiala_curenta)
    return lista_cheltuieli_tip

def sorteaza_lista_cheltuieli_dupa_tip(lista_cheltuieli):
    '''
    functie care returneaza lista de apartamente sortate dupa tipul cheltuielii
    :param lista_cheltuieli: lista de cheltuieli
    :return: lista sortata
    '''
    lista_sortata = sorted(lista_cheltuieli, key=get_tip, reverse=True)
    return lista_sortata

def suma_totala_tip(lista_cheltuieli, tip):
    '''
    functie care calculeaza suma totala care trebuie achitata pt un apartament
    :param lista_cheltuieli: lista de cheltuieli
    :param id: idul cheltuielii
    :return: suma totala pentru un apartament
    '''
    S = 0
    for cheltuiala in lista_cheltuieli:
        if get_tip(cheltuiala) == tip:
            S = S + get_suma(cheltuiala)
    return S

def total_cheltuieli_id(lista_cheltuieli, id):
    '''
    fuctie care calculeaza totalul de cheltuieli pt un apartament
    :param lista_cheltuieli: lista de cheltuieli
    :param id: id cheltuiala
    :return: totalul de cheltuieli
    '''
    total = 0
    for cheltuiala in lista_cheltuieli:
        if get_id(cheltuiala) == id:
            total = total + 1
    return total

def acelasi_id(cheltuiala1, cheltuiala2):
    '''
    functie care verifica daca 2 cheltuieli au acelasi id
    :param cheltuiala1: cheltuiala
    :param cheltuiala2: cheltuiala
    :return: 1 daca cele 2 iduri sunt egale, 0 in caz contrar
    '''
    if get_id(cheltuiala1) != get_id(cheltuiala2):
        return 0
    return 1

def suma_apartament(lista_cheltuieli, id):
    '''
    functie care calculeaza suma totala de la un apartament dat
    :param lista_cheltuieli: lista de cheltuieli
    :param id: id cheltuiala
    :return: suma totala de la un apartament
    '''
    S = 0
    for cheltuiala in lista_cheltuieli:
        if get_id(cheltuiala) == id:
            S = S + get_suma(cheltuiala)
    return S

def lista_apartamente(lista_cheltuieli, suma):
    '''
    functie care construieste lista de apartamente cu cheltuieli mai mari decat o suma data
    :param lista_cheltuieli: lista de cheltuieli
    :param suma: suma data
    :return: lista de apartamente cu cheltuieli mai mari decat suma data
    '''
    lista_apartamente = []
    for i in range (0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        if suma < suma_apartament(lista_cheltuieli, get_id(cheltuiala_curenta)):
            lista_apartamente.append(cheltuiala_curenta)
    return lista_apartamente



def lista_cheltuieli_suma_zi( cheltuiala, suma, zi_cheltuiala,zi):
    if suma < get_suma(cheltuiala) and zi_cheltuiala < zi:
        print(cheltuiala)


def elimina_cheltuieli_tip(lista_cheltuieli, tip):
    '''
    functia filtreaza elementele care nu sunt de tipul specificat intr-o alta lista de cheltuieli
    :param lista_cheltuieli: lista de cheltuieli
    :param tip: tipul cheltuielii
    :return: lista de cheltuieli dupa eliminarea celor de un anumit tip
    '''
    lista_cheltuieli_dupa_eliminare_tip = []
    for i in range(0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        if get_tip(cheltuiala_curenta) != tip:
            lista_cheltuieli_dupa_eliminare_tip.append(cheltuiala_curenta)
    return lista_cheltuieli_dupa_eliminare_tip


def elimina_cheltuieli_mai_mici_decat_suma(lista_cheltuieli, suma):
    '''
    functia filtreaza elementele care sunt mai mari decat o suma data intr-o alta lista de cheltuieli
    :param lista_cheltuieli: lista de cheltuieli
    :param suma: suma
    :return: lista de cheltuieli dupa eliminarea celor mai mici decat o suma data
    '''
    lista_cheltuieli_mai_mari = []
    for i in range(0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        if get_suma(cheltuiala_curenta) >= suma:
            lista_cheltuieli_mai_mari.append(cheltuiala_curenta)
    return lista_cheltuieli_mai_mari
