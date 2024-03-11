#pragma once
#include <vector>
#include <string>
#include <QtWidgets/QApplication>
#include <QLabel>
#include <QPushButton>
#include <QHBoxLayout>
#include <QFormLayout>
#include <QLineEdit>
#include <QTableWidget>
#include <QMessageBox>
#include <QHeaderView>
#include <QGroupBox>
#include <QRadioButton>
#include <QListWidget>
#include "Service.h"
#include "LstMasina.h"

using std::vector;
using std::string;

class ListaGUI:public QWidget{
private:

    listaMasina& rep;
    carService& srv;
    QHBoxLayout* recipe_main_layout = new QHBoxLayout;
    QListWidget* recipe_list;

    QLineEdit* lne_recipe;
    QPushButton* add_to_rec;
    QPushButton* empty_rec;
    QPushButton* random_add;
    QPushButton* export_recipe;
    QPushButton* help_button;
    void initGUI();
    void connectSignals();
    void reloadDis(vector<Car> car);
    void update() {
        reloadDis(rep.getallspalatorieMasini());
    }

public:
    ListaGUI(listaMasina& rep, carService& srv): srv{ srv }, rep{rep}{
        initGUI();
        connectSignals();
        reloadDis(rep.getallspalatorieMasini());
    }

};

class CarsGUI : public QWidget{
private:

    carService& srv;

    QLabel* lblRegistrationNumber = new QLabel{ "Registration number:" };
    QLabel* lblProducer = new QLabel("Producer:" );
    QLabel* lblModel = new QLabel( "Model:" );
    QLabel* lblType = new QLabel("Type:" );

    QLineEdit* editRegistrationNumber;
    QLineEdit* editProducer;
    QLineEdit* editModel;
    QLineEdit* editType;

    QPushButton* btnAddCar;

    QPushButton* btnRemoveCar;

    QPushButton* btnUpdateCar;

    QPushButton* btnUndo;

    QPushButton* btn_lst_mst;

    vector<ListaGUI* > rcp;

    QGroupBox* groupBox = new QGroupBox(tr("Tip sortare"));

    QRadioButton* radioSrtProducerModel = new QRadioButton(QString::fromStdString("Producer+Model"));
    QRadioButton* radioSrtRegistrationNumber = new QRadioButton(QString::fromStdString("Registration number"));
    QRadioButton* radioSrtType = new QRadioButton(QString::fromStdString("Type"));
    QPushButton* btnSortCars;

    QLabel* lblFilterProducer = new QLabel{ "Producatorul dupa care se filtreaza:"};
    QLineEdit* editFilterProducer;
    QLabel* lblFilterType = new QLabel{"Tipul dupa care se filtreaza:"};
    QLineEdit* editFilterType;
    QPushButton* btnFilterCars;

    QPushButton* btnReloadData;

    QTableWidget* tableCars;

    void initializeGUIComponents();

    void connectSignalsSlots();
    void reloadCarList(vector<Car> cars);

public:
    CarsGUI(carService& carSrv) : srv{ carSrv }{
        initializeGUIComponents();
        connectSignalsSlots();
        reloadCarList(srv.getAllCars());
    }

    void guiAddCar();
    void guiRemoveCar();
    void guiUptCar();
    void guiUndo();
};
