#pragma once

#include <sstream>
#include <vector>
#include <fstream>
#include "Melodie.h"

using namespace std;


class FileRepo
{
private:
    string filename;
    vector<Melodie> melodii;

    ///Metoda care incarca in fisier
    void load();
    ///Metoda care salvceaza in fisier
    void save();

public:

    ///constructor
    FileRepo(string filename) : filename{ filename } {
        load();
    }

    /* Metoda care valideaza id-ul unei melodii pt ca acesta sa fie unic
     * param intrare: id(int)
     */
    void validateId(int id);

    /* Metoda care adauga o melodie
     * m - melodie
     */
    void add(Melodie m);

    /* Metoda care sterge o melodie
     * poz - pozitia pe care se afla melodia pe care dorim sa o stergem
     */
    void remove(int poz);

    int getNrMelodii(string gen);

    /*
     * Metoda care returneaza lista de melodii
     */
    vector<Melodie> & get_all();
};


class DuplicatedIdException
{
private:
    string message;
public:
    DuplicatedIdException(string message): message{ message }{}

    string getMessage() {
        return message;
    }
};

void test_repo();

int to_nr(string nr);
