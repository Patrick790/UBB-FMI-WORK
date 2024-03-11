#include "Service.h"
#include <cassert>
#include <functional>
#include <algorithm>





/* Adauga masina
 * :param: registrationNumber: string
 * :return: -
 */
void carService::addCar(const string &registrationNumber, const string &producer, const string &model,
                        const string &type) {
    Car c{registrationNumber, producer, model, type};
    carValidator::validate(c);
    repo.store(c);
    undoActiuni.push_back(new undoAdauga(&repo, c));
}

/* Sterge masina
 * :param: poz: int
 * :return:-
 */
void carService::deleteCar(const int &poz) {
    auto dlt = repo.getAllCars()[poz];
    repo.remove(poz);
    undoActiuni.push_back(new undoSterge(&repo, dlt, poz));

}

/* Modifica masina
 * :param: poz: int
 * :param: registrationNumber: string
 * :param: producer: string
 * :param: model: string
 * :param: type: string
 * :return: -
 */
void carService::modifyCar(const int &poz, const string &registrationNumber, const string &producer,
                           const string &model, const string &type) {
    Car c{registrationNumber, producer, model, type};
    carValidator::validate(c);

    auto di = repo.getAllCars()[poz];
    repo.modify(c, poz);
    undoActiuni.push_back(new undoUpdate(&repo, di, poz));

}

/* Cauta masina dupa nr de inmatriculare
 * :param: registrationNumber: string
 * :return: masina cu nr de inmatriculare dat
 */
const Car &carService::find(const string& registrationNumber) {
    return repo.find(registrationNumber);

}

/* Filtreaza dupa producator
 * :param: producer: string
 * :return: lista de masini filtrata
 */
vector<Car> carService::filterProducer(const string& producer) {
    const vector<Car>& cars = getAllCars();
    vector<Car> filteredCars;
    std::copy_if(cars.begin(), cars.end(), back_inserter(filteredCars),
                 [producer](const Car& c){
                      return c.getProducer() == producer;
    });
    return filteredCars;

}

/* Filtreaza dupa tip
 * :param: type: string
 * :return: lista de masini filtrata
 */
vector<Car> carService::filterType(const string& type) {
    const vector<Car>& cars = getAllCars();
    vector<Car> filteredCars;
    std::copy_if(cars.begin(), cars.end(), back_inserter(filteredCars),
                 [type](const Car& c){
                     return c.getType() == type;
                 });
    return filteredCars;

}


vector<Car> carService::sortByRegistrationNumber() {
    auto sortedCopy = repo.getAllCars();
    sort(sortedCopy.begin(), sortedCopy.end(), cmpRegistrationNumber);
    return sortedCopy;

}

vector<Car> carService::sortByType() {
    auto sortedCopy = repo.getAllCars();
    sort(sortedCopy.begin(), sortedCopy.end(), cmpType);
    return sortedCopy;
}

vector<Car> carService::sortByProducerModel() {
    auto sortedCopy = repo.getAllCars();
    sort(sortedCopy.begin(), sortedCopy.end(), cmpProducerModel);
    return sortedCopy;
}

void carService::addToLista(string registrationNumber) {
    const auto& car = repo.find(registrationNumber);
    currentList.addCartoLista(car);
}

int carService::addRandomtoListaMasina(int cate) {
    currentList.addRandomMasini(this->getAllCars(), cate);
    return currentList.getallspalatorieMasini().size();
}

void carService::emptyListaMasina() {
    currentList.emptyList();
}


const vector<Car>& carService::getListaMasini() {
    return currentList.getallspalatorieMasini();
}

int carService::undo()
{
    if (undoActiuni.empty())
        return -1;

    ActiuneUndo* act = undoActiuni.back();
    act->doUndo();
    undoActiuni.pop_back();
    delete act;
    return 0;
}


bool carService::exportFile(const string filename, const string type)
{
    return repo.exportFisier(filename, type);
}

void testAddService(){
    CarRepo testRepo;
    carValidator testVal;
    carService testService{testRepo, testVal};

    testService.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");
    testService.addCar("MM 13 VSO", "Opel", "Astra", "Sedan");
    testService.addCar("CJ 78 PSH", "Skoda", "Octavia", "Sedan");

    assert(testService.getAllCars().size() == 3);

    try{
        testService.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");

    }
    catch (CarRepoException&){
        assert(true);
    }

    try{
        testService.addCar("CJ 82 JOY", "", "V50", "Combi");

    }
    catch (validateException& ve)
    {
        assert(ve.getErrorMessages() == "Invalid producer!\n");
    }
    testService.deleteCar(0);

    testService.modifyCar(1, "MM 13 VSO", "Skoda" , "Octavia", "Sedan");
}

void testFindService() {
    CarRepo testRepo;
    carValidator testVal;
    carService testService{testRepo, testVal};

    testService.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");
    testService.addCar("MM 13 VSO", "Opel", "Astra", "Sedan");
    testService.addCar("CJ 78 PSH", "Skoda", "Octavia", "Sedan");

    // Find an existing car
    const Car& foundCar = testService.find("CJ 21 NEO");
    assert(foundCar.getRegistrationNumber() == "CJ 21 NEO");
    assert(foundCar.getProducer() == "Volvo");
    assert(foundCar.getModel() == "V50");
    assert(foundCar.getType() == "Combi");

    // Find a non-existing car
    try {
        testService.find("CJ 99 DNG");
    }
    catch (CarRepoException &) {
        assert(true);
    }
}

void testFilterService() {
    CarRepo testRepo;
    carValidator testVal;
    carService testService{testRepo, testVal};

    testService.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");
    testService.addCar("NT 23 JOR", "Volvo", "XC-90", "SUV");
    testService.addCar("CJ 77 SUS", "Mazda", "6", "Combi");
    testService.addCar("MM 88 JOS", "Skoda", "Superb", "Sedan");

    vector<Car> carsByProducer = testService.filterProducer("Volvo");
    assert(carsByProducer.size() == 2);
    vector<Car> carsByType = testService.filterType("Combi");
    assert(carsByType.size() == 2);

}

void testSortService(){
    CarRepo testRepo;
    carValidator testVal;
    carService testService{testRepo, testVal};

    testService.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");
    testService.addCar("NT 23 JOR", "Volvo", "XC-90", "SUV");
    testService.addCar("CJ 77 SUS", "Mazda", "6", "Combi");
    testService.addCar("MM 88 JOS", "Skoda", "Superb", "Sedan");
    testService.addCar("CJ 23 APA", "Tesla", "Model 3", "Sedan");
    testService.addCar("SJ 65 URS", "Renault", "Austral", "SUV");

    vector<Car> sortedByRegistrationNumber = testService.sortByRegistrationNumber();
    assert(sortedByRegistrationNumber[0].getRegistrationNumber() == "CJ 21 NEO");
    assert(sortedByRegistrationNumber[1].getRegistrationNumber() == "CJ 23 APA");
    assert(sortedByRegistrationNumber[2].getRegistrationNumber() == "CJ 77 SUS");
    assert(sortedByRegistrationNumber[5].getRegistrationNumber() == "SJ 65 URS");

    vector<Car> sortedByType = testService.sortByType();
    assert(sortedByType[0].getRegistrationNumber() == "CJ 21 NEO");
    assert(sortedByType[0].getProducer() == "Volvo");
    assert(sortedByType[0].getModel() == "V50");

    assert(sortedByType[2].getRegistrationNumber() == "NT 23 JOR");
    assert(sortedByType[2].getProducer() == "Volvo");
    assert(sortedByType[2].getModel() == "XC-90");

    assert(sortedByType[5].getRegistrationNumber() == "CJ 23 APA");
    assert(sortedByType[5].getProducer() == "Tesla");
    assert(sortedByType[5].getModel() == "Model 3");

    vector<Car> sortedByProducerModel = testService.sortByProducerModel();
    assert(sortedByProducerModel[0].getRegistrationNumber() == "CJ 77 SUS");
    assert(sortedByProducerModel[0].getType() == "Combi");

    assert(sortedByProducerModel[2].getRegistrationNumber() == "MM 88 JOS");
    assert(sortedByProducerModel[2].getType() == "Sedan");

    assert(sortedByProducerModel[5].getRegistrationNumber() == "NT 23 JOR");
    assert(sortedByProducerModel[5].getType() == "SUV");

    testService.deleteCar(0);
    testService.deleteCar(1);
    testService.deleteCar(2);
    testService.deleteCar(3);
    testService.deleteCar(4);
    testService.deleteCar(5);
    vector<Car> sortedEmpty = testService.sortByRegistrationNumber();
    assert(sortedEmpty.empty() == true);

}

void testLista() {
    CarRepo testRepo;
    carValidator testVal;
    carService testService{ testRepo,testVal };

    testService.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");
    testService.addCar("NT 23 JOR", "Volvo", "XC-90", "SUV");
    testService.addCar("CJ 77 SUS", "Mazda", "6", "Combi");
    testService.addCar("MM 88 JOS", "Skoda", "Superb", "Sedan");
    testService.addCar("CJ 23 APA", "Tesla", "Model 3", "Sedan");
    testService.addCar("SJ 65 URS", "Renault", "Austral", "SUV");

    testService.addRandomtoListaMasina(4);
    assert(testService.getListaMasini().size() == 4);
    testService.emptyListaMasina();
    assert(testService.getListaMasini().size() == 0);

    testService.addRandomtoListaMasina(20);
    //putem adauga doar 6 masini (fara sa se repete)
    assert(testService.getListaMasini().size() == 6);

    testService.emptyListaMasina();
    testService.addToLista("SJ 65 URS");
    assert(testService.getListaMasini().size() == 1);

    /*try {
        testService.addToLista("SJ 65 URS");
        assert(false);
    }
    catch (CarRepoException&) {
        assert(true);
    }*/


}

void testUndo()
{
    auto* testRepo = new CarRepo();
    auto testVal = carValidator();
    auto testService = carService(*testRepo, testVal);

    testService.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");
    testService.modifyCar(0,"CJ 21 NEO", "Mazda", "6", "Sedan");
    testService.deleteCar(0);
    assert(testService.getAllCars().size() == 0);
    testService.undo();
    assert(testService.getAllCars().size() == 1);
    testService.undo();
    const Car car = testRepo->find("CJ 21 NEO");
    assert(car.getType() == "Combi");
    testService.undo();
    assert(testService.getAllCars().size() == 0);
    assert(testService.undo() == -1);

}

void testService(){
    testAddService();
    testFindService();
    testFilterService();
    testSortService();
    testLista();
    testUndo();
}