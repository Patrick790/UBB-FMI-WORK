package com.example.bibliotecaiss.service;

import com.example.bibliotecaiss.domain.*;
import com.example.bibliotecaiss.repository.*;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.stream.StreamSupport;
import java.util.stream.Collectors;
import java.util.Objects;
import java.util.Optional;
import java.util.Random;

public class Service implements IService{
    private ISubscriberRepository subscriberRepo;
    private ILibrarianRepository librarianRepo;
    private IBookRepository bookRepo;
    private IBorrowingRepository borrowingRepo;
    private ITerminalRepository terminalRepo;

    public Service(ISubscriberRepository subscriberRepo, ILibrarianRepository librarianRepo, IBookRepository bookRepo, IBorrowingRepository borrowingRepo, ITerminalRepository terminalRepo) {
        this.subscriberRepo = subscriberRepo;
        this.librarianRepo = librarianRepo;
        this.bookRepo = bookRepo;
        this.borrowingRepo = borrowingRepo;
        this.terminalRepo = terminalRepo;
    }
    @Override
    public boolean loginSubscriber(String username, String password) {
        Long idSubscriber = findSubscriberByUsername(username).getId();
        Optional<Subscriber> subs = subscriberRepo.findOne(idSubscriber);
        if(subs.isPresent()) {
            return Objects.equals(subs.get().getPassword(), password);
        } else {
            throw new RuntimeException("Subscriber does not exist");
        }

    }

    @Override
    public boolean loginLibrarian(String username, String password) {
        Long idLibrarian = findLibrarianByUsername(username).getId();
        Optional<Librarian> lib = librarianRepo.findOne(idLibrarian);
        if(lib.isPresent()) {
            return Objects.equals(lib.get().getPassword(), password);
        } else {
            throw new RuntimeException("Subscriber does not exist");
        }

    }

    public Subscriber findSubscriberByUsername(String username) {
        for(Subscriber s : subscriberRepo.findAll())
            if(Objects.equals(s.getUsername(), username)) {
                return s;
            }
        return null;
    }

    public Librarian findLibrarianByUsername(String username) {
        for(Librarian l : librarianRepo.findAll())
            if(Objects.equals(l.getUsername(), username)) {
                return l;
            }
        return null;
    }

    public void registerSubscriber(Subscriber subscriber) {

        subscriberRepo.save(subscriber);

    }

    public String generatePassword() {
        Random random = new Random();
        return String.format("%06d", random.nextInt(1000000));
    }

    public void addBook(Book book){
        if(bookRepo.findOne(book.getId()).isPresent())
            throw new RuntimeException("Book already exists");
        bookRepo.save(book);

    }

    public Iterable<Book> getAllBooks() {
        return bookRepo.findAll();
    }

    public void deleteBook(Long id) {
        Optional<Book> bookToDelete = bookRepo.findOne(id);
        if(bookToDelete.isEmpty())
            throw new RuntimeException("Book does not exist");
        bookRepo.delete(id);
    }

    public void modifyBook(Book book) {
        Optional<Book> bookToModify = bookRepo.findOne(book.getId());
        if(bookToModify.isEmpty())
            throw new RuntimeException("Book does not exist");
        bookRepo.update(book);
    }

    // In Service.java
    public void addBorrowing(Borrowing borrowing){
        // Get the book from the repo
        Optional<Book> bookOptional = bookRepo.findOne(borrowing.getBook().getId());

        if (bookOptional.isPresent()) {
            Book book = bookOptional.get();

            // Update the book in the repo
            bookRepo.update(book);

            // Format the LocalDateTime to a string
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            String formattedBorrowingDate = LocalDateTime.now().format(formatter);

            borrowing.setBorrowingDate(LocalDateTime.parse(formattedBorrowingDate, formatter));

            // Save the borrowing to the repo
            borrowingRepo.save(borrowing);

        } else {
            throw new RuntimeException("Book does not exist");
        }
    }

    public Iterable<Borrowing> getAllBorrowings(){
        return borrowingRepo.findAll();
    }

    public int getAvailableQuantity(Long bookId) {
        Optional<Book> book = bookRepo.findOne(bookId);
        if (book.isPresent()) {
            int totalQuantity = book.get().getQuantity();
            Iterable<Borrowing> borrowings = getAllBorrowings();
            List<Borrowing> borrowingList = StreamSupport.stream(borrowings.spliterator(), false).toList();
            int borrowedQuantity = (int) borrowingList.stream()
                    .filter(borrowing -> borrowing.getBook().getId().equals(bookId) && !borrowing.getStatus().equals("RETURNAT"))
                    .count();
            return totalQuantity - borrowedQuantity;
        } else {
            throw new RuntimeException("Book does not exist");
        }
    }

    public Iterable<Terminal> getAllTerminals() {
        return terminalRepo.findAll();
    }


    public Optional<Book> findByTitle(String title){
        return bookRepo.findByTitle(title);
    }

    public Optional<Book> findBookById(Long id) {
        return bookRepo.findOne(id);
    }

    public void returnBook(Long borrowingID){
        Optional<Borrowing> borrowingOpt = borrowingRepo.findOne(borrowingID);

        if(borrowingOpt.isPresent()){
            Borrowing borrowing = borrowingOpt.get();
            borrowing.setStatus("CERERE RETUR");
            borrowing.setBorrowingDate(LocalDateTime.now());
            borrowingRepo.update(borrowing);
        } else {
            throw new RuntimeException("Borrowing does not exist");
        }
    }

    public Optional<Subscriber> findSubscriberById(Long id) {
        return subscriberRepo.findOne(id);
    }

    public void acceptReturn(Long borrowingID){
        Optional<Borrowing> borrowingOpt = borrowingRepo.findOne(borrowingID);

        if(borrowingOpt.isPresent()){
            Borrowing borrowing = borrowingOpt.get();
            borrowing.setStatus("RETURNAT");
            borrowing.setReturnDate(LocalDateTime.now());
            borrowingRepo.update(borrowing);
        } else {
            throw new RuntimeException("Borrowing does not exist");
        }
    }

    public void refuseReturn(Long borrowingID){
        Optional<Borrowing> borrowingOpt = borrowingRepo.findOne(borrowingID);

        if(borrowingOpt.isPresent()){
            Borrowing borrowing = borrowingOpt.get();
            borrowing.setStatus("RETUR REFUZAT");
            borrowingRepo.update(borrowing);
        } else {
            throw new RuntimeException("Borrowing does not exist");
        }
    }






}
