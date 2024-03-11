#include <QApplication>
#include <QPushButton>
#include <QtWidgets/QApplication>
#include "CarsGUI.h"
#include "Car.h"
#include "Repo.h"
#include "Service.h"
#include "qtwidgetsapplication.h"
#include <cstdlib>
#include <iostream>
using std::cout;
using std::endl;

void testAll(){
    testDomain();
    testRepo();
    testService();
    cout << "Finished tests" << endl;

}


int main(int argc, char *argv[]) {
    testAll();
    QApplication a(argc, argv);
    FileRepo repoFile{ "cars.txt"};

    carValidator val;
    carService srv{ repoFile, val};
    CarsGUI gui{ srv };

    gui.show();
    return QApplication::exec();
}
