package com.example.bibliotecaiss.repository;

import com.example.bibliotecaiss.domain.Book;

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

public class BookDBRepository implements IBookRepository{

    private final JdbcUtils dbUtils;

    private static final Logger logger = LogManager.getLogger();

    public BookDBRepository(Properties props) {
        logger.info("Initializing BookDBRepository with dbUtils: {}",props);
        this.dbUtils = new JdbcUtils(props);
    }
    @Override
    public Optional<Book> findOne(Long bookId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Book where id = ?")){
            preStmt.setLong(1, bookId);
            try(ResultSet result = preStmt.executeQuery()) {
                if (result.next()) {
                    Long id = result.getLong("id");
                    String title = result.getString("title");
                    String author = result.getString("author");
                    int quantity = result.getInt("quantity");
                    Book book = new Book(title, author, quantity);
                    book.setId(id);
                    logger.traceExit(book);
                    return Optional.of(book);
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
    public Iterable<Book> findAll() {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        List<Book> books = new ArrayList<>();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Book")){
            try(ResultSet result = preStmt.executeQuery()) {
                while (result.next()) {
                    Long id = result.getLong("id");
                    String title = result.getString("title");
                    String author = result.getString("author");
                    int quantity = result.getInt("quantity");
                    Book book = new Book(title, author, quantity);
                    book.setId(id);
                    books.add(book);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit(books);
        return books;
    }

    @Override
    public void save(Book entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("insert into Book (title, author, quantity) values (?, ?, ?)")){
            preStmt.setString(1, entity.getTitle());
            preStmt.setString(2, entity.getAuthor());
            preStmt.setInt(3, entity.getQuantity());
            int result = preStmt.executeUpdate();
            logger.trace("Saved {} instances", result);
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
    }

    @Override
    public Optional<Book> delete(Long bookId) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("delete from Book where id = ?")){
            preStmt.setLong(1, bookId);
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
    public Optional<Book> update(Book entity) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("update Book set title = ?, author = ?, quantity = ? where id = ?")){
            preStmt.setString(1, entity.getTitle());
            preStmt.setString(2, entity.getAuthor());
            preStmt.setInt(3, entity.getQuantity());
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
    public Optional<Book> findByTitle(String title) {
        logger.traceEntry();
        Connection con = dbUtils.getConnection();
        try(PreparedStatement preStmt = con.prepareStatement("select * from Book where title = ?")){
            preStmt.setString(1, title);
            try(ResultSet result = preStmt.executeQuery()) {
                while (result.next()) {
                    Long id = result.getLong("id");
                    String author = result.getString("author");
                    int quantity = result.getInt("quantity");
                    Book book = new Book(title, author, quantity);
                    book.setId(id);
                    logger.traceExit(book);
                    return Optional.of(book);
                }
            }
        } catch (SQLException e) {
            logger.error(e);
            System.err.println("Error DB"+e);
        }
        logger.traceExit();
        return Optional.empty();
    }
}
