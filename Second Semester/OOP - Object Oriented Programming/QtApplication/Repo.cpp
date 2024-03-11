
#include "Repo.h"
#include <cassert>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>


using namespace std;

using std::ostream;
using std::stringstream;
using std::getline;


bool CarRepo::exist(const Car &c) {
    try{
        find(c.getRegistrationNumber());
        return true;
    }
    catch (CarRepoException) {
        return false;
    }
}

bool CarRepo::exportFisier(const string filename, const string type)
{
    string numeFisier = filename + '.' + type;
    std::ofstream fout(numeFisier);
    if (type == "html" || type == "csv")
    {
        for (const Car& c : this->getAllCars())
        {
            fout << "Registration number: " << c.getRegistrationNumber() << " Producer: " << c.getProducer() << " Model: " << c.getModel() << " Type: " << c.getType() << endl;
        }
        return true;
    }
    return false;
}

const Car& CarRepo::find(const string& registrationNumber) {
    auto f = std::find_if(this->cars.begin(), this->cars.end(),
                          [=](const Car& c) {
                              return c.getRegistrationNumber() == registrationNumber ;
                          });
    if (f != this->cars.end())
        return (*f);
    else
        throw CarRepoException("The car with registration number " + registrationNumber + " does not exist in the list");
}

void CarRepo::store(const Car &c) {
    if(exist(c)){
        throw CarRepoException("The car with registration number " + c.getRegistrationNumber() + " produced by " + c.getProducer() + " model " + c.getModel() + " type " + c.getType() + " already exists!");
    }
    this->cars.push_back(c);
}


void CarRepo::remove(int poz) {
    this->cars.erase(cars.begin() + poz);
}

void CarRepo::modify(const Car &c, int poz) {
    this->cars[poz] = c;
}

vector<Car>& CarRepo::getAllCars() {
    return this->cars;
}


void FileRepo::loadFromFile() {
    ifstream carFile(this->filename);
    if(!carFile.is_open()) {
        throw CarRepoException("Cannot read from file " + filename);
    }
    string line;
    while(getline(carFile, line))
    {
        string registrationNumber, producer, model, type;

        stringstream linestream(line);
        string current_item;
        int item_no = 0;

        while(getline(linestream, current_item, ','))
        {
            if(item_no == 0) registrationNumber = current_item;
            if(item_no == 1) producer = current_item;
            if(item_no == 2) model = current_item;
            if(item_no == 3) type = current_item;
            item_no++;
        }
        Car c{ registrationNumber, producer, model, type};

        CarRepo::store(c);

    }
    carFile.close();
}

void FileRepo::saveToFile() {
    ofstream carOutput(this->filename);
    if(!carOutput.is_open())
        throw CarRepoException("Cannot write to file" + filename);
    for(auto& car : getAllCars()) {
        carOutput << car.getRegistrationNumber() << "," << car.getProducer() << ",";
        carOutput << car.getModel() << "," << car.getType() << endl;
    }
    carOutput.close();
}

void testAddRepo(){
    CarRepo testRepo;

    Car car1{ "CJ 21 NEO", "Volvo", "V50", "Combi"};

    testRepo.store(car1);
    assert(testRepo.getAllCars().size() == 1);

    Car car2{ "MM 13 VSO", "Opel", "Astra", "Sedan"};
    Car car3{ "CJ 21 NEO", "Volvo", "V50", "Combi" };
    try{
        testRepo.store(car3);
    }
    catch (CarRepoException){
        assert(true);
    }

}

void FileRepo::store(const Car &c) {
    CarRepo::store(c);
    saveToFile();
}

void FileRepo::remove(int poz) {
    CarRepo::remove(poz);
    saveToFile();
}

void FileRepo::modify(const Car &c, int poz) {
    CarRepo::modify(c, poz);
    saveToFile();
}



void testFindRepo(){
    CarRepo testRepo;
    Car car1{ "CJ 21 NEO", "Volvo", "V50", "Combi"};
    Car car2{ "MM 13 VSO", "Opel", "Astra", "Sedan"};
    Car car3{ "CJ 78 PSH", "Skoda", "Octavia", "Sedan"};
    Car car4{ "CJ 12 OHJ", "Renault", "Austral", "SUV"};
    Car car5{ "CJ 79 ADF", "Skoda", "Superb", "Sedan"};
    testRepo.store(car1);
    testRepo.store(car2);
    testRepo.store(car4);

    assert(testRepo.exist(car1));
    assert(!testRepo.exist(car3));
    testRepo.remove(1);
    testRepo.modify(car5, 1);
    testRepo.modify(car4,1);

    auto foundCar = testRepo.find("CJ 21 NEO");
    assert(foundCar.getRegistrationNumber() == "CJ 21 NEO");
    assert(foundCar.getProducer() == "Volvo");
    assert(foundCar.getModel() == "V50");
    assert(foundCar.getType() == "Combi");

}

void testDeleteRepo(){

    CarRepo testRepo;

    Car car1{ "CJ 21 NEO", "Volvo", "V50", "Combi"};
    Car car2{ "MM 13 VSO", "Opel", "Astra", "Sedan"};
    Car car3{ "CJ 78 PSH", "Skoda", "Octavia", "Sedan"};
    testRepo.store(car1);
    testRepo.store(car2);

    assert(testRepo.getAllCars().size() == 2);
    testRepo.remove(1);
    assert(testRepo.getAllCars().size() == 1);

}

void testModifyRepo() {
    CarRepo testRepo;

    Car car1{ "CJ 21 NEO", "Volvo", "V50", "Combi"};
    Car car2{ "MM 13 VSO", "Opel", "Astra", "Sedan"};
    testRepo.store(car1);
    testRepo.store(car2);

    Car modifiedCar{ "CJ 21 NEO", "Volvo", "XC60", "SUV"};
    testRepo.modify(modifiedCar, 0);

    auto foundCar = testRepo.find("CJ 21 NEO");
    assert(foundCar.getRegistrationNumber() == "CJ 21 NEO");
    assert(foundCar.getProducer() == "Volvo");
    assert(foundCar.getModel() == "XC60");
    assert(foundCar.getType() == "SUV");
}





void testRepo(){
    testAddRepo();
    testFindRepo();
    testDeleteRepo();
    testModifyRepo();
}



