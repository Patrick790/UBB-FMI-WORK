#pragma once

#include <QWidget>
#include <QTableWidget>
#include <QLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QLabel>
#include <QFormLayout>
#include <QMessageBox>

#include "Service.h"
#include "MyListModel.h"

class GUI:public QWidget, public Observer{
private:
    Service& srv;
    vector<Melodie> displayed;
    QHBoxLayout* ly_main = new QHBoxLayout;
    QTableWidget* tb_wdg;

    QTableView* tb_view;
    MyTableModel* tb_model;

    QLineEdit* txt_id;
    QLineEdit* txt_titlu;
    QLineEdit* txt_artist;
    QLineEdit* txt_gen;
    QPushButton* btna;
    QPushButton* btnr;

    void initGUI();
    void connectSignals();
    void reloadList(vector<Melodie>& all);

public:
    void alert() override;
    GUI(Service& srv):srv{srv}{
        srv.addObserver(this);
        initGUI();
        tb_model = new MyTableModel{srv.getAll()};
        displayed = srv.getAll();
        tb_view->setModel(tb_model);
        connectSignals();
        reloadList(srv.getAll());
    }
    ~GUI(){
        srv.removeObs(this);
    }
};

