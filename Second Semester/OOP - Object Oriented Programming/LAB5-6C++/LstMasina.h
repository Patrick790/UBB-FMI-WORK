#pragma once
#include "Car.h"
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

using std::vector;

class listaMasina {
private:
    vector<Car> spalatorieMasini;
public:
    listaMasina() = default;



    void addCartoLista(const Car& c);


    void emptyList();


    void addRandomMasini(vector<Car> originalMasini, int cate);

    const vector<Car>& getallspalatorieMasini();


};
