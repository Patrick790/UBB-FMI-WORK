package com.example.bibliotecaiss.service;

import com.example.bibliotecaiss.domain.Book;
import com.example.bibliotecaiss.domain.Borrowing;
import com.example.bibliotecaiss.domain.Subscriber;
import com.example.bibliotecaiss.domain.Terminal;

import java.util.Optional;

public interface IService {
    public boolean loginSubscriber(String username, String password);

    public boolean loginLibrarian(String username, String password);
    public Subscriber findSubscriberByUsername(String username);
    public void addBook(Book book);
    public Iterable<Book> getAllBooks();
    public void deleteBook(Long id);
    public void modifyBook(Book book);
    public Iterable<Borrowing> getAllBorrowings();
    public int getAvailableQuantity(Long bookId);
    public void addBorrowing(Borrowing borrowing);
    public Iterable<Terminal> getAllTerminals();
    public Optional<Book> findByTitle(String title);

    Optional<Book> findBookById(Long id);
    void returnBook(Long borrowingID);
    Optional<Subscriber> findSubscriberById(Long id);
    void acceptReturn(Long borrowingID);
    void refuseReturn(Long borrowingID);
}
