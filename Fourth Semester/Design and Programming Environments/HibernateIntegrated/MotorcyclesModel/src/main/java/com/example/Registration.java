package com.example;


public class Registration extends Entity<Long>{

    private Participant participant;

    private Race race;

    public Registration(Participant participant, Race race) {
        this.participant = participant;
        this.race = race;
    }

    public Participant getParticipant() {
        return participant;
    }

    public void setParticipant(Participant participant) {
        this.participant = participant;
    }

    public Race getRace() {
        return race;
    }

    public void setRace(Race race) {
        this.race = race;
    }

    @Override
    public String toString() {
        return "Registration{" +
                "participant=" + participant + '\'' +
                ", race='" + race + '\'' +
                '}';
    }
}
