package com.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.*;

public class UserDBRepository implements IUserRepository {
    private final JdbcUtils dbUtils;

    private static final Logger logger= LogManager.getLogger();

    public UserDBRepository(Properties props){
        logger.info("Initializing UserDBRepository with properties: {}",props);
        dbUtils=new JdbcUtils(props);
    }


    @Override
    public Optional<User> findOne(Long userId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from user where id = ?")){
            preStmt.setLong(1, userId);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    String username = result.getString("username");
                    String name = result.getString("name");
                    String password = result.getString("password");
                    User user = new User(username, name, password);
                    user.setId(id);
                    logger.traceExit(user);
                    return Optional.of(user);
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
    public Iterable<User> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<User> users = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from user")){
            try(ResultSet result = preStmt.executeQuery()) {
                while(result.next()) {
                    Long id = result.getLong("id");
                    String username = result.getString("username");
                    String name = result.getString("name");
                    String password = result.getString("password");
                    User user = new User(username, name, password);
                    user.setId(id);
                    users.add(user);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(users);
        return users;

    }

    @Override
    public void save(User entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into user (username, name, password) values (?,?,?)")){
            preStmt.setString(1, entity.getUsername());
            preStmt.setString(2, entity.getName());
            preStmt.setString(3, entity.getPassword());
            int result = preStmt.executeUpdate();
            logger.trace("Saved {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();

    }

    @Override
    public Optional<User> delete(Long userId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("delete from user where id = ?")){
            preStmt.setLong(1, userId);
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
    public Optional<User> update(User entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("update user set username = ?, name = ?, password = ? where id = ?")){
            preStmt.setString(1, entity.getUsername());
            preStmt.setString(2, entity.getName());
            preStmt.setString(3, entity.getPassword());
            preStmt.setLong(4, entity.getId());
            int result = preStmt.executeUpdate();
            logger.trace("Updated {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return Optional.of(entity);
    }

    @Override
    public User findByUsername(String username) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try (PreparedStatement preStmt = con.prepareStatement("select * from user where username = ?")) {
            preStmt.setString(1, username);
            try (ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    String name = result.getString("name");
                    String password = result.getString("password");
                    User user = new User(username, name, password);
                    user.setId(id);
                    logger.traceExit(user);
                    return user;
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB" + e);
        }
        logger.traceExit();
        return null;
    }
    public String hashPassword(String password){
        try{
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(password.getBytes());
            byte[] digest = md.digest();
            return Base64.getEncoder().encodeToString(digest);
        } catch(NoSuchAlgorithmException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public User findBy(String username, String pass) {
        System.out.println("JDBC findBy 2 params");
        Connection con=dbUtils.getConnection();
        try(PreparedStatement preStmt=con.prepareStatement("select name from user where username=? and password=?")){
            preStmt.setString(1,username);
            preStmt.setString(2,pass);
            ResultSet result=preStmt.executeQuery();
            boolean resOk=result.next();
            System.out.println("findBy user, pass "+resOk);
            if (resOk) {
                String name = result.getString("name"); // Extract the name from the result
                return new User(name, username, pass);
            }
        } catch (SQLException e) {
            System.out.println("Error DB "+e);
        }
        return null;
    }
}
