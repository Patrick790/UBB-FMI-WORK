package com.services;

public class MotorcyclesException extends Exception{
    public MotorcyclesException() {
    }

    public MotorcyclesException(String message) {
        super(message);
    }

    public MotorcyclesException(String message, Throwable cause) {
        super(message, cause);
    }
}
