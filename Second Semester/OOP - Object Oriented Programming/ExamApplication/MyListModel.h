#pragma once

#include <QAbstractTableModel>
#include <vector>
#include "Melodie.h"

class MyTableModel: public QAbstractTableModel{
private:
    vector<Melodie> melodii;

public:
    MyTableModel(vector<Melodie> melodii): melodii{ melodii }{}

    int rowCount(const QModelIndex& parent = QModelIndex()) const override{
        return melodii.size();
    }

    int columnCount(const QModelIndex& parent = QModelIndex()) const override{
        return 4;
    }

    QVariant data(const QModelIndex& ind, int role = Qt::DisplayRole) const override{
        if(role == Qt::DisplayRole){
            if(ind.column() == 0)
                return QString::number(melodii[ind.row()].getId());
            else if(ind.column() == 1)
                return QString::fromStdString(melodii[ind.row()].getTitlu());
            else if(ind.column() == 2)
                return QString::fromStdString(melodii[ind.row()].getArtist());
            else if(ind.column() == 3)
                return QString::fromStdString(melodii[ind.row()].getGen());
        }
        return QVariant{};
    }

    void setMelodii(vector<Melodie>& nw){
        melodii = nw;
        auto up = createIndex(0, 0);
        auto down = createIndex(rowCount(), columnCount());
        emit dataChanged(up, down);
        emit layoutChanged();
    }

    QVariant headerData(int section, Qt::Orientation orientation, int role) const
    {
        if (role == Qt::DisplayRole && orientation == Qt::Horizontal)
        {
            if (section == 0)
                return "ID";
            if (section == 1)
                return "TITLU";
            if (section == 2)
                return "ARTIST";
            if (section == 3)
                return "GEN";
        }
        return QVariant();
    }
};
