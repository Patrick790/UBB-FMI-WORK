package com.example;


public interface IRegistrationRepository extends Repository<Long, Registration> {
    public int getNumberOfParticipantsInRace(Race race);

    public int getCapacityForParticipant(Participant participant);
}
