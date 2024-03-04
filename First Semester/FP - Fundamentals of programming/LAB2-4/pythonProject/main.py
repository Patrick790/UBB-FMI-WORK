def toateelemsuntdesemncontrar(a):
    '''
    verifica daca oricare 2 elemente consecutive din sir au semne contrare
    :param a: lista de nr intregi
    :return: 1 daca oricare 2 nr consecutive sunt de semn contrar, 0 in caz contrar
    '''
    for i in range(len(a)-1):
        if a[i] < 0 and a[i+1] < 0:
            return 0
        elif a[i] > 0 and a[i+1] > 0:
            return 0
    return 1

def testtoateelemsuntdesemncontrar():
    assert(toateelemsuntdesemncontrar([1,-1,2,-2,3]) == 1)
    assert(toateelemsuntdesemncontrar([1,1,2,-2,3]) == 0)
    assert(toateelemsuntdesemncontrar([1,-1,2,-2,-7]) == 0)

def Ceamailungasecvdesemnecontrare(a):
    '''
    determina cea mai lunga secv de elem de semn contrar
    :param a: lista de nr intregi
    :return: secventa de lungime maxima
    '''
    secvmax = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            if toateelemsuntdesemncontrar(a[i:j + 1]) and len(a[i:j + 1]) > len(secvmax):
                secvmax = a[i:j + 1]
    return secvmax

def testCeamailungasecvdesemnecontrare():
    assert(Ceamailungasecvdesemnecontrare([1,-2,23,-4,-5])==[1,-2,23,-4])
    assert (Ceamailungasecvdesemnecontrare([1, -2, -23, -4, -5]) == [1,-2])
    assert (Ceamailungasecvdesemnecontrare([-1, -2, -23, -4, -5]) == [-1])



def toatedifausemncontrar(a):
    '''
    verifica daca toate nr din sir sunt de forma a[j]<a[j+1]>a[j+2] sau a[j]>a[j+1]<a[j+2]
    :param a: lista de nr intregi
    :return: 1 daca numerele sunt de forma specificata, 0 in caz contrar
    '''
    for i in range(len(a) - 2):
        if a[i] > a[i + 1]:
            if a[i + 1] > a[i + 2]:
                return 0
        elif a[i] < a[i + 1]:
            if a[i + 1] < a[i + 2]:
                return 0
    return 1


def testtoatedifausemncontrar():
    assert (toatedifausemncontrar([1, 3, 1, 5, 4, 8]) == 1)
    assert (toatedifausemncontrar([1, 2, 1, 5, 6]) == 0)
    assert (toatedifausemncontrar([8, 1, 5, 3, 6, 1]) == 1)


def Ceamailungasecvcudifcontrare(a):
    '''
    determina cea mai lunga secventa de nr de forma a[j]<a[j+1]>a[j+2] sau a[j]>a[j+1]<a[j+2]
    :param a: lista de nr intregi
    :return: secventa maxima de nr obtinuta
    '''
    secvmax = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            if toatedifausemncontrar(a[i:j + 1]) and len(a[i:j + 1]) > len(secvmax):
                secvmax = a[i:j + 1]
    return secvmax


def testCeamailungasecvcudifcontrare():
    assert (Ceamailungasecvcudifcontrare([4, 5, 6, 4, 7]) == [5, 6, 4, 7])
    assert (Ceamailungasecvcudifcontrare([4, 5, 6, 7]) == [4,5])
    assert (Ceamailungasecvcudifcontrare([3, 5, 3, 2, 5, 4, 11]) == [3, 2, 5, 4, 11])


def toatenrininterval(x, y, a):
    '''
    verifica daca nr din lista a apartin intervalului [x, y]
    :param x: nr intreg
    :param y: nr intreg
    :param a: lista de nr intregi
    :return: 1 daca toate nr din lista apartin intervalului, 0 in caz contrar
    '''
    for i in range(len(a)):
        if a[i] < x or a[i] > y:
            return 0
    return 1


def testtoatenrininterval():
    assert (toatenrininterval(0, 10, [1, 2, 3]) == 1)
    assert (toatenrininterval(2, 5, [6, 7, 8]) == 0)
    assert (toatenrininterval(1, 36, [21, 22, 34, 35]) == 1)


def Ceamailungasecvdenrdininterval(a):
    '''
    determina cea mai lunga secventa de nr care apartin unui interval
    :param a: lista de nr intregi
    :return: secventa maxima de nr obtinuta
    '''
    secvmax = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            if toatenrininterval(0, 10, a[i:j + 1]) and len(a[i:j + 1]) > len(secvmax):
                secvmax = a[i:j + 1]
    return secvmax


def testCeamailungasecvdenrdininterval():
    assert (Ceamailungasecvdenrdininterval([2, 3, 4, 5, 11, 2, 3]) == [2, 3, 4, 5])
    assert (Ceamailungasecvdenrdininterval([2, 12, 4, 5, 10, 2, 3, 23]) == [4, 5, 10, 2, 3])
    assert (Ceamailungasecvdenrdininterval([11, 23, 45, 11]) == [])


def print_meniu():
    print("1.Citirea unei liste de numere intregi")
    print("2.Afisare cea mai lunga secventa de numere dintr-un interval dat")
    print("3.Afisare cea mai lunga secventa de numere de forma a[j]<a[j+1]>a[j+2]")
    print("4.Afisare cea mai lunga secventa de numere cu oricare 2 elem consecutive de semn contrar")
    print("5.Iesire din aplicatie.")


def citeste_sir():
    a = []
    linie = (input("Dati nr din lista, separate printr-un spatiu: "))
    numere = linie.split(" ")
    for nr in numere:
        a.append(int(nr))
    return a


def main():
    a = []
    ruleaza = 1
    while ruleaza == 1:
        print_meniu()
        nr = int(input("Introdu unul din numerele:1, 2, 3, 4, 5: \n"))
        if nr == 1:
            a = citeste_sir()
        elif nr == 2:
            print(Ceamailungasecvdenrdininterval(a))
        elif nr == 3:
            print(Ceamailungasecvcudifcontrare(a))
        elif nr == 4:
            print(Ceamailungasecvdesemnecontrare(a))


        else:
            ruleaza = 0


testtoatenrininterval()
testCeamailungasecvdenrdininterval()
testtoatedifausemncontrar()
testCeamailungasecvcudifcontrare()
testtoateelemsuntdesemncontrar()
testCeamailungasecvdesemnecontrare()
main()
