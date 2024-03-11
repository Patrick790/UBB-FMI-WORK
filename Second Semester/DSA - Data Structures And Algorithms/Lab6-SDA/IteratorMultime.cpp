#include "IteratorMultime.h"
#include "Multime.h"

IteratorMultime::IteratorMultime(const Multime& m) : multime(m) {
    prim();
    pozitieAnterioara = -1;
}

void IteratorMultime::prim() {
    /* Set the current position to 0 */
    pozitieCurenta = 0;

    /* Find the next non-empty set */
    while (pozitieCurenta < multime.capacitate && multime.tabela[pozitieCurenta].empty()) {
        ++pozitieCurenta;
    }

    /* Check if the current position is within the valid range */
    if (pozitieCurenta < multime.capacitate) {
        /* Set the iterator to the beginning of the current set */
        itCurent = multime.tabela[pozitieCurenta].begin();
    }
    else {
        /* All sets are empty, set the iterator to the end of the first set in the table */
        itCurent = multime.tabela[0].end();
    }

    /* Set the previous position to -1 */
    pozitieAnterioara = -1;
}


void IteratorMultime::urmator() {
    /* Check if the current position is within the valid range */
    if (pozitieCurenta < multime.capacitate) {
        /* Move the iterator to the next element in the current set */
        ++itCurent;

        /* Check if the iterator has reached the end of the current set */
        if (itCurent == multime.tabela[pozitieCurenta].end()) {

            ++pozitieCurenta;


            while (pozitieCurenta < multime.capacitate && multime.tabela[pozitieCurenta].empty()) {
                ++pozitieCurenta;
            }

            /* Check if a non-empty set is found at the new current position */
            if (pozitieCurenta < multime.capacitate) {
                /* Set the iterator to the beginning of the new set */
                itCurent = multime.tabela[pozitieCurenta].begin();
            }
            else {
                /* All sets are empty, set the iterator to the end of the first set in the table */
                itCurent = multime.tabela[0].end();
            }
        }
    }

    /* Set the previous position to -1 */
    pozitieAnterioara = -1;
}


void IteratorMultime::anterior() {
    if (!valid()) {
        throw std::exception();
    }

    if (pozitieCurenta == 0 && itCurent == multime.tabela[0].begin()) {
        // Iterator is already at the first element
        pozitieAnterioara = -1;
        return;
    }

    if (pozitieAnterioara != -1) {
        // We have a valid previous position, so move the iterator there
        --itCurent;
        pozitieCurenta = pozitieAnterioara;
        pozitieAnterioara = -1;
    } else {
        // Set the previous position and move the iterator to the previous element
        pozitieAnterioara = pozitieCurenta;
        --itCurent;
    }
}

TElem IteratorMultime::element() const {
    if (!valid()) {
        throw std::exception();
    }

    return *itCurent;
}

bool IteratorMultime::valid() const {
    return pozitieCurenta < multime.capacitate && itCurent != multime.tabela[pozitieCurenta].end();
}