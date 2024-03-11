#include "Melodie.h"


int Melodie::getId() const {
    return id;
}

string Melodie::getTitlu() const {
    return titlu;
}

string Melodie::getArtist() const {
    return artist;
}

string Melodie::getGen() const {
    return gen;
}

void Melodie::validate(int id, const string& titlu, const string& artist, const string& gen) {
    string exc="";
    if(titlu.empty()){
        exc+="Titlul nu poate fi vid\n";
    }
    if(artist.empty()){
        exc+="Starea nu poate fi vida\n";
    }
    if(gen!="pop" && gen!="rock" && gen!="folk" && gen!="disco"){
        exc+="Genul nu poate fi decat pop, rock, folk sau disco\n";
    }
    if(!exc.empty()){
        throw ValidationException(exc);
    }
}


void test_domain() {
    Melodie m{1, "Praise the Lord", "Asap Rocky", "pop"};
    assert(m.getId() == 1);
    assert(m.getTitlu() == "Praise the Lord");
    assert(m.getArtist() == "Asap Rocky");
    assert(m.getGen() == "pop");
    Melodie::validate(1, "Praise the Lord", "Asap Rocky", "pop");
}