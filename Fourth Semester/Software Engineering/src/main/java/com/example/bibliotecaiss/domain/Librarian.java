package com.example.bibliotecaiss.domain;

public class Librarian extends User{
    private String name;

    public Librarian(String username, String password, String name) {
        super(username, password);
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Librarian{" +
                "id=" + getId() +
                ", username='" + getUsername() + '\'' +
                ", password='" + getPassword() + '\'' +
                ", name='" + name + '\'' +
                '}';
    }

}
