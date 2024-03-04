from Business.service import tipareste_cheltuieli_dupa_tip, sorteaza_lista_cheltuieli_dupa_tip, suma_totala_tip, \
    total_cheltuieli_id, lista_apartamente, lista_cheltuieli_suma_zi, elimina_cheltuieli_tip, \
    elimina_cheltuieli_mai_mici_decat_suma
from domeniu.cheltuiala import initializeaza_cheltuiala, to_string
from infrastructura.repository import modifica_cheltuiala, sterge_cheltuiala_id, sterge_cheltuiala_id_consecutiv, \
    sterge_cheltuiala_tip, adauga_cheltuiala


def ui_tipareste_cheltuieli(lista_cheltuieli):
    if len(lista_cheltuieli) == 0:
        print("Lista de cheltuieli este goala!")
    for i in range(0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        print(to_string(cheltuiala_curenta))

def ui_adauga_cheltuiala(lista_cheltuieli):
    id = int(input("Introduceti id:"))
    suma = float(input("Introduceti suma:"))
    tip = input("Introduceti tip:")
    cheltuiala = initializeaza_cheltuiala(id, suma, tip)
    adauga_cheltuiala(lista_cheltuieli, cheltuiala)


def ui_sterge_cheltuiala_id(lista_cheltuieli):
    id = int(input("Introduceti idul cheltuielii pe care doriti sa o stergeti:"))
    sterge_cheltuiala_id(lista_cheltuieli, id)


def ui_modifica_cheltuiala(lista_cheltuieli):
    id = int(input("Introduceti idul cheltuielii pe care vreti sa o modificati:"))
    suma = float(input("Introduceti suma:"))
    tip = input("Introduceti tip:")
    modifica_cheltuiala(lista_cheltuieli, id, suma, tip)

def ui_sterge_cheltuiala_id_consecutiv(lista_cheltuieli):
    id1 = int(input("Introduceti primul id:"))
    id2= int(input("Introduceti al doilea id:"))
    sterge_cheltuiala_id_consecutiv(lista_cheltuieli, id1, id2)

def ui_sterge_cheltuiala_tip(lista_cheltuieli):
    tip = input("Introduceti tip:")
    sterge_cheltuiala_tip(lista_cheltuieli,tip)

def ui_tipareste_cheltuieli_dupa_tip(lista_cheltuieli):
    tip = input("Introduceti tip:")
    cheltuieli = tipareste_cheltuieli_dupa_tip(lista_cheltuieli,tip)
    ui_tipareste_cheltuieli(cheltuieli)

def ui_tipareste_lista_cheltuieli_sortata(lista_cheltuieli):
    lista_sortata = sorteaza_lista_cheltuieli_dupa_tip(lista_cheltuieli)
    ui_tipareste_cheltuieli(lista_sortata)

def ui_suma_totala_tip(lista_cheltuieli):
    tip = input("Introduceti tip:")
    Suma = suma_totala_tip(lista_cheltuieli, tip)
    print(Suma)

def ui_total_cheltuieli_apartament(lista_cheltuieli):
    id = int(input("Introduceti apartament:"))
    total = total_cheltuieli_id(lista_cheltuieli, id)
    print(total)

def ui_tipareste_toate_apartamentele_cu_cheltuieli_mai_mari(lista_cheltuieli):
    suma = float(input("Introduceti suma:"))
    apartamente = lista_apartamente(lista_cheltuieli, suma)
    ui_tipareste_cheltuieli(apartamente)


def ui_tipareste_cheltuieli_zi_suma(lista_cheltuieli):
    suma = float(input("Introduceti suma:"))
    zi = int(input("Introduceti zi:"))
    for i in range (0, len(lista_cheltuieli)):
        cheltuiala_curenta = lista_cheltuieli[i]
        zi_cheltuiala = int(input("Introduceti zi:"))
        lista_cheltuieli_suma_zi( cheltuiala_curenta, suma, zi_cheltuiala, zi)


def ui_elimina_cheltuieli_dupa_tip(lista_cheltuieli):
    tip = input("Introduceti tip:")
    cheltuieli = elimina_cheltuieli_tip(lista_cheltuieli,tip)
    ui_tipareste_cheltuieli(cheltuieli)


def ui_elimina_cheltuieli_mai_mici(lista_cheltuieli):
    suma = float(input("Introduceti suma:"))
    cheltuieli = elimina_cheltuieli_mai_mici_decat_suma(lista_cheltuieli, suma)
    ui_tipareste_cheltuieli(cheltuieli)

def ui_undo(lista_undo, lista_cheltuieli_precompletata):
    if len(lista_undo) == 1:
        return lista_cheltuieli_precompletata
    return lista_undo[-2]

def meniu():
    meniu = "MENIU\n"
    meniu = meniu + "1.Tipareste toate cheltuielile\n"
    meniu = meniu + "2.Adauga cheltuiala\n"
    meniu = meniu + "3.Sterge cheltuiala dupa id\n"
    meniu = meniu + "4.Modificare cheltuiala\n"
    meniu = meniu + "5.Sterge cheltuieli la apartamente consecutive\n"
    meniu = meniu + "6.Sterge cheltuielile de un anumit tip de la fiecare apartament\n"
    meniu = meniu + "7.Tipareste cheltuielile de un anumit tip\n"
    meniu = meniu + "8.Tipareste apartamentele sortate dupa tip\n"
    meniu = meniu + "9.Tipareste suma totala pentru un tip de cheltuiala\n"
    meniu = meniu + "10.Tipareste totalul de cheltuieli pt un apartament dat\n"
    meniu = meniu + "11.Tipareste toate apartamentele care au cheltuieli mai mari decat o suma data\n"
    meniu = meniu + "12.Tipareste toate cheltuielile efectuate inainte de o zi si mai mari decat o suma\n"
    meniu = meniu + "13.Elimina toate cheltuielile de un anumit tip\n"
    meniu = meniu + "14.Eliminare toate cheltuielile mai mici decat o suma data\n"
    meniu = meniu + "15.Undo\n"
    meniu = meniu + "0.Iesire\n"
    return meniu


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
    while ruleaza == True:
        meniul_meu = meniu()
        print(meniul_meu)
        comanda = input("Introduceti comanda:")
        if comanda == "1":
            ui_tipareste_cheltuieli(lista_cheltuieli)
        elif comanda == "2":
            ui_adauga_cheltuiala(lista_cheltuieli)
            lista_undo.append(lista_cheltuieli[:])

        elif comanda == "3":
            ui_sterge_cheltuiala_id(lista_cheltuieli)
            lista_undo.append(lista_cheltuieli[:])
        elif comanda == "4":
            ui_modifica_cheltuiala(lista_cheltuieli)
            lista_undo.append(lista_cheltuieli[:])
        elif comanda == "5":
            ui_sterge_cheltuiala_id_consecutiv(lista_cheltuieli)
            lista_undo.append(lista_cheltuieli[:])
        elif comanda == "6":
            ui_sterge_cheltuiala_tip(lista_cheltuieli)
            lista_undo.append(lista_cheltuieli[:])
        elif comanda == "7":
            ui_tipareste_cheltuieli_dupa_tip(lista_cheltuieli)
        elif comanda =="8":
            ui_tipareste_lista_cheltuieli_sortata(lista_cheltuieli)
        elif comanda =="9":
            ui_suma_totala_tip(lista_cheltuieli)
        elif comanda == "10":
            ui_total_cheltuieli_apartament(lista_cheltuieli)
        elif comanda == "11":
            ui_tipareste_toate_apartamentele_cu_cheltuieli_mai_mari(lista_cheltuieli)
        elif comanda == "12":
            ui_tipareste_cheltuieli_zi_suma(lista_cheltuieli)
        elif comanda == "13":
            ui_elimina_cheltuieli_dupa_tip(lista_cheltuieli)
            lista_undo.append(lista_cheltuieli[:])
        elif comanda == "14":
            ui_elimina_cheltuieli_mai_mici(lista_cheltuieli)
            lista_undo.append(lista_cheltuieli[:])
        elif comanda == "15":
            lista_cheltuieli = ui_undo(lista_undo, lista_cheltuieli_precompletata())
            ui_undo(lista_undo, lista_cheltuieli_precompletata())

        elif comanda == "0":
            ruleaza = False

        else:
            print("Comanda invalida! Reincercati!")