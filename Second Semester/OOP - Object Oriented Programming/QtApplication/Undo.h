#pragma once
#include "Car.h"
#include "Repo.h"
#include <vector>
#include <algorithm>

using std::vector;

class ActiuneUndo{
public:
    virtual void doUndo() = 0;
    ~ActiuneUndo() = default;
};

class undoAdauga : public ActiuneUndo
{
    Car masinaAdaugata;
    CarRepo* repo;

public:
    undoAdauga(CarRepo* repo, const Car& car) : repo{ repo }, masinaAdaugata{ car }{}
    void doUndo() override
    {
        int i = 0;
        for(auto& it : repo->getAllCars()){
            if(it == masinaAdaugata){
                break;
            }
            ++i;
        }
        repo->remove(i);
    }
};


class undoSterge : public ActiuneUndo
{
    Car masinaStearsa;
    CarRepo* repo;
    int poz;

public:

    undoSterge(CarRepo* repo, const Car& car, const int poz) : repo{ repo }, masinaStearsa{ car }, poz{poz}{}
    void doUndo() override
    {
        auto it = repo->getAllCars().begin();
        it += poz;
        repo->getAllCars().insert(it, masinaStearsa);
    }
};

class undoUpdate : public ActiuneUndo
{
    Car masinaModificata;
    CarRepo* repo;
    int poz;

public:
    undoUpdate(CarRepo* repo, const Car& car, const int p) : repo{ repo }, masinaModificata{ car }, poz{p}{}
    void doUndo() override
    {
        repo->modify(masinaModificata, poz);
    }
};
