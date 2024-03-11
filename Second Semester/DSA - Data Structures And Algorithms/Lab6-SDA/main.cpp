#include <iostream>
#include "TestScurt.h"
#include "TestExtins.h"
#include "Multime.h"
#include "IteratorMultime.h"
#include <cassert>
int main() {
    testAll();
    testAllExtins();
    Multime m;
    m.adauga(10);
    m.adauga(20);
    m.adauga(30);
    IteratorMultime it(m);
   /* try{
        it.anterior();
        assert(false);
    }catch (const std::exception& e){ }*/

    assert(it.element() == 10);

    it.urmator();
    it.anterior();
    assert(it.element() == 10);

    std::cout<< "Teste rulate cu succes!";

}
