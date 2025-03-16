package com.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Properties;

public class RegistrationDBRepository implements IRegistrationRepository{
    private final JdbcUtils dbUtils;

    private static final Logger logger= LogManager.getLogger();

    public RegistrationDBRepository(Properties props){
        logger.info("Initializing UserDBRepository with properties: {}",props);
        dbUtils=new JdbcUtils(props);
    }

    @Override
    public Optional<Registration> findOne(Long registrationId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from registration where id = ?")){
            preStmt.setLong(1, registrationId);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    Long participant_id = result.getLong("participant_id");
                    Long race_id = result.getLong("race_id");
                    Participant participant = new Participant(null, null);
                    participant.setId(participant_id);

                    Race race = new Race(0);
                    race.setId(race_id);

                    Registration registration = new Registration(participant, race);
                    registration.setId(id);
                    logger.traceExit(registration);
                    return Optional.of(registration);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return Optional.empty();
    }

    @Override
    public Iterable<Registration> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Registration> registrations = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from registration")){
            try(ResultSet result = preStmt.executeQuery()) {
                while(result.next()) {
                    Long id = result.getLong("id");
                    Long participant_id = result.getLong("participant_id");
                    Long race_id = result.getLong("race_id");
                    Participant participant = new Participant(null, null);
                    participant.setId(participant_id);

                    Race race = new Race(0);
                    race.setId(race_id);

                    Registration registration = new Registration(participant, race);
                    registration.setId(id);
                    registrations.add(registration);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(registrations);
        return registrations;

    }

    @Override
    public void save(Registration entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into registration (participant_id, race_id) values (?,?)")){
            preStmt.setLong(1, entity.getParticipant().getId());
            preStmt.setLong(2, entity.getRace().getId());
            int result = preStmt.executeUpdate();
            logger.trace("Saved {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
    }

    @Override
    public Optional<Registration> delete(Long id) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("delete from registration where id=?")){
            preStmt.setLong(1, id);
            int result = preStmt.executeUpdate();
            logger.trace("Deleted {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return Optional.empty();
    }

    @Override
    public Optional<Registration> update(Registration entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("update registration set participant_id=?, race_id=? where id=?")){
            preStmt.setLong(1, entity.getParticipant().getId());
            preStmt.setLong(2, entity.getRace().getId());
            preStmt.setLong(3, entity.getId());
            int result = preStmt.executeUpdate();
            logger.trace("Updated {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return Optional.of(entity);
    }


    public int getNumberOfParticipantsInRace(Race race) {
        String query = "SELECT COUNT(*) FROM registration WHERE race_id=?";
        int count = 0;
        Connection con = dbUtils.getConnection();
        try (PreparedStatement preStmt = con.prepareStatement(query)) {
            preStmt.setLong(1, race.getId());
            try (ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    count = result.getInt(1);
                }
            }
        } catch (SQLException e) {
            logger.error("Error occurred while counting participants in race", e);
        }

        return count;
    }

    public int getCapacityForParticipant(Participant participant) {
        logger.traceEntry();
        int capacity = 0;
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("SELECT capacity FROM race INNER JOIN registration ON race.id = registration.race_id WHERE registration.participant_id = ?")){
            preStmt.setLong(1, participant.getId());
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    capacity = result.getInt("capacity");
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return capacity;
    }
}
