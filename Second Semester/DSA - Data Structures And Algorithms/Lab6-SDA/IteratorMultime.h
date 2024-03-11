#pragma once
#include <vector>
#include <list>
class Multime;
typedef int TElem;

class IteratorMultime
{
    friend class Multime;
private:

    //contine o referinta catre containerul pe care il itereaza
    const Multime& multime;
    /* aici e reprezentarea  specifica a iteratorului */
    int pozitieCurenta;
    int pozitieAnterioara;
    typename std::list<TElem>::const_iterator itCurent;


public:

    //reseteaza pozitia iteratorului la inceputul containerului
    void prim();

    //muta iteratorul in container
    // arunca exceptie daca iteratorul nu e valid
    void urmator();

    void anterior();

    //verifica daca iteratorul e valid (indica un element al containerului)
    bool valid() const;

    //returneaza valoarea elementului din container referit de iterator
    //arunca exceptie daca iteratorul nu e valid
    TElem element() const;

//constructorul primeste o referinta catre Container
//iteratorul va referi primul element din container
IteratorMultime(const Multime& m);
};
