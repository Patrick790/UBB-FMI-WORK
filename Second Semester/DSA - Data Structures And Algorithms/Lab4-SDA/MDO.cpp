#include "IteratorMDO.h"
#include "MDO.h"
#include <vector>

#include <exception>
using namespace std;

//tetha(1)
MDO::MDO(Relatie r) {
    /* de adaugat */
    rel = r;
    prim = nullptr;
    capacitate = 10;
    dimensiune = 0;
    tabela = new Node[capacitate];
}

//tetha(n)-worst case
void MDO::adauga(TCheie c, TValoare v) {
    /* Create a new node */
    Node* nod = new Node{ c, v, nullptr };

    /* Check if the multi-map is empty or if the new key is smaller than the first key */
    if (prim == nullptr || rel(c, prim->cheie)) {
        /* Insert the new node at the beginning */
        nod->urmator = prim;
        prim = nod;
    }
    else {
        /* Find the appropriate position to insert the new node */
        Node* anterior = prim;
        while (anterior->urmator != nullptr && rel(anterior->urmator->cheie, c))
            anterior = anterior->urmator;

        /* Insert the new node at the found position */
        nod->urmator = anterior->urmator;
        anterior->urmator = nod;
    }

    /* Resize the dynamic array if needed */
    if (dimensiune == capacitate) {
        /* Double the capacity */
        capacitate *= 2;

        /* Create a new temporary array with the updated capacity */
        Node* temp = new Node[capacitate];

        /* Copy the existing nodes to the temporary array */
        for (int i = 0; i < dimensiune; i++) {
            temp[i] = tabela[i];
        }

        /* Deallocate the memory used by the old array */
        delete[] tabela;

        /* Update the tabela pointer to the new array */
        tabela = temp;
    }

    /* Add the new node to the tabela array */
    tabela[dimensiune] = *nod;
    dimensiune++;
}


// caz favoranil : Tetha(1)
// caz defavorabil : Tetha(n)
// caz mediu : Tetha(n)
// overall case : O(n)
vector<TValoare> MDO::cauta(TCheie c) const {
    /* de adaugat */
    vector<TValoare> rezultat;
    Node* nod = prim;
    while (nod != nullptr && !rel(c, nod->cheie))
        nod = nod->urmator;
    while (nod != nullptr && nod->cheie == c) {
        rezultat.push_back(nod->valoare);
        nod = nod->urmator;
    }
    return rezultat;
}

// caz favoranil : Tetha(1)
// caz defavorabil : Tetha(n)
// caz mediu : Tetha(n)
// overall case : O(n)
bool MDO::sterge(TCheie c, TValoare v) {
    /* de adaugat */
    Node* nod = prim;
    Node* anterior = nullptr;
    while (nod != nullptr && !(nod->cheie == c && nod->valoare == v)) {
        anterior = nod;
        nod = nod->urmator;
    }
    if (nod == nullptr) {
        return false;
    }
    else {
        if (anterior == nullptr) {
            prim = nod->urmator;
        }
        else {
            anterior->urmator = nod->urmator;
        }

        // Update the dynamic array
        for (int i = 0; i < dimensiune; i++)
                if (i < dimensiune - 1)
                    tabela[i] = tabela[i + 1];
                else
                    tabela[i] = *nod;
    }

    dimensiune--;

    return true;
}

//tetha(1)
int MDO::dim() const {
    /* de adaugat */
    return dimensiune;
}

//tetha(1)
bool MDO::vid() const {
    /* de adaugat */
    return prim == nullptr;
}

//tetha(1)
IteratorMDO MDO::iterator() const {
    return IteratorMDO(*this);
}

//tetha(n)
MDO::~MDO() {
    /* de adaugat */
    while (prim != nullptr) {
        Node* nod = prim;
        prim = prim->urmator;
        delete nod;
    }
    delete[] tabela;
}
