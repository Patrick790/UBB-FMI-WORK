package com.server;


import com.example.*;
import com.hibernate.user.User;
import com.hibernate.user.UserRepository;
import com.services.IMotorcyclesObserver;
import com.services.IMotorcyclesServices;
import com.services.MotorcyclesException;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.SQLException;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class MotorcyclesServicesImpl implements IMotorcyclesServices{

    private final UserRepository userRepository;
    private final IParticipantRepository participantRepository;
    private final IRaceRepository raceRepository;
    private final IRegistrationRepository registrationRepository;

    private Map<String, IMotorcyclesObserver> loggedClients;

    public MotorcyclesServicesImpl(UserRepository userRepository, IParticipantRepository participantRepository, IRaceRepository raceRepository, IRegistrationRepository registrationRepository) {
        this.userRepository = userRepository;
        this.participantRepository = participantRepository;
        this.raceRepository = raceRepository;
        this.registrationRepository = registrationRepository;
        loggedClients = new ConcurrentHashMap<>();
    }
    @Override
    public Iterable<Participant> getAllParticipants() {
        return participantRepository.findAll();
    }

    @Override
    public void addParticipant(Participant participant) throws SQLException, MotorcyclesException {
        if (participantRepository.findOne(participant.getId()).isPresent()) {
            throw new RuntimeException("Participant already exists");
        }
        participantRepository.save(participant);


    }

    @Override
    public List<Participant> findByTeam(String team) {
        return participantRepository.findByTeam(team);
    }

    @Override
    public Optional<Participant> findParticipantByNameAndTeam(String name, String team) {
        return participantRepository.findParticipantByNameAndTeam(name, team);
    }

    @Override
    public Iterable<Race> getAllRaces() {
        return raceRepository.findAll();
    }

    @Override
    public void addRace(Race race) throws MotorcyclesException {
        if (raceRepository.findOne(race.getId()).isPresent()) {
            throw new RuntimeException("Race already exists");
        }
        raceRepository.save(race);

        // Notify all logged in clients about the new race
        for (IMotorcyclesObserver client : loggedClients.values()) {
            client.raceAdded(race);
        }
    }

    @Override
    public void addRegistration(Registration registration) throws SQLException, MotorcyclesException {
        if (registrationRepository.findOne(registration.getId()).isPresent()) {
            throw new RuntimeException("Registration already exists");
        }
        registrationRepository.save(registration);

    }

    @Override
    public int countRegistrationsForRace(Race race) throws SQLException, MotorcyclesException {
        List<Registration> registrations = new ArrayList<>();
        registrationRepository.findAll().forEach(registrations::add);
        return (int) registrations.stream()
                .filter(registration -> registration.getRace().equals(race))
                .count();
    }

    public synchronized int getCapacityForParticipant(Participant participant) {
        return registrationRepository.getCapacityForParticipant(participant);
    }

    @Override
    public boolean login2(String username, String password) {
        Long idUser = Long.valueOf(findAfterUsername(username).getId());
        Optional<User> user = userRepository.findOne(Math.toIntExact(idUser));
        if(user.isPresent()){
            return Objects.equals(user.get().getPassword(), password);
        } else {
            throw new RuntimeException("User does not exist");
        }
    }
    @Override
    public synchronized boolean login(String username, String password, IMotorcyclesObserver client) throws MotorcyclesException {
        Long idUser = Long.valueOf(findAfterUsername(username).getId());
        Optional<User> user = userRepository.findOne(Math.toIntExact(idUser));
        if(user.isPresent()){

            if (password.equals(user.get().getPassword())) {
                // User successfully logged in, add to loggedClients
                loggedClients.put(username, client); // replace null with an instance of IMotorcyclesObserver if available
                return true;
            } else {
                throw new RuntimeException("Incorrect password");
            }
        } else {
            throw new RuntimeException("User does not exist");
        }
    }

    @Override
    public User findAfterUsername(String username) {
        for(User u : userRepository.findAll()){
            if (Objects.equals(u.getUsername(), username)){
                return u;
            }
        }
        return null;
    }

    @Override
    public synchronized void addUser(User user) {
        if (userRepository.findOne(user.getId()).isPresent()) {
            throw new RuntimeException("Participant already exists");
        }
        userRepository.save(user);

    }
    @Override
    public String hashPassword(String password){
        try{
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(password.getBytes());
            byte[] digest = md.digest();
            return Base64.getEncoder().encodeToString(digest);
        } catch(NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }


    @Override
    public long getNextParticipantId() {
        Iterable<Participant> participants = participantRepository.findAll();
        long maxId = 0;
        for (Participant participant : participants) {
            if (participant.getId() > maxId) {
                maxId = participant.getId();
            }
        }
        return maxId + 1;
    }

    @Override
    public boolean isParticipantRegisteredForRace(Participant participant, Race race) {
        Iterable<Registration> registrations = registrationRepository.findAll();
        for (Registration registration : registrations) {
            if (registration.getParticipant().getId().equals(participant.getId()) && registration.getRace().getId().equals(race.getId())) {
                return true;
            }
        }
        return false;
    }
}
