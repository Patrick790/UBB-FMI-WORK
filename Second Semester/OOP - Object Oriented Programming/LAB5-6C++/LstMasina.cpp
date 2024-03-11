#include "LstMasina.h"
using std::shuffle;



void listaMasina::addCartoLista(const Car& c) {
    this->spalatorieMasini.push_back(c);
}

void listaMasina::emptyList() {
    this->spalatorieMasini.clear();
}

void listaMasina::addRandomMasini(vector<Car> originalMasini, int cate) {
    shuffle(originalMasini.begin(), originalMasini.end(), std::default_random_engine(std::random_device{}())); //amesteca vectorul v
    while(spalatorieMasini.size() < cate && !originalMasini.empty()){
        spalatorieMasini.push_back(originalMasini.back());
        originalMasini.pop_back();
    }
}

const vector<Car>& listaMasina::getallspalatorieMasini() {
    return this->spalatorieMasini;
}


