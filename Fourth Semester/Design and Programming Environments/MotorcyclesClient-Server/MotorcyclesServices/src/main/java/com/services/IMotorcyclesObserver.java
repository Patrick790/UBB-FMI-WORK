package com.services;

import com.example.Participant;
import com.example.Race;

public interface IMotorcyclesObserver {
    void participantRegistered(Participant participant) throws MotorcyclesException;

    void countRegistrationsForRace(Race race) throws MotorcyclesException;

    void addRace(Race race) throws MotorcyclesException;





}
