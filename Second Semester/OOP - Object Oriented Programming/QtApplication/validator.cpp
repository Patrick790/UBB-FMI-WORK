#include "validator.h"


void carValidator::validate(const Car &c) {
    vector<string> msgs;
    if(c.getRegistrationNumber().size() < 8)
        msgs.emplace_back("Invalid registration number!");
    if(c.getProducer().empty())
        msgs.emplace_back("Invalid producer!");
    if(c.getModel().empty())
        msgs.emplace_back("Invalid model!");
    if(c.getType().empty())
        msgs.emplace_back("Invalid type!");
    if (!msgs.empty()) {
        throw validateException(msgs);
    }

}


void testValidator(){
    carValidator val;

    Car car1{"CJ 21 NEO", "Volvo", "V50", "Combi"};
    val.validate(car1);

    Car c2{ "CJ 21 A", "Volvo", "V60", "Combi" };
    try{
        val.validate(c2);
    }
    catch (validateException& ve){
        assert(ve.getErrorMessages() == "Invalid registration number!\n");
    }

    Car c3{ "CJ 21 ABC", "", "V60", "Combi" };
    try {
        val.validate(c3);
    }
    catch (validateException& e) {
        assert(e.getErrorMessages() == "Invalid producer!\n");
    }

    Car c4{ "CJ 21 ABC", "Volvo", "", "Combi" };
    try {
        val.validate(c4);
    }
    catch (validateException& e) {
        assert(e.getErrorMessages() == "Invalid model!\n");
    }

    Car c5{ "CJ 21 ABCD", "Volvo", "V60", "" };
    try {
        val.validate(c5);
    }
    catch (validateException& e) {
        assert(e.getErrorMessages() == "Invalid type!\n");
    }

}
