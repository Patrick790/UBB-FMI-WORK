package com.example.bibliotecaiss.domain;

public class Subscriber extends User{
    private String cnp;
    private String name;
    private String address;
    private String phone;

    public Subscriber(String username, String password, String cnp, String name, String address, String phone) {
        super(username, password);
        this.cnp = cnp;
        this.name = name;
        this.address = address;
        this.phone = phone;

    }


    public String getCnp() {
        return cnp;
    }

    public void setCnp(String cnp) {
        this.cnp = cnp;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }



    @Override
    public String toString() {
        return "Subscriber{" +
                "id=" + getId() +
                ", username='" + getUsername() + '\'' +
                ", cnp='" + cnp + '\'' +
                ", name='" + name + '\'' +
                ", address='" + address + '\'' +
                ", phone='" + phone + '\'' +
                '}';
    }
}
