package com.services;

import com.example.Participant;
import com.example.Race;
import com.example.Registration;
import com.example.User;

import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

public interface IMotorcyclesServices extends Observable {
    Iterable<Participant> getAllParticipants() throws MotorcyclesException;
    void addParticipant(Participant participant) throws SQLException, MotorcyclesException;
    List<Participant> findByTeam(String team) throws MotorcyclesException;
    Optional<Participant> findParticipantByNameAndTeam(String name, String team) throws MotorcyclesException;

    Iterable<Race> getAllRaces() throws MotorcyclesException;
    void addRace(Race race) throws SQLException, MotorcyclesException;

    void addRegistration(Registration registration) throws SQLException, MotorcyclesException;
    int countRegistrationsForRace(Race race) throws MotorcyclesException, SQLException;
    int getCapacityForParticipant(Participant participant) throws MotorcyclesException;

    boolean login2(String username, String password);
    boolean login(String username, String password, Observer observer) throws MotorcyclesException;
    User findAfterUsername(String username) throws MotorcyclesException;
    void addUser(User user) throws MotorcyclesException;
    String hashPassword(String password) throws MotorcyclesException;

    long getNextParticipantId() throws MotorcyclesException;

    boolean isParticipantRegisteredForRace(Participant participant, Race race) throws MotorcyclesException;
}
