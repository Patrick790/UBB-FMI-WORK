#include <fstream>
#include "LstMasina.h"
using std::shuffle;
using namespace std;



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

void listaMasina::save_to_file(const std::string &filename) {
    ofstream fout(filename);
    fout << "First car\n";
    fout << "Nrcrt. Registration number Producer Model Type\n";
    int i = 0;
    for(auto& car : spalatorieMasini){
        fout << i++ << " " << car.getRegistrationNumber() << "," << car.getProducer() << "," << car.getModel() << "," << car.getType();
    }

}

