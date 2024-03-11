#include "Service.h"
#include <algorithm>

void Service::add(int id, std::string titlu, std::string artist, std::string gen) {
    Melodie::validate(id, titlu, artist, gen);
    repo.validateId(id);

    repo.add(Melodie(generareId(), titlu, artist, gen));
    notify();
}

void Service::remove(const int &poz) {
    auto dlt = repo.get_all()[poz];
    repo.remove(poz);
    notify();
}

int Service::generareId() {
    int id = 0;
    vector<Melodie> mel = repo.get_all();
    int size = mel.size();
    id = size+1;
    return id;
}


vector<Melodie> &Service:: getAll(){
    return repo.get_all();
}

void Service::validateIdd(int id) {
    repo.validateId(id);
}

void test_service(){
    auto rp=FileRepo{"service.txt"};
    auto srv=Service{rp};
    assert(srv.getAll().size()==6);

    srv.add(16,"Lush Life","Zara Larsson","pop");
    assert(srv.getAll().size()==6);


    try{
        srv.add(6,"sa","gfas","sagf");
        assert(false);
    } catch(ValidationException& ve){
        assert(true);
    }


}


