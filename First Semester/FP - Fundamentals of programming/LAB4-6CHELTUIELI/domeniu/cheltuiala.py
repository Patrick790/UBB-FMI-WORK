def initializeaza_cheltuiala(id, suma, tip):
    '''
    Functie care initializeaza o cheltuiala cu niste valori pt proprietatile id, suma, tip
    :param id: numarul apartamentului caruia ii apartine cheltuiala
    :param suma: suma care trebuie platita
    :param tip: tipul cheltuielii create
    :return: dictionar care va descrie o anumita cheltuiala
    '''
    dictionar_cheltuiala = { "id":id, "suma":suma, "tip":tip }
    return dictionar_cheltuiala

####GETTERI

def get_id(cheltuiala):
    return cheltuiala["id"]

def get_suma(cheltuiala):
    return cheltuiala["suma"]

def get_tip(cheltuiala):
    return cheltuiala["tip"]

#####SETTERI

def set_id(cheltuiala, id_nou):
    cheltuiala["id"] = id_nou

def set_suma(cheltuiala, suma_noua):
    cheltuiala["suma"] = suma_noua

def set_tip(cheltuiala, tip_nou):
    cheltuiala["tip"] = tip_nou


def to_string(cheltuiala):
    string = ""
    string = string + "Cheltuiala id = " + str(get_id(cheltuiala)) + "\n"
    string = string + "suma = " + str(get_suma(cheltuiala)) + "\n"
    string = string + "tip = " + (get_tip(cheltuiala)) + "\n"
    return string