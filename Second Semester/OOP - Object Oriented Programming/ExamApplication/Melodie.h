#pragma once

#include <string>
#include <iostream>
#include <ostream>
#include <cassert>

using namespace std;

class Melodie
{
private:
    int id;
    string titlu;
    string artist;
    string gen;

public:
    ///constructor
    Melodie(int id, string titlu, string artist, string gen) : id{ id }, titlu{ titlu }, artist{ artist }, gen{ gen } {}

    ///metoda care returneaza id-ul unei melodii
    int getId() const;

    ///metoda care returneaza titlul(string) unei melodii
    string getTitlu() const;

    ///metoda care returneaza artistul(string) unei melodii
    string getArtist() const;

    ///metoda care returneaza genul(string) unei melodii
    string getGen() const;

    /* Meroda de validare a datelor introduse
     * id: int
     * titlu: string
     * artist: string
     * gen : string
     * daca datele nu sunt valide arunca validation error
     */
    static void validate(int id, const string& titlu, const string& artist, const string& gen);

};


class ValidationException
{
private:
    string message;

public:
    ValidationException(string message) : message{ message } {}

    ///getter mesaj de validare
    string getMessage() {
        return message;
    }
};

void test_domain();
