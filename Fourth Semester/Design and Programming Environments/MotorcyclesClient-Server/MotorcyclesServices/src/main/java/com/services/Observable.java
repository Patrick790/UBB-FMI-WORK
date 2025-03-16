package com.services;

import java.sql.SQLException;

public interface Observable {
    public void registerObserver(Observer o);
    public void removeObserver(Observer o);
    public void notifyAllObservers() throws MotorcyclesException, SQLException;
}
