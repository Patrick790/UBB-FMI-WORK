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

public class ParticipantDBRepository implements IParticipantRepository{

    private final JdbcUtils dbUtils;

    private static final Logger logger= LogManager.getLogger();

    public ParticipantDBRepository(Properties props){
        logger.info("Initializing UserDBRepository with properties: {}",props);
        dbUtils=new JdbcUtils(props);
    }

    @Override
    public Optional<Participant> findOne(Long participantId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from participant where id = ?")){
            preStmt.setLong(1, participantId);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    String name = result.getString("name");
                    String team = result.getString("team");
                    Participant participant = new Participant(name, team);
                    participant.setId(id);
                    logger.traceExit(participant);
                    return Optional.of(participant);
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
    public Iterable<Participant> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Participant> participants = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from participant")){
            try(ResultSet result = preStmt.executeQuery()) {
                while(result.next()) {
                    Long id = result.getLong("id");
                    String name = result.getString("name");
                    String team = result.getString("team");
                    Participant participant = new Participant(name, team);
                    participant.setId(id);
                    participants.add(participant);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(participants);
        return participants;
    }

    @Override
    public void save(Participant entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into participant (name, team) values (?,?)")){
            preStmt.setString(1, entity.getName());
            preStmt.setString(2, entity.getTeam());
            int result = preStmt.executeUpdate();
            logger.trace("Saved {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
    }

    @Override
    public Optional<Participant> delete(Long participantId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("delete from participant where id = ?")){
            preStmt.setLong(1, participantId);
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
    public Optional<Participant> update(Participant entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("update participant set name = ?, team = ? where id = ?")){
            preStmt.setString(1, entity.getName());
            preStmt.setString(2, entity.getTeam());
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

    public List<Participant> findByTeam(String team) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Participant> participants = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from participant where team = ?")){
            preStmt.setString(1, team);
            try(ResultSet result = preStmt.executeQuery()) {
                while(result.next()) {
                    Long id = result.getLong("id");
                    String participantName = result.getString("name");
                    String participantTeam = result.getString("team");
                    Participant participant = new Participant(participantName, participantTeam);
                    participant.setId(id);
                    participants.add(participant);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(participants);
        return participants;
    }


    public Optional<Participant> findParticipantByNameAndTeam(String name, String team) {
        Connection con = dbUtils.getConnection();
        try (PreparedStatement preStmt = con.prepareStatement("select * from participant where name=? and team=?")) {
            preStmt.setString(1, name);
            preStmt.setString(2, team);
            try (ResultSet result = preStmt.executeQuery()) {
                if (!result.next()) {
                    return Optional.empty();
                }
                Long id = result.getLong("id");
                Participant participant = new Participant(name, team);
                participant.setId(id);
                return Optional.of(participant);
            }
        } catch (SQLException e) {
            System.out.println("Error DB " + e);
        }
        return Optional.empty();
    }
}
