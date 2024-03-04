from business.service import tipareste_cheltuieli_dupa_tip, sorteaza_lista_cheltuieli_dupa_tip, suma_totala_tip, \
    total_cheltuieli_id, lista_apartamente, lista_cheltuieli_suma_zi, elimina_cheltuieli_tip, \
    elimina_cheltuieli_mai_mici_decat_suma
from domeniu.cheltuiala import initializeaza_cheltuiala, to_string
from infrastructura.repository import modifica_cheltuiala, sterge_cheltuiala_id, sterge_cheltuiala_id_consecutiv, \
    sterge_cheltuiala_tip, adauga_cheltuiala


def ui_tipareste_cheltuieli(lista_cheltuieli,params):
    if len(lista_cheltuieli) == 0:
        print("Lista de cheltuieli este goala!")
    for i in range(0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        print(to_string(cheltuiala_curenta))

def ui_adauga_cheltuiala(lista_cheltuieli,params):
    if len(params) != 3:
        print("Numar parametri invalid!\n")
    #id = int(input("Introduceti id:"))
    #suma = float(input("Introduceti suma:"))
    #tip = input("Introduceti tip:")
    id = int(params[0])
    suma = float(params[1])
    tip = params[2]
    cheltuiala = initializeaza_cheltuiala(id, suma, tip)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala)


def ui_sterge_cheltuiala_id(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid\n")
    id = int(params[0])
    #id = int(input("Introduceti idul cheltuielii pe care doriti sa o stergeti:"))
    sterge_cheltuiala_id(lista_cheltuieli, id)


def ui_modifica_cheltuiala(lista_cheltuieli,params):
    if len(params) != 3:
        print("Numar parametri invalid!\n")
    id = int(params[0])
    suma = float(params[1])
    tip = params[2]
    #id = int(input("Introduceti idul cheltuielii pe care vreti sa o modificati:"))
    #suma = float(input("Introduceti suma:"))
    #tip = input("Introduceti tip:")
    modifica_cheltuiala(lista_cheltuieli, id, suma, tip)

def ui_sterge_cheltuiala_id_consecutiv(lista_cheltuieli,params):
    if len(params) != 2:
        print("Numar parametri invalid!\n")
    id1 = int(params[0])
    id2 = int(params[1])
    #id1 = int(input("Introduceti primul id:"))
    #id2 = int(input("Introduceti al doilea id:"))
    sterge_cheltuiala_id_consecutiv(lista_cheltuieli, id1, id2)

def ui_sterge_cheltuiala_tip(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
    tip = params[2]
    #tip = input("Introduceti tip:")
    sterge_cheltuiala_tip(lista_cheltuieli,tip)

def ui_tipareste_cheltuieli_dupa_tip(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
    tip = params[0]
    #tip = input("Introduceti tip:")
    cheltuieli = tipareste_cheltuieli_dupa_tip(lista_cheltuieli,tip)
    ui_tipareste_cheltuieli(cheltuieli,params)

def ui_tipareste_lista_cheltuieli_sortata(lista_cheltuieli,params):
    lista_sortata = sorteaza_lista_cheltuieli_dupa_tip(lista_cheltuieli)
    ui_tipareste_cheltuieli(lista_sortata,params)

def ui_suma_totala_tip(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
    tip = params[2]

    #tip = input("Introduceti tip:")
    Suma = suma_totala_tip(lista_cheltuieli, tip)
    print(Suma)

def ui_total_cheltuieli_apartament(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
    id = int(params[0])
    #id = int(input("Introduceti apartament:"))
    total = total_cheltuieli_id(lista_cheltuieli, id)
    print(total)

def ui_tipareste_toate_apartamentele_cu_cheltuieli_mai_mari(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
    suma = float(params[0])
    #suma = float(input("Introduceti suma:"))
    apartamente = lista_apartamente(lista_cheltuieli, suma)
    ui_tipareste_cheltuieli(apartamente, params)


def ui_tipareste_cheltuieli_zi_suma(lista_cheltuieli,params):

    suma = float(input("Introduceti suma:"))
    zi = int(input("Introduceti zi:"))
    for i in range (0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        zi_cheltuiala = int(input("Introduceti zi:"))
        lista_cheltuieli_suma_zi( cheltuiala_curenta, suma, zi_cheltuiala, zi)


def ui_elimina_cheltuieli_dupa_tip(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
    tip = params[0]
    #tip = input("Introduceti tip:")
    cheltuieli = elimina_cheltuieli_tip(lista_cheltuieli,tip)
    ui_tipareste_cheltuieli(cheltuieli, params)


def ui_elimina_cheltuieli_mai_mici(lista_cheltuieli,params):
    if len(params) != 1:
        print("Numar parametri invalid!\n")
    suma = float(params[0])
    #suma = float(input("Introduceti suma:"))
    cheltuieli = elimina_cheltuieli_mai_mici_decat_suma(lista_cheltuieli, suma)
    ui_tipareste_cheltuieli(cheltuieli, params)

def ui_undo(lista_undo, lista_cheltuieli_precompletata,params):
    if len(lista_undo) == 1:
        return lista_cheltuieli_precompletata
    return lista_undo[-2]


def lista_cheltuieli_precompletata():
    lista_cheltuieli = []
    cheltuiala1 = initializeaza_cheltuiala(11, 123, "apa")
    cheltuiala2 = initializeaza_cheltuiala(11, 133, "gaz")
    cheltuiala3 = initializeaza_cheltuiala(12, 57, "curent")
    cheltuiala4 = initializeaza_cheltuiala(13, 155.23, "gaz")
    cheltuiala5 = initializeaza_cheltuiala(14, 178, "incalzire")
    cheltuiala6 = initializeaza_cheltuiala(15, 139, "curent")
    lista_cheltuieli.append(cheltuiala1)
    lista_cheltuieli.append(cheltuiala2)
    lista_cheltuieli.append(cheltuiala3)
    lista_cheltuieli.append(cheltuiala4)
    lista_cheltuieli.append(cheltuiala5)
    lista_cheltuieli.append(cheltuiala6)
    return lista_cheltuieli





def program():
    lista_cheltuieli = lista_cheltuieli_precompletata()
    ruleaza = True
    lista_undo = []
    lista_undo.append(lista_cheltuieli_precompletata())
    comenzi = {
        "tipareste_cheltuieli":ui_tipareste_cheltuieli,
        "adauga_cheltuiala":ui_adauga_cheltuiala,
        "sterge_cheltuiala_dupa_id":ui_sterge_cheltuiala_id,
        "modifica_cheltuiala":ui_modifica_cheltuiala,
        "sterge_cheltuieli_apartamente_consecutive":ui_sterge_cheltuiala_id_consecutiv,
        "sterge_cheltuieli_anumit_tip":ui_sterge_cheltuiala_tip,
        "tipareste_cheltuieli_tip":ui_tipareste_cheltuieli_dupa_tip,
        "tipareste_apartamente_sortate_tip":ui_tipareste_lista_cheltuieli_sortata,
        "suma_totala_tip_cheltuiala":ui_suma_totala_tip,
        "total_cheltuieli_apartament":ui_total_cheltuieli_apartament,
        "tipareste_apartamente_mai_mari_decat_suma_data":ui_tipareste_toate_apartamentele_cu_cheltuieli_mai_mari,
        "tiparestde_cheltuieli_efectuate_zi_suma":ui_tipareste_cheltuieli_zi_suma,
        "elimina_cheltuieli_tip":ui_elimina_cheltuieli_dupa_tip,
        "elimina_cheltuieli_mai_mici_decat_suma":ui_elimina_cheltuieli_mai_mici,
        "undo":ui_undo

    }
    while ruleaza == True:
        comanda = input(">>>")
        comanda = comanda.strip()
        if comanda == "":
            continue
        if comanda == "exit":
            return
        parti = comanda.split()
        nume_comanda = parti[0]
        params = parti[1:]
        for param in params:
            param = param.strip()
        if nume_comanda in comenzi:
            try:
                comenzi[nume_comanda](lista_cheltuieli, params)
            except ValueError as ve:
                print(ve)

        else:
            print("comanda invalida!")