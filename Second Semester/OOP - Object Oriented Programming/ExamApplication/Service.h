#include "Melodie.h"
#include "Repo.h"
#include "Observer.h"

class Service:public Observable{
private:
    FileRepo& repo;
public:
    ///constructor
    Service(FileRepo& rp): repo{rp}{}

    /*
     * Metoda de adaugare melodie
     * id: int
     * titlu: string
     * artist: string
     * gen: string
     * return: -
     */
    void add(int id, string titlu, string artist, string gen);

    /*
     * Metoda de remove melodie in service
     * poz: pozitia pe care se afla melodia pe care dorim sa o stergem
     */
    void remove(const int& poz);

    ///get all
    vector<Melodie>& getAll();

    ///Metoda care valideaza id pt a nu exista 2 id-uri identice
    void validateIdd(int id);

    int generareId();

};

void test_service();
