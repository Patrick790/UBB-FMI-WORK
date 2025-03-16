package com.example;

import com.example.Participant;

import java.util.List;
import java.util.Optional;

public interface IParticipantRepository extends Repository<Long, Participant> {

    public List<Participant> findByTeam(String team);

    public Optional<Participant> findParticipantByNameAndTeam(String name, String team);
}
