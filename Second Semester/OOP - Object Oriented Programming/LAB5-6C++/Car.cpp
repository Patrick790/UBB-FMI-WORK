#include "Car.h"

void Car::setRegistrationNumber(string newRegistrationNr) {
    this->registrationNumber = newRegistrationNr;
}

void Car::setProducer(string newProducer) {
    this->producer = newProducer;
}

void Car::setModel(string newModel) {
    this->model = newModel;
}

void Car::setType(string newType) {
    this->type = newType;
}

bool Car::operator==(const Car& ot)
{
    if (registrationNumber == ot.registrationNumber && producer == ot.producer && model == ot.model && type == ot.type)
    {
        return true;
    }
    return false;

}

bool cmpRegistrationNumber(const Car& c1, const Car& c2)
{
    return c1.getRegistrationNumber() < c2.getRegistrationNumber();
}

bool cmpType(const Car& c1, const Car& c2)
{
    return c1.getType() < c2.getType();
}

bool cmpProducerModel(const Car& c1, const Car& c2) {
     if(c1.getProducer() == c2.getProducer())
         return c1.getModel() < c2.getModel();
     else
         return c1.getProducer() < c2.getProducer();
}

/*bool cmpProducerModel(const Car& c1, const Car& c2) {
    if (c1.getProducer() < c2.getProducer()) {
        return true;
    }
    else if (c1.getProducer() == c2.getProducer()) {
        return c1.getModel() < c2.getModel();
    }
    else {
        return false;
    }
}*/

/*(bool cmpProducer(const Car& c1, const Car& c2){
    return c1.getProducer() < c2.getProducer();
}*/

void testGetSet(){
    Car car1{"CJ 21 NEO", "Volvo", "V50", "Combi"};
    assert(car1.getRegistrationNumber() == "CJ 21 NEO");
    assert(car1.getProducer() == "Volvo");
    assert(car1.getModel() == "V50");
    assert(car1.getType() == "Combi");

    Car car2{"CJ 67 ZDK", "Mazda", "3", "Hatchback"};
    assert(car2.getRegistrationNumber() == "CJ 67 ZDK");
    assert(car2.getProducer() == "Mazda");
    assert(car2.getModel() == "3");
    assert(car2.getType() == "Hatchback");

    car2.setRegistrationNumber("B 22 IFK");
    car2.setProducer("BMW");
    car2.setModel("Seria 4");
    car2.setType("Coupe");

    assert(car2.getRegistrationNumber() == "B 22 IFK");
    assert(car2.getProducer() == "BMW");
    assert(car2.getModel() == "Seria 4");
    assert(car2.getType() == "Coupe");


}

void testCarOperatorEquals() {
    Car car1{"CJ 21 NEO", "Volvo", "V50", "Combi"};
    Car car2{"CJ 21 NEO", "Volvo", "V50", "Combi"};
    Car car3{"CJ 21 NEP", "Volvo", "V50", "Combi"};
    Car car4{"CJ 21 NEO", "Opel", "Astra", "Sedan"};

    assert(car1 == car2);
    assert(!(car1 == car3));
    assert(!(car1 == car4));
}

void testDomain(){
    testGetSet();
    testCarOperatorEquals();
}