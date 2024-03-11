#include "CarsGUI.h"

void CarsGUI::initializeGUIComponents() {
    QHBoxLayout* lyMain = new QHBoxLayout;
    this->setLayout(lyMain);

    QWidget* left = new QWidget;
    QVBoxLayout* lyLeft = new QVBoxLayout;
    left->setLayout(lyLeft);

    QWidget* form = new QWidget;
    QFormLayout* lyForm = new QFormLayout;
    form->setLayout(lyForm);
    editRegistrationNumber = new QLineEdit;
    editProducer = new QLineEdit;
    editModel = new QLineEdit;
    editType = new QLineEdit;

    lyForm->addRow(lblRegistrationNumber, editRegistrationNumber);
    lyForm->addRow(lblProducer, editProducer);
    lyForm->addRow(lblModel, editModel);
    lyForm->addRow(lblType, editType);
    btnAddCar = new QPushButton("Add car");
    lyForm->addWidget(btnAddCar);
    btnRemoveCar = new QPushButton("Delete car");
    lyForm->addWidget(btnRemoveCar);
    btnUpdateCar = new QPushButton("Update car");
    lyForm->addWidget(btnUpdateCar);
    btnUndo = new QPushButton("Undo");
    lyForm->addWidget(btnUndo);

    btn_lst_mst = new QPushButton("Generate List");
    lyForm->addWidget(btn_lst_mst);

    lyLeft->addWidget(form);

    QVBoxLayout* lyRadioBox = new QVBoxLayout;
    this->groupBox->setLayout(lyRadioBox);
    lyRadioBox->addWidget(radioSrtProducerModel);
    lyRadioBox->addWidget(radioSrtRegistrationNumber);
    lyRadioBox->addWidget(radioSrtType);

    btnSortCars = new QPushButton("Sort cars");
    lyRadioBox->addWidget(btnSortCars);

    lyLeft->addWidget(groupBox);

    QWidget* formFilter = new QWidget;
    QFormLayout* lyFormFilter = new QFormLayout;
    formFilter->setLayout(lyFormFilter);
    editFilterProducer = new QLineEdit();
    lyFormFilter->addRow(lblFilterProducer, editFilterProducer);
    btnFilterCars = new QPushButton("Filter after producer");
    lyFormFilter->addWidget(btnFilterCars);
    editFilterType = new QLineEdit();
    lyFormFilter->addRow(lblFilterType, editFilterType);
    btnFilterCars = new QPushButton("Filter after type");
    lyFormFilter->addWidget(btnFilterCars);

    lyLeft->addWidget(formFilter);

    btnReloadData = new QPushButton("Reload data");
    lyLeft->addWidget(btnReloadData);

    QWidget* right = new QWidget;
    QVBoxLayout* lyRight = new QVBoxLayout;
    right->setLayout(lyRight);

    int noLines = 10;
    int noColumns = 4;
    this->tableCars = new QTableWidget{noLines, noColumns};

    QStringList tblHeaderList;
    tblHeaderList << "Registration number" << "Producer" << "Model" << "Type";
    this->tableCars->setHorizontalHeaderLabels(tblHeaderList);

    this->tableCars->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);

    lyRight->addWidget(tableCars);

    lyMain->addWidget(left);
    lyMain->addWidget(right);
}

void CarsGUI::reloadCarList(vector<Car> cars) {
    this->tableCars->clearContents();
    this->tableCars->setRowCount(cars.size());

    int lineNumber = 0;
    for(auto& car : cars){
        this->tableCars->setItem(lineNumber, 0, new QTableWidgetItem(QString::fromStdString(car.getRegistrationNumber())));
        this->tableCars->setItem(lineNumber, 1, new QTableWidgetItem(QString::fromStdString(car.getProducer())));
        this->tableCars->setItem(lineNumber, 2, new QTableWidgetItem(QString::fromStdString(car.getModel())));
        this->tableCars->setItem(lineNumber, 3, new QTableWidgetItem(QString::fromStdString(car.getType())));
        lineNumber++;
    }
}

void CarsGUI::connectSignalsSlots() {
    QObject::connect(btnAddCar, &QPushButton::clicked, this, &CarsGUI::guiAddCar);
    QObject::connect(btnRemoveCar, &QPushButton::clicked, this, &CarsGUI::guiRemoveCar);
    QObject::connect(btnUpdateCar, &QPushButton::clicked, this, &CarsGUI::guiUptCar);
    QObject::connect(btnUndo, &QPushButton::clicked, this, &CarsGUI::guiUndo);
    QObject::connect(btnSortCars, &QPushButton::clicked, [&]() {
        if( this->radioSrtProducerModel->isChecked())
            this->reloadCarList(srv.sortByProducerModel());
        else if(this->radioSrtRegistrationNumber->isChecked())
            this->reloadCarList(srv.sortByRegistrationNumber());
        else if(this->radioSrtType->isChecked())
            this->reloadCarList(srv.sortByType());
    });

    QObject::connect(btnFilterCars, &QPushButton::clicked, [&](){
        string filterC = this->editFilterProducer->text().toStdString();
        this->reloadCarList(srv.filterProducer(filterC));
        string filterT = this->editFilterType->text().toStdString();
        this->reloadCarList(srv.filterType(filterT));
    });

    QObject::connect(btnReloadData, &QPushButton::clicked, [&](){
        this->reloadCarList(srv.getAllCars());
    });

    QObject::connect(btn_lst_mst, &QPushButton::clicked, [=]() {
        auto wind = new ListaGUI{ rep,srv };
        rcp.push_back(wind);
        wind->show();
    });
}

void CarsGUI::guiAddCar() {
    try{
        string registrationNumber = editRegistrationNumber->text().toStdString();
        string producer = editProducer->text().toStdString();
        string model = editModel->text().toStdString();
        string type = editType->text().toStdString();

        editRegistrationNumber->clear();
        editProducer->clear();
        editModel->clear();
        editType->clear();

        this->srv.addCar(registrationNumber, producer, model, type);
        this->reloadCarList(this->srv.getAllCars());

        QMessageBox::information(this, "Info", QString::fromStdString("Car successfully added!"));
    }catch (CarRepoException& re) {
        QMessageBox::warning(this, "Warning", QString::fromStdString(re.getErrorMessage()));
    }catch(validateException& ve){
        QMessageBox::warning(this, "Warning", QString::fromStdString(ve.getErrorMessages()));
    }


}

void CarsGUI::guiRemoveCar() {
    string registrationNumber = editRegistrationNumber->text().toStdString();
    string producer = editProducer->text().toStdString();
    string model = editModel->text().toStdString();
    string type = editModel->text().toStdString();

    auto c = Car(registrationNumber, producer, model, type);
    int index = 0;
    for(auto& car : srv.getAllCars()){
        if(car == c){
            break;
        }
        ++index;
    }
    if(index == srv.getAllCars().size()){
        QMessageBox::warning(this, "Warning", QString::fromStdString("Introduced element does not exist!"));
    }
    else{
        srv.deleteCar(index);
        reloadCarList(srv.getAllCars());
    }
}

void CarsGUI::guiUptCar() {
    auto registrationNumber = editRegistrationNumber->text().toStdString();
    auto producer = editProducer->text().toStdString();
    auto model = editModel->text().toStdString();
    auto type = editType->text().toStdString();
    int index = 0;
    for(auto& car : srv.getAllCars()){
        if(car.getRegistrationNumber() == registrationNumber){
            break;
        }
        ++index;
    }
    if(index == srv.getAllCars().size()){
        QMessageBox::warning(this, "Warning", QString::fromStdString("You haven't selected any element"));
        return;
    }

    try{
        srv.modifyCar(index,registrationNumber, producer, model, type);
        reloadCarList(srv.getAllCars());
    }
    catch (validateException& ve){
        QMessageBox::warning(this, "Warning", QString::fromStdString(ve.getErrorMessages()));
    }
}

void CarsGUI::guiUndo() {
    srv.undo();
    reloadCarList(srv.getAllCars());
}

void ListaGUI::initGUI() {
    setLayout(recipe_main_layout);

    recipe_list = new QListWidget;
    recipe_main_layout->addWidget(recipe_list);

    QWidget* recipe_but_zone = new QWidget;
    QVBoxLayout* recipe_but_layout = new QVBoxLayout;
    recipe_but_zone->setLayout(recipe_but_layout);

    QWidget* recipe_form = new QWidget;
    QFormLayout* recipe_form_layout = new QFormLayout;
    recipe_form->setLayout(recipe_form_layout);

    QLabel* lbl_recipe = new QLabel("Input");
    lne_recipe = new QLineEdit;

    recipe_form_layout->addRow(lbl_recipe, lne_recipe);

    recipe_but_layout->addWidget(recipe_form);

    add_to_rec = new QPushButton("Add");
    empty_rec = new QPushButton("Empty list");
    random_add = new QPushButton("Add random");
    export_recipe = new QPushButton("Export");
    help_button = new QPushButton("Help");

    recipe_but_layout->addWidget(add_to_rec);
    recipe_but_layout->addWidget(empty_rec);
    recipe_but_layout->addWidget(random_add);
    recipe_but_layout->addWidget(export_recipe);
    recipe_but_layout->addWidget(help_button);

    recipe_main_layout->addWidget(recipe_but_zone);

    reloadDis(rep.getallspalatorieMasini());

}

void ListaGUI::reloadDis(vector<Car> car) {
    recipe_list->clear();
    for (const auto& med : car) {
        QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(med.getRegistrationNumber()));
        recipe_list->addItem(item);
    }
}

void ListaGUI::connectSignals() {
    QObject::connect(add_to_rec, &QPushButton::clicked, [=]() {
        auto inp = lne_recipe->text().toStdString();
        int nr = 0;
        bool valid = true;
        for (auto& ch : inp) {
            if ('0' <= ch && ch <= '9') {
                nr = nr * 10 + (ch - '0');
            }
            else {
                valid = false;
            }
        }
        if (nr > srv.getAllCars().size()) {
            valid = false;
        }
        if (valid) {
            rep.addCartoLista(srv.getAllCars()[nr]);
            reloadDis(rep.getallspalatorieMasini());
        }
        else {
            QMessageBox::warning(this, "Warning", QString::fromStdString("Invalid index"));
        }
    });

    QObject::connect(empty_rec, &QPushButton::clicked, [=]() {
        rep.emptyList();
        reloadDis(rep.getallspalatorieMasini());
        //reset_form();
    });

    QObject::connect(random_add, &QPushButton::clicked, [=]() {
        auto inp = lne_recipe->text().toStdString();
        int nr = 0;
        bool valid = true;
        for (auto& ch : inp) {
            if ('0' <= ch && ch <= '9') {
                nr = nr * 10 + (ch - '0');
            }
            else {
                valid = false;
            }
        }
        if (valid) {
            rep.addRandomMasini(srv.getAllCars(), nr);
            reloadDis(rep.getallspalatorieMasini());
        }
        else {
            QMessageBox::warning(this, "Warning", QString::fromStdString("Invalid number"));
        }
    });

    QObject::connect(export_recipe, &QPushButton::clicked, [=]() {
        auto filename = lne_recipe->text().toStdString();
        rep.save_to_file(filename);
    });

    QObject::connect(help_button, &QPushButton::clicked, [=]() {
        string msg = "Campul input se foloseste pentru a comunica optiunile\n";
        msg += "Pentru Add in input se va specifica indicele de adaugat\n";
        msg += "Pentru Add random in input se va specifica numarul de entitati de adaugat\n";
        msg += "Pentru Export in input se va specifica numele fisierului in care se face exportul\n";
        QMessageBox::information(this, "Help", QString::fromStdString(msg));
    });
}
