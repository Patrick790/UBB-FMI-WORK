package com.example.bibliotecaiss.repository;

import com.example.bibliotecaiss.domain.Terminal;
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

public class TerminalDBRepository implements ITerminalRepository{

    private final JdbcUtils dbUtils;
    private static final Logger logger = LogManager.getLogger();

    public TerminalDBRepository(Properties props){
        logger.info("Initializing TerminalDBRepository with properties: {}",props);
        dbUtils = new JdbcUtils(props);
    }
    @Override
    public Optional<Terminal> findOne(Long terminalId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Terminal where id = ?")){
            preStmt.setLong(1, terminalId);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    String location = result.getString("location");
                    Terminal terminal = new Terminal(location);
                    terminal.setId(id);
                    logger.traceExit(terminal);
                    return Optional.of(terminal);
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
    public Iterable<Terminal> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Terminal> terminals = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Terminal")){
            try(ResultSet result = preStmt.executeQuery()) {
                while (result.next()) {
                    Long id = result.getLong("id");
                    String location = result.getString("location");
                    Terminal terminal = new Terminal(location);
                    terminal.setId(id);
                    terminals.add(terminal);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return terminals;
    }

    @Override
    public void save(Terminal entity) {

    }

    @Override
    public Optional<Terminal> delete(Long aLong) {
        return Optional.empty();
    }

    @Override
    public Optional<Terminal> update(Terminal entity) {
        return Optional.empty();
    }
}
