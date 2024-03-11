#include "Multime.h"
#include "IteratorMultime.h"

#include <list>
#include <iostream>

Multime::Multime() {
    /* de adaugat */
    capacitate = 10;
    dimensiune = 0;
    tabela.resize(capacitate);
}

//tetha(1)
int Multime::hash(TElem elem) const {
    return abs(elem) % capacitate;
}

//overall-O(n)
bool Multime::adauga(TElem elem) {
    /* de adaugat */
    int pozitie = hash(elem);
    for (const auto& el : tabela[pozitie]) {
        if (el == elem) {
            // Elementul exista deja in multime
            return false;
        }
    }

    tabela[pozitie].push_back(elem);
    dimensiune++;
    return true;

}

//overall- O(n)
bool Multime::sterge(TElem elem) {
    /* de adaugat */
    int pozitie = hash(elem);
    for (auto it = tabela[pozitie].begin(); it != tabela[pozitie].end(); ++it) {
        if (*it == elem) {
            tabela[pozitie].erase(it);
            dimensiune--;
            return true;
        }
    }
    return false;
}

//overall - O(n)
bool Multime::cauta(TElem elem) const {
    /* de adaugat */
    int pozitie = hash(elem);
    for (const auto& el : tabela[pozitie]) {
        if (el == elem) {
            return true;
        }
    }
    return false;
}

//tetha(1)
int Multime::dim() const {
    /* de adaugat */
    return dimensiune;
}

//tetha(1)
bool Multime::vida() const {
    /* de adaugat */
    return dimensiune == 0;
}


Multime::~Multime() {
    /* de adaugat */
    tabela.clear();
}



IteratorMultime Multime::iterator() const {
    return IteratorMultime(*this);
}

