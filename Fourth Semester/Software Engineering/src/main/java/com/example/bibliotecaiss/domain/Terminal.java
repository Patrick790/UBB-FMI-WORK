package com.example.bibliotecaiss.domain;

public class Terminal extends Entity<Long>{

    private String location;

    public Terminal(String location) {
        this.location = location;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    @Override
    public String toString() {
        return "Terminal{" +
                "id=" + getId() +
                ", location='" + location + '\'' +
                '}';
    }
}
