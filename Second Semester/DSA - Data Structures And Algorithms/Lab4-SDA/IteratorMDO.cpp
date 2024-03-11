#include "IteratorMDO.h"
#include "MDO.h"

//tetha(1)
IteratorMDO::IteratorMDO(const MDO& d) : dict(d){
    /* de adaugat */
    nod_curent = d.prim;
    pozitie_curenta = 0;
}

//tetha(1)
void IteratorMDO::prim(){
    /* de adaugat */
    nod_curent = dict.prim;
    pozitie_curenta = 0;
}

//tetha(1)
void IteratorMDO::urmator() {
    /* Check if the iterator is valid */
    if (!valid()) {
        throw exception();
    }

    /* Check if there are multiple values for the current key */
    if (nod_curent->urmator != nullptr && nod_curent->cheie == nod_curent->urmator->cheie) {
        /* Move to the next value for the current key */
        nod_curent = nod_curent->urmator;
    }
    else {
        /* Move to the next position  */
        pozitie_curenta++;

        if (pozitie_curenta < dict.dim()) {
            /* Update the nod_curent pointer to the node at the current position */
            nod_curent = &dict.tabela[pozitie_curenta];
        }
        else {
            /* Set the nod_curent pointer to nullptr to indicate the end of the iterator */
            nod_curent = nullptr;
        }
    }
}

//tetha(1)
bool IteratorMDO::valid() const{
    /* de adaugat */
    return nod_curent != nullptr || pozitie_curenta < dict.dim();
}

//tetha(1)
TElem IteratorMDO::element() const{
    /* de adaugat */
    if (!valid()) {
        throw exception();
    }

    return make_pair(nod_curent->cheie, nod_curent->valoare);
}
