#include "Repo.h"


void FileRepo::validateId(int id) {
    bool found = false;
    for (auto &m: melodii) {
        if (m.getId() == id) {
            found = true;
            break;
        }
    }
    if (found) {
        throw DuplicatedIdException("Nu sunt permise 2 id-uri identice");
    }
}

int to_nr(string s) {
    int rez = 0;
    int sign = 1;
    if (s[0] == '-') {
        sign = -1;
        s.erase(s.begin());
    }
    for (auto &ch:s) {
        if (!('0' <= ch && ch <= '9')) {
            throw ValidationException("Id-ul trebuie sa fie intreg");
        }
        rez = rez * 10 + (ch - '0');
    }
    return rez * sign;
}

void FileRepo::load() {

    ifstream f(filename);
    string line;
    while (getline(f, line)) {
        if (line.empty()) {
            continue;
        }
        auto ss = stringstream(line);
        vector<string> elems;
        string elem;
        while (getline(ss, elem, ';')) {
            elems.push_back(elem);
        }
        auto m = Melodie(to_nr(elems[0]), elems[1], elems[2], elems[3]);
        add(m);
    }
    f.close();
}

void FileRepo::add(Melodie m) {
    melodii.push_back(m);
    save();
}

void FileRepo::remove(int poz) {
    this->melodii.erase(melodii.begin() + poz);
    save();
}



void FileRepo::save() {
    ofstream f(filename);
    for (auto &m: melodii) {
        f << m.getId() << ";" << m.getTitlu() << ";" << m.getArtist() << ";" << m.getGen() << "\n";
    }
    f.close();
}

vector<Melodie> & FileRepo::get_all() {
    return melodii;
}

int FileRepo::getNrMelodii(string gen) {
    int k = 0;
    for(const auto& m : melodii){
        if(m.getGen() == gen)
            k++;
    }
    return k;
}

void test_repo(){

    auto fr = FileRepo("test.txt");
    auto all = fr.get_all();
    assert(all.size() == 4);

    fr.add( Melodie(5, "Enter Sandman", "Metallica", "rock"));
    all = fr.get_all();

    assert(all.size() == 5);

    try {
        fr.validateId(5);
        assert(false);
    } catch (DuplicatedIdException &e) {
        assert(true);
    }
    assert(to_nr("12") == 12);
    assert(to_nr("-9") == -9);
}


