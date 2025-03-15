package com.example.bibliotecaiss.repository;

import com.example.bibliotecaiss.domain.Librarian;
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

public class LibrarianDBRepository implements ILibrarianRepository{
    private final JdbcUtils dbUtils;

    private static final Logger logger = LogManager.getLogger();

    public LibrarianDBRepository(Properties props){
        logger.info("Initializing LibrarianDBRepository with properties: {}",props);
        dbUtils = new JdbcUtils(props);
    }
    @Override
    public Optional<Librarian> findOne(Long aLong) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Librarian where id = ?")){
            preStmt.setLong(1, aLong);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    String username = result.getString("username");
                    String password = result.getString("password");
                    String name = result.getString("name");
                    Librarian librarian = new Librarian(username, password, name);
                    librarian.setId(id);
                    logger.traceExit(librarian);
                    return Optional.of(librarian);
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
    public Iterable<Librarian> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Librarian> librarians = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Librarian")){
            try(ResultSet result = preStmt.executeQuery()) {
                while (result.next()) {
                    Long id = result.getLong("id");
                    String username = result.getString("username");
                    String password = result.getString("password");
                    String name = result.getString("name");
                    Librarian librarian = new Librarian(username, password, name);
                    librarian.setId(id);
                    librarians.add(librarian);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(librarians);
        return librarians;
    }

    @Override
    public void save(Librarian entity) {
    }

    @Override
    public Optional<Librarian> delete(Long aLong) {
        return Optional.empty();
    }

    @Override
    public Optional<Librarian> update(Librarian entity) {
        return Optional.empty();
    }
}
