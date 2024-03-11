#include "UI.h"


void GUI::initGUI() {
    setLayout(ly_main);

    tb_view = new QTableView;
    ly_main->addWidget(tb_view);

    QWidget* wdg_right = new QWidget;
    QVBoxLayout* ly_right = new QVBoxLayout;
    wdg_right->setLayout(ly_right);

    QWidget* form_wdg = new QWidget;
    QFormLayout* form_lay = new QFormLayout;
    form_wdg->setLayout(form_lay);

    QLabel* lId = new QLabel("Id");
    QLabel* lT = new QLabel("Titlu");
    QLabel* lA = new QLabel("Artist");
    QLabel* lR = new QLabel("Gen");

    txt_id = new QLineEdit;
    txt_titlu = new QLineEdit;
    txt_artist = new QLineEdit;
    txt_gen = new QLineEdit;

    form_lay->addRow(lId, txt_id);
    form_lay->addRow(lT, txt_titlu);
    form_lay->addRow(lA, txt_artist);
    form_lay->addRow(lR, txt_gen);

    ly_right->addWidget(form_wdg);
    btna = new QPushButton("Add");
    ly_right->addWidget(btna);
    btnr = new QPushButton("Sterge");
    ly_right->addWidget(btnr);

    ly_main->addWidget(wdg_right);
}

void GUI::connectSignals() {

    QObject::connect(tb_view->selectionModel(), &QItemSelectionModel::selectionChanged, [=](){
        if(tb_view->selectionModel()->selectedIndexes().empty()){
            txt_id->setText("");
            txt_titlu->setText("");
            txt_artist->setText("");
            txt_gen->setText("");
            return;
        }
        auto sel = tb_view->selectionModel()->selectedIndexes().at(0);
        int row = sel.row();
        auto elem = displayed[row];
        txt_id->setText(QString::number(elem.getId()));
        txt_titlu->setText(QString::fromStdString(elem.getTitlu()));
        txt_artist->setText(QString::fromStdString(elem.getArtist()));
        txt_gen->setText(QString::fromStdString(elem.getGen()));
    });

    QObject::connect(btna, &QPushButton::clicked, [=](){
        try{
            int id = to_nr(txt_id->text().toStdString());
            string titlu = txt_titlu->text().toStdString();
            string artist = txt_artist->text().toStdString();
            string gen = txt_gen->text().toStdString();

            Melodie::validate(id, titlu, artist, gen);
            srv.validateIdd(id);
            srv.add(id, titlu, artist, gen);
            int row = tb_model->rowCount(QModelIndex());
            tb_model->insertRows(row, 1, QModelIndex());
            reloadList(srv.getAll());
        }catch(ValidationException& ve){
            QMessageBox::critical(nullptr, "Warning", QString::fromStdString(ve.getMessage()));
        }catch(DuplicatedIdException& de){
            QMessageBox::critical(nullptr, "Warning", QString::fromStdString(de.getMessage()));
        }
    });

    QObject::connect(btnr, &QPushButton::clicked, [=](){
        int id = to_nr(txt_id->text().toStdString());
        string titlu = txt_titlu->text().toStdString();
        string artist = txt_artist->text().toStdString();
        string gen = (txt_gen->text().toStdString());
        Melodie m{id, titlu, artist, gen};
        int poz = 0;
        for(auto& mel: displayed){
            if(mel.getId() == id){
                break;
            }
            poz++;
        }

        srv.remove(poz);
        reloadList(srv.getAll());
    });

}

void GUI::reloadList(vector<Melodie>& all) {
    sort(all.begin(), all.end(), [](Melodie& m1, Melodie& m2){
        return m1.getArtist() > m2.getArtist();
    });

    displayed = all;
    tb_model->setMelodii(all);
}


void GUI::alert() {
    reloadList(srv.getAll());
}