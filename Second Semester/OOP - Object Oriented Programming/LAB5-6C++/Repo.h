#pragma once
#include "Car.h"
#include "validator.h"

#include <vector>
#include <string>
#include <ostream>
#include <map>

using std::vector;
using std::string;
using std::ostream;
using namespace std;


class CarRepo{

private:

    vector<Car> cars;

public:

    CarRepo() = default;

    CarRepo(const CarRepo& ot) = delete;

    //store car in repo
    void store(const Car& c);

    //remove car from repo
    void remove(int poz);

    //modify car
    void modify(const Car& c, int poz);

    /*
	Cauta
	arunca exceptie daca nu exista disciplina
	*/
    const Car& find(const string& registrationNumber);

    bool exist(const Car& c);

    vector<Car>& getAllCars();

    ~CarRepo() = default;


    bool exportFisier(const string filename, const string type);
};

class FileRepo :public CarRepo{
private:
    string filename;

    void loadFromFile();

    void saveToFile();

public:
    FileRepo() = default;

    explicit FileRepo(string fn);

    ~FileRepo()  = default;

    void store(const Car& c){
        CarRepo::store(c);
        saveToFile();
    }

    void remove(int poz){
        CarRepo::remove(poz);
        saveToFile();
    }

    void modify(const Car& c, int poz){
        CarRepo::modify(c,poz);
        saveToFile();
    }




};
/*
Folosit pentru a semnala situatii exceptionale care pot aparea in repo
*/
class CarRepoException {
private:
    string errorMsg;
public:
    CarRepoException(string errorMsg) :errorMsg{ errorMsg } {};
    string getErrorMessage() {
        return this->errorMsg;
    }
};


void testRepo();
