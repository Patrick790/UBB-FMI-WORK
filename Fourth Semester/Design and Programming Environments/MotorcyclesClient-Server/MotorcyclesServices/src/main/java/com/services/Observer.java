package com.services;

import java.sql.SQLException;

public interface Observer {
    public void update() throws SQLException, MotorcyclesException;
}
