package com.example.bibliotecaiss.domain;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Borrowing extends Entity<Long>{

    private Subscriber subscriber;

    private Book book;

    private Terminal terminal;
    private LocalDateTime borrowingDate;
    private LocalDateTime returnDate;
    private String status;
    public Borrowing(Book book, Subscriber subscriber, Terminal terminal) {
        this.book = book;
        this.subscriber = subscriber;
        this.terminal = terminal;
        this.borrowingDate = LocalDateTime.now();

    }

    public Subscriber getSubscriber() {
        return subscriber;
    }

    public void setSubscriber(Subscriber subscriber) {
        this.subscriber = subscriber;
    }

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }

    public Terminal getTerminal() {
        return terminal;
    }

    public void setTerminal(Terminal terminal) {
        this.terminal = terminal;
    }

    public LocalDateTime getBorrowingDate() {
        return borrowingDate;
    }

    public void setBorrowingDate(LocalDateTime borrowingDate) {
        this.borrowingDate = borrowingDate;
    }

    public LocalDateTime getReturnDate() {
        return returnDate;
    }

    public void setReturnDate(LocalDateTime returnDate) {
        this.returnDate = returnDate;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    // In Borrowing.java
    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String formattedBorrowingDate = getBorrowingDate().format(formatter);
        String formattedReturnDate = getReturnDate() != null ? getReturnDate().format(formatter) : null;

        return "Borrowing{" +
                "id=" + getId() +
                ", subscriber=" + subscriber +
                ", book=" + book +
                ", terminal=" + terminal +
                ", borrowingDate=" + formattedBorrowingDate +
                ", returnDate=" + formattedReturnDate +
                ", status='" + status + '\'' +
                '}';
    }
}
