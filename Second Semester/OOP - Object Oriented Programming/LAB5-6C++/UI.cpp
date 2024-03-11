
#include "UI.h"

#include "Car.h"
#include <iostream>
#include <string>

using namespace std;

void consoleUi::printSpalatorieMenu() {
    cout << "1. Add car in list" << endl;
    cout << "2. Add random car in list" << endl;
    cout << "3. Empty list" << endl;
    cout << "4. Print current list" << endl;
    cout << "5. Export" << endl;
}

void consoleUi::printMenu() {
    cout << "Available commands:" << endl;
    cout << "1. Print all cars" << endl;
    cout << "2. Add car" << endl;
    cout << "3. Delete car" << endl;
    cout << "4. Modify car" << endl;
    cout << "5. Find car" << endl;
    cout << "6. Filter cars" << endl;
    cout << "7. Sort cars" << endl;
    cout << "8. List menu" << endl;
    cout << "9. Undo" << endl;
    cout << "0. Exit" << endl;
}

void consoleUi::printCars(const vector<Car> &cars) {
    cout << "Cars:\n";
    for(const auto& c : cars){
        cout << " " << c.getRegistrationNumber() << " " << c.getProducer() << " " << c.getModel() << " " << c.getType() << "\n";
    }
    cout << "End of the list\n";

}

void consoleUi::uiAdd() {
    string registrationNumber, producer, model, type;

    cout << "Registration number: ";
    getline(cin >> ws, registrationNumber);
    cout << "Producer: ";
    getline(cin >> ws, producer);
    cout << "Model: ";
    getline(cin >> ws, model);
    cout << "Type: ";
    getline(cin >> ws, type);
    try{
        car.addCar(registrationNumber, producer, model, type);
        cout << "Successfully added\n";
    }
    catch(CarRepoException& ba){
        cout << ba.getErrorMessage();
    }
    catch (validateException& ve){
        cout << "The car is invalid \n";
        cout << ve.getErrorMessages();
    }

}

void consoleUi::uiDelete() {
    string registrationNumber, producer, model, type;
    cout << "Registration number: ";
    getline(cin >> ws, registrationNumber);
    cout << "Producer: ";
    getline(cin >> ws, producer);
    cout << "Model: ";
    getline(cin >> ws, model);
    cout << "Type: ";
    getline(cin >> ws, type);
    auto c = Car(registrationNumber, producer, model, type);

    int index = 0;

    for(auto& ca : car.getAllCars()){
        if(ca.getRegistrationNumber() == c.getRegistrationNumber()){
            break;
        }
        ++index;
    }
    if(index == car.getAllCars().size()){
        cout << "The car does not exist";
    }
    try{
        car.deleteCar(index);

    }
    catch (CarRepoException& ba)
    {
        cout << ba.getErrorMessage();
    }

}

void consoleUi::uiModify() {
    string registrationNumber, producer, model, type;
    cout << "Registration number of the car you want to modify: ";
    getline(cin >> ws, registrationNumber);
    cout << "New Producer: ";
    getline(cin >> ws, producer);
    cout << "New Model: ";
    getline(cin >> ws, model);
    cout << "New Type: ";
    getline(cin >> ws, type);
    int index = 0;
    for(auto& ca : car.getAllCars()){
        if(ca.getRegistrationNumber() == registrationNumber){
            break;
        }
        ++index;
    }
    if(index == car.getAllCars().size()){
        cout << "The given car does not exist!";
    }
    try{
        car.modifyCar(index, registrationNumber, producer, model, type);
        cout << "Successfully modified!\n";
    }
    catch (CarRepoException& ba){
        cout << ba.getErrorMessage();
    }
    catch (validateException& ve){
        cout << "The car with the given registration number does not exist!\n";
        cout << ve.getErrorMessages();
    }
}

void consoleUi::uiFind() {
    string registrationNumber;
    cout << "Registration number of the car you want to find: ";
    cin >> registrationNumber;
    try{
        const Car& c = car.find(registrationNumber);
        cout << " " << c.getRegistrationNumber() << " " << c.getProducer() << " " << c.getModel() << " " << c.getType() << "\n";

    }
    catch (CarRepoException& ba){
        cout << ba.getErrorMessage();
    }
}

void consoleUi::uiFilter() {
    cout << "Filter criteria is (producer/type): ";
    string criteria;
    cin >> criteria;

    if(criteria == "producer") {
        cout << "The producer for filtering cars: ";
        string producerFilter;
        cin >> producerFilter;
        printCars(car.filterProducer(producerFilter));
    }
    else if(criteria == "type") {
        cout << "The type for filtering cars: ";
        string typeFilter;
        cin >> typeFilter;
        printCars(car.filterType(typeFilter));
    }
    else
        cout << "Invalid filtering criteria!\n";
}

void consoleUi::uiSort() {
    cout << "Sort criteria is(registration/type/producer+model): ";
    string criteriu;
    cin >> criteriu;

    if( criteriu == "registration")
        printCars(car.sortByRegistrationNumber());
    else if (criteriu == "type")
        printCars(car.sortByType());
    else if(criteriu == "producer+model")
        printCars(car.sortByProducerModel());
    else
        cout << "Invalid criteria.\n";

}

void consoleUi::uiAddToLista() {
    string registrationNumber;
    cout << "Registration number is: ";
    getline(cin >> ws, registrationNumber);

    try{
        car.addToLista(registrationNumber);
        cout << "Car was successfully added in the list." << endl;
    }
    catch(CarRepoException& re){
        cout << re.getErrorMessage();
    }
    catch(validateException& ve){
        cout << "Invalid car!" << endl;
        cout << ve.getErrorMessages();
    }
}

void consoleUi::uiAddRandomToLista() {
    int cate;
    cout << "Number of cars to be added: ";
    cin >> cate;

    try{
        int cateadaugate = car.addRandomtoListaMasina(cate);
        cout << cateadaugate << " cars were added in the list " << endl;
    }
    catch(CarRepoException& re){
        cout << re.getErrorMessage();
    }
}

void consoleUi::uiEmptyLista() {
    car.emptyListaMasina();
    cout << "All cars were deleted from the current list." << endl;
}

void consoleUi::addDefaultCars() {
    car.addCar("CJ 21 NEO", "Volvo", "V50", "Combi");
    car.addCar("MM 13 VSO", "Opel", "Astra", "Sedan");
    car.addCar("CJ 78 PSH", "Skoda", "Octavia", "Sedan");
    car.addCar("CJ 99 DNG", "Mazda", "CX-30", "SUV");
    car.addCar("GJ 22 PAT", "Mazda", "CX-5", "SUV");

}

void consoleUi::exportCars()
{
    string filename, type;
    cout << "File name: ";
    cin >> filename;
    cout << "Extension (html/csv): ";
    cin >> type;
    if (car.exportFile(filename, type))
        cout << "\nSuccesfully exported!\n";
    else
        cout << "\nExport failed!\n";
}

void consoleUi::uiListaMasina() {
    int cmd;
    int runningList = 1;
    while (runningList) {
        printSpalatorieMenu();
        cout << "Command: ";
        cin >> cmd;
        switch (cmd)
        {
            case 1:
                uiAddToLista();
                break;
            case 2:
                uiAddRandomToLista();
                break;
            case 3:
                uiEmptyLista();
                break;
            case 4:
                printCars(car.getListaMasini());
                break;
            case 5:
                exportCars();
                break;
            case 6:
                runningList = 0;
                break;
            default:
                break;
        }
    }
}



void consoleUi::run() {
    int running = 1;
    int cmd;
    addDefaultCars();
    while(running){
        printMenu();
        cout << "Command: ";
        cin >> cmd;
        switch (cmd) {
            case 0:
                running = 0;
                break;
            case 1:
                printCars(car.getAllCars());
                break;
            case 2:
                uiAdd();
                break;
            case 3:
                uiDelete();
                break;
            case 4:
                uiModify();
                break;
            case 5:
                uiFind();
                break;
            case 6:
                uiFilter();
                break;
            case 7:
                uiSort();
                break;
            case 8:
                uiListaMasina();
                break;
            case 9:
                if(car.undo() == -1)
                {
                    cout << "Undo is not available!\n";
                }
                else
                {
                    printCars(car.getAllCars());
                }
                break;

            default:
                break;



        }
    }


}