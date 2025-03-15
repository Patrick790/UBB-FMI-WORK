package com.example.bibliotecaiss.repository;

import com.example.bibliotecaiss.domain.Subscriber;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Properties;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class SubscriberDBRepository implements ISubscriberRepository{
    private final JdbcUtils dbUtils;

    private static final Logger logger = LogManager.getLogger();

    public SubscriberDBRepository(Properties props){
        logger.info("Initializing SubscriberDBRepository with properties: {}",props);
        dbUtils = new JdbcUtils(props);
    }
    @Override
    public Optional<Subscriber> findOne(Long subscriberId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Subscriber where id = ?")){
            preStmt.setLong(1, subscriberId);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    String username = result.getString("username");
                    String cnp = result.getString("cnp");
                    String name = result.getString("name");
                    String address = result.getString("address");
                    String phone = result.getString("phone");
                    String password = result.getString("password");
                    Subscriber subscriber = new Subscriber(username, password, cnp, name, address, phone);
                    subscriber.setId(id);
                    logger.traceExit(subscriber);
                    return Optional.of(subscriber);
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
    public Iterable<Subscriber> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Subscriber> subscribers = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Subscriber")){
            try(ResultSet result = preStmt.executeQuery()) {
                while(result.next()) {
                    Long id = result.getLong("id");
                    String username = result.getString("username");
                    String cnp = result.getString("cnp");
                    String name = result.getString("name");
                    String address = result.getString("address");
                    String phone = result.getString("phone");
                    String password = result.getString("password");
                    Subscriber subscriber = new Subscriber(username, password, cnp, name, address, phone);
                    subscriber.setId(id);
                    subscribers.add(subscriber);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return subscribers;
    }

    @Override
    public void save(Subscriber entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into Subscriber (username, cnp, name, address, phone, password) values (?,?,?,?,?, ?)")){
            preStmt.setString(1, entity.getUsername());
            preStmt.setString(2, entity.getCnp());
            preStmt.setString(3, entity.getName());
            preStmt.setString(4, entity.getAddress());
            preStmt.setString(5, entity.getPhone());
            preStmt.setString(6, entity.getPassword());
            int result = preStmt.executeUpdate();
            logger.trace("Saved {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
    }

    @Override
    public Optional<Subscriber> delete(Long aLong) {
        return Optional.empty();
    }

    @Override
    public Optional<Subscriber> update(Subscriber entity) {
        return Optional.empty();
    }
}
