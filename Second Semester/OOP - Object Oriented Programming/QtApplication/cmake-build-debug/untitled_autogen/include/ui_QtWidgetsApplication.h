/********************************************************************************
** Form generated from reading UI file 'qtwidgetsapplication.ui'
**
** Created by: Qt User Interface Compiler version 6.5.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QTWIDGETSAPPLICATION_H
#define UI_QTWIDGETSAPPLICATION_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QtWidgetsApplication
{
public:

    void setupUi(QWidget *QtWidgetsApplication)
    {
        if (QtWidgetsApplication->objectName().isEmpty())
            QtWidgetsApplication->setObjectName("QtWidgetsApplication");
        QtWidgetsApplication->resize(400, 300);

        retranslateUi(QtWidgetsApplication);

        QMetaObject::connectSlotsByName(QtWidgetsApplication);
    } // setupUi

    void retranslateUi(QWidget *QtWidgetsApplication)
    {
        QtWidgetsApplication->setWindowTitle(QCoreApplication::translate("QtWidgetsApplication", "QtWidgetsApplication", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QtWidgetsApplication: public Ui_QtWidgetsApplication {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QTWIDGETSAPPLICATION_H
