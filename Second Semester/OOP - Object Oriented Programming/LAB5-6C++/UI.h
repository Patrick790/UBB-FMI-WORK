#pragma once

#include "Service.h"
#include "Car.h"
#include "Repo.h"

class consoleUi {
private:
    carService& car;

public:
    explicit consoleUi(carService& car) : car{car }{}
    consoleUi(const consoleUi& ot) = delete;

    static void printMenu();
    void uiAdd();
    void uiDelete();
    void uiModify();
    void uiFind();
    void uiFilter();
    void uiSort();
    void uiAddToLista();
    void uiAddRandomToLista();
    void uiEmptyLista();
    void uiListaMasina();
    void addDefaultCars();
    void exportCars();
    static void printCars(const vector<Car>& cars);
    void run();


    static void printSpalatorieMenu();
};