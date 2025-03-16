package com.example;

public class Race extends Entity<Long> {

    private int capacity;

    public Race(int capacity) {
        this.capacity = capacity;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

}
