package com.example;

public interface IUserRepository extends Repository<Long, User>{

    User findByUsername(String username);
    User findBy(String username, String password);




}
