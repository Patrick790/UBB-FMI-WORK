//
// Created by Ardelean on 5/24/2023.
//

// You may need to build the project (run Qt uic code generator) to get "ui_QtWidgetsApplication.h" resolved

#include "qtwidgetsapplication.h"
#include "ui_QtWidgetsApplication.h"


QtWidgetsApplication::QtWidgetsApplication(QWidget *parent) :
        QWidget(parent), ui(new Ui::QtWidgetsApplication) {
    ui->setupUi(this);
}

QtWidgetsApplication::~QtWidgetsApplication() {
    delete ui;
}
