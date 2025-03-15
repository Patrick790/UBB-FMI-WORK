package com.example.bibliotecaiss.repository;

import com.example.bibliotecaiss.domain.Book;
import com.example.bibliotecaiss.domain.Borrowing;
import com.example.bibliotecaiss.domain.Subscriber;
import com.example.bibliotecaiss.domain.Terminal;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Properties;

public class BorrowingDBRepository implements IBorrowingRepository {

    private final JdbcUtils dbUtils;
    private static final Logger logger = LogManager.getLogger();

    public BorrowingDBRepository(Properties props) {
        logger.info("Initializing BorrowingDBRepository with properties: {}", props);
        dbUtils = new JdbcUtils(props);
    }

    @Override
    public Optional<Borrowing> findOne(Long borrowingId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try (PreparedStatement preStmt = con.prepareStatement("select * from Borrowing where id = ?")) {
            preStmt.setLong(1, borrowingId);
            try (ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    Long book_id = result.getLong("book_id");
                    Long subscriber_id = result.getLong("subscriber_id");
                    Long terminal_id = result.getLong("terminal_id");
                    Timestamp borrowing_date = result.getTimestamp("borrowing_date");
                    Timestamp return_date = result.getTimestamp("return_date");
                    String status = result.getString("status");

                    Book book = new Book(null, null, 0);
                    book.setId(book_id);
                    Subscriber subscriber = new Subscriber(null, null, null, null, null, null);
                    subscriber.setId(subscriber_id);
                    Terminal terminal = new Terminal(null);
                    terminal.setId(terminal_id);

                    LocalDateTime formattedBorrowingDate = borrowing_date.toLocalDateTime();
                    LocalDateTime formattedReturnDate = return_date != null ? return_date.toLocalDateTime() : null;

                    Borrowing borrowing = new Borrowing(book, subscriber, terminal);
                    borrowing.setId(borrowingId);
                    borrowing.setBorrowingDate(formattedBorrowingDate);
                    borrowing.setReturnDate(formattedReturnDate);
                    borrowing.setStatus(status);
                    logger.traceExit(borrowing);
                    return Optional.of(borrowing);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB" + e);
        }
        logger.traceExit();
        return Optional.empty();
    }

    @Override
    public Iterable<Borrowing> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Borrowing> borrowings = new ArrayList<>();
        try (PreparedStatement preStmt = con.prepareStatement("select * from Borrowing")) {
            try (ResultSet result = preStmt.executeQuery()) {
                while (result.next()) {
                    Long id = result.getLong("id");
                    Long book_id = result.getLong("book_id");
                    Long subscriber_id = result.getLong("subscriber_id");
                    Long terminal_id = result.getLong("terminal_id");
                    Timestamp borrowing_date = result.getTimestamp("borrowing_date");
                    Timestamp return_date = result.getTimestamp("return_date");
                    String status = result.getString("status");

                    Book book = new Book(null, null, 0);
                    book.setId(book_id);
                    Subscriber subscriber = new Subscriber(null, null, null, null, null, null);
                    subscriber.setId(subscriber_id);
                    Terminal terminal = new Terminal(null);
                    terminal.setId(terminal_id);

                    Borrowing borrowing = new Borrowing(book, subscriber, terminal);
                    borrowing.setId(id);
                    borrowing.setBorrowingDate(borrowing_date.toLocalDateTime());
                    borrowing.setReturnDate(return_date != null ? return_date.toLocalDateTime() : null);
                    borrowing.setStatus(status);
                    borrowings.add(borrowing);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB" + e);
        }
        logger.traceExit(borrowings);
        return borrowings;
    }

    @Override
    public void save(Borrowing entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try (PreparedStatement preStmt = con.prepareStatement("insert into Borrowing(book_id, subscriber_id, terminal_id, borrowing_date, return_date, status) values (?,?,?,?,?,?)")) {
            preStmt.setLong(1, entity.getBook().getId());
            preStmt.setLong(2, entity.getSubscriber().getId());
            preStmt.setLong(3, entity.getTerminal().getId());
            preStmt.setTimestamp(4, Timestamp.valueOf(entity.getBorrowingDate()));
            if (entity.getReturnDate() != null) {
                preStmt.setTimestamp(5, Timestamp.valueOf(entity.getReturnDate()));
            } else {
                preStmt.setNull(5, Types.TIMESTAMP);
            }
            preStmt.setString(6, entity.getStatus());
            int result = preStmt.executeUpdate();
            logger.trace("Saved {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB" + e);
        }
    }

    @Override
    public Optional<Borrowing> delete(Long aLong) {
        return Optional.empty();
    }

    @Override
    public Optional<Borrowing> update(Borrowing entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try (PreparedStatement preStmt = con.prepareStatement("update Borrowing set book_id = ?, subscriber_id = ?, terminal_id = ?, borrowing_date = ?, return_date = ?, status = ? where id = ?")) {
            preStmt.setLong(1, entity.getBook().getId());
            preStmt.setLong(2, entity.getSubscriber().getId());
            preStmt.setLong(3, entity.getTerminal().getId());
            preStmt.setTimestamp(4, Timestamp.valueOf(entity.getBorrowingDate()));
            if (entity.getReturnDate() != null) {
                preStmt.setTimestamp(5, Timestamp.valueOf(entity.getReturnDate()));
            } else {
                preStmt.setNull(5, Types.TIMESTAMP);
            }
            preStmt.setString(6, entity.getStatus());
            preStmt.setLong(7, entity.getId());
            int result = preStmt.executeUpdate();
            logger.trace("Updated {} instances", result);
            return Optional.of(entity);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB" + e);
        }
        logger.traceExit();
        return Optional.empty();
    }
}
