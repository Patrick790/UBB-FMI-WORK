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

public class RaceDBRepository implements IRaceRepository{
    private final JdbcUtils dbUtils;

    private static final Logger logger= LogManager.getLogger();

    public RaceDBRepository(Properties props){
        logger.info("Initializing UserDBRepository with properties: {}",props);
        dbUtils=new JdbcUtils(props);
    }

    @Override
    public Optional<Race> findOne(Long raceId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from race where id = ?")){
            preStmt.setLong(1, raceId);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    int capacity = result.getInt("capacity");
                    Race race = new Race(capacity);
                    race.setId(id);
                    logger.traceExit(race);
                    return Optional.of(race);
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
    public Iterable<Race> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Race> races = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from race")){
            try(ResultSet result = preStmt.executeQuery()) {
                while(result.next()) {
                    Long id = result.getLong("id");
                    int capacity = result.getInt("capacity");
                    Race race = new Race(capacity);
                    race.setId(id);
                    races.add(race);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(races);
        return races;
    }

    @Override
    public void save(Race entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into race (capacity) values (?)")){
            preStmt.setInt(1, entity.getCapacity());
            int result = preStmt.executeUpdate();
            logger.trace("Saved {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
    }

    @Override
    public Optional<Race> delete(Long raceId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("delete from race where id = ?")){
            preStmt.setLong(1, raceId);
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
    public Optional<Race> update(Race entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("update race set capacity = ? where id = ?")){
            preStmt.setInt(1, entity.getCapacity());
            preStmt.setLong(2, entity.getId());
            int result = preStmt.executeUpdate();
            logger.trace("Updated {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return Optional.of(entity);
    }

    public List<Race> findByCapacity(int capacity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Race> races = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from race where capacity = ?")){
            preStmt.setInt(1, capacity);
            try(ResultSet result = preStmt.executeQuery()) {
                while(result.next()) {
                    Long id = result.getLong("id");
                    Race race = new Race(capacity);
                    race.setId(id);
                    races.add(race);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(races);
        return races;
    }
}
