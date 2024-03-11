#pragma once
#include <string>
#include <iostream>
#include <cassert>

using std::string;
using std::cout;

class Car{
    std::string registrationNumber;
    std::string producer;
    std::string model;
    std::string type;

public:

    Car() = default;
    Car(const string r, const string p, const string m, const string t) : registrationNumber{ r }, producer{ p }, model{ m }, type{ t }{}

    Car(const Car& ot) : registrationNumber{ot.registrationNumber }, producer{ot.producer }, model{ot.model }, type{ot.type }{

    }

    string getRegistrationNumber() const {
        return registrationNumber;
    }

    string getProducer() const {
        return producer;
    }

    string getModel() const {
        return model;
    }

    string getType() const {
        return type;
    }

    void setRegistrationNumber(string newRegistrationNr);
    void setProducer(string newProducer);
    void setModel(string newModel);
    void setType(string newType);

    bool operator==(const Car& ot);



};

bool cmpRegistrationNumber(const Car& c1, const Car& c2);

bool cmpType(const Car& c1, const Car& c2);

bool cmpProducerModel(const Car& c1, const Car& c2);

//bool cmpProducer(const Car& c1, const Car& c2);

void testDomain();