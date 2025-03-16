package com.example;
import com.fasterxml.jackson.annotation.JsonProperty;


public class Race extends Entity<Long> {

    @JsonProperty("capacity")
    private int capacity;

    public Race(){}
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
