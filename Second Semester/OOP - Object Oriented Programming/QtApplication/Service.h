#pragma once

#include "Car.h"
#include "Repo.h"
#include "LstMasina.h"
#include <string>
#include <vector>

#include <functional>
#include "validator.h"

#include "Undo.h"

using std::vector;
using std::function;

class carService {
private:
    CarRepo& repo;
    carValidator& val;

    vector<ActiuneUndo*>undoActiuni;

    listaMasina currentList;

public:
    carService(CarRepo& carRepo, carValidator& val): repo {carRepo }, val {val } {}

    carService(const carService& ot) = default;

    void addCar(const string& registrationNumber, const string& producer, const string& model, const string& type);

    void deleteCar(const int& poz);

    void modifyCar(const int &poz, const string& registrationNumber, const string& producer, const string& model, const string& type);

    vector<Car>filterProducer(const string& producer);

    vector<Car>filterType(const string& type);

    const Car& find(const string& registrationNumber);

    vector<Car>sortByRegistrationNumber();
    vector<Car>sortByType();
    vector<Car>sortByProducerModel();

    vector<Car>& getAllCars(){
        return this->repo.getAllCars();
    }

    void addToLista(string registrationNumber);

    int addRandomtoListaMasina(int cate);

    void emptyListaMasina();

    const vector<Car>& getListaMasini();

    bool exportFile(const string filename, const string type);

    int undo();

    ~carService() = default;


};

void testService();

