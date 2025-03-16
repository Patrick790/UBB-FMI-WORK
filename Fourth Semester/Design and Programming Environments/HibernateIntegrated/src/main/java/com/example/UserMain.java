package com.example;

public class UserMain {
    public static void main(String[] args) {
        System.out.println("Starting user main");
        UserRepository repo = new UserHibernateRepository();

        User user = new User("deng", "Patrick", "deng1");

        System.out.println("Adding user");
        repo.save(user);
    }


}
