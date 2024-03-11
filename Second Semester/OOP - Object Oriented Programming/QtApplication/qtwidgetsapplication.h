//
// Created by Ardelean on 5/24/2023.
//

#ifndef UNTITLED_QTWIDGETSAPPLICATION_H
#define UNTITLED_QTWIDGETSAPPLICATION_H

#include <QWidget>


QT_BEGIN_NAMESPACE
namespace Ui { class QtWidgetsApplication; }
QT_END_NAMESPACE

class QtWidgetsApplication : public QWidget {
Q_OBJECT

public:
    explicit QtWidgetsApplication(QWidget *parent = nullptr);

    ~QtWidgetsApplication() override;

private:
    Ui::QtWidgetsApplication *ui;
};


#endif //UNTITLED_QTWIDGETSAPPLICATION_H
