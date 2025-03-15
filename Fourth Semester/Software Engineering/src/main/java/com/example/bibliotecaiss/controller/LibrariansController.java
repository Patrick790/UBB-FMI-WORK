package com.example.bibliotecaiss.controller;

import com.example.bibliotecaiss.Main;
import com.example.bibliotecaiss.domain.Book;
import com.example.bibliotecaiss.domain.Borrowing;
import com.example.bibliotecaiss.domain.Librarian;
import com.example.bibliotecaiss.domain.Subscriber;
import com.example.bibliotecaiss.service.IService;
import com.example.bibliotecaiss.service.Service;
import javafx.beans.property.SimpleStringProperty;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.util.Objects;
import java.util.Optional;
import java.util.Random;

public class LibrariansController {
    public Button logoutButton;
    public Button acceptReturnButton;
    public Button refuseButton;
    private IService service;
    private Stage stage;
    private Main main;
    private Librarian librarian;
    @FXML
    TableView<Book> booksTableView;

    @FXML
    TableColumn<Book, Long> bookId;
    @FXML
    TableColumn<Book, String> bookTitle;
    @FXML
    TableColumn<Book, Integer> quantity;

    @FXML
    TextField titleField;
    @FXML
    TextField authorField;
    @FXML
    TextField quantityField;
    @FXML
    Button addBookButton;
    @FXML
    Button deleteBookButton;
    @FXML
    Button modifyBookButton;

    public void setService(Librarian librarian, IService service, Stage stage, Main main) {

        this.librarian = librarian;
        this.service = service;
        this.stage = stage;
        this.main = main;
        initializeBooks();
        initializeBorrowings();

        booksTableView.getSelectionModel().selectedItemProperty().addListener((obs, oldSelection, newSelection) -> {
            if (newSelection != null) {
                titleField.setText(newSelection.getTitle());
                authorField.setText(newSelection.getAuthor());
                quantityField.setText(String.valueOf(newSelection.getQuantity()));
            }
        });

        booksTableView.addEventHandler(MouseEvent.MOUSE_CLICKED, new EventHandler<MouseEvent>() {
            public void handle(MouseEvent event) {
                if (event.getClickCount() == 2) {
                    Book selectedBook = booksTableView.getSelectionModel().getSelectedItem();
                    if (selectedBook != null) {
                        handleDoubleClickOnBook(selectedBook);
                    }
                }
            }
        });

    }

    private void initModelBooks(){
        Iterable<Book> books = service.getAllBooks();
        booksTableView.getItems().clear();
        for(Book book : books){
            booksTableView.getItems().add(book);
        }
    }

    private void initializeBooks(){
        bookId.setCellValueFactory(new PropertyValueFactory<>("id"));
        bookTitle.setCellValueFactory(new PropertyValueFactory<>("title"));
        quantity.setCellValueFactory(new PropertyValueFactory<>("quantity"));
        initModelBooks();
    }

    private void handleDoubleClickOnBook(Book book) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Book Details");
        alert.setHeaderText(null);
        alert.setContentText("Title: " + book.getTitle() + "\n"
                + "Author: " + book.getAuthor() + "\n"
                + "Quantity: " + book.getQuantity());

        alert.showAndWait();
    }

    public void handleAddBook(){
        String title = titleField.getText();
        String author = authorField.getText();
        int quantity = Integer.parseInt(quantityField.getText());
        if(title.isEmpty() || author.isEmpty() || quantity == 0){
            MessageAlert.showErrorMessage(null, "Please complete title and author fields!");
        } else {
            Book book = new Book(title, author, quantity);
            Long id = new Random().nextLong();
            book.setId(id);
            service.addBook(book);
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Book added", "Book was added successfully!");
            titleField.clear();
            authorField.clear();
            quantityField.clear();
            initModelBooks();
        }
    }

    public void handleDeleteBook(){
        Book book = booksTableView.getSelectionModel().getSelectedItem();
        if(book == null){
            MessageAlert.showErrorMessage(null, "Please select a book!");
        } else {
            service.deleteBook(book.getId());
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Book deleted", "Book was deleted successfully!");
        }
        initModelBooks();

    }

    public void handleLogout() throws Exception{
        Stage stage = (Stage) logoutButton.getScene().getWindow();
        stage.close();
        main.loginStage(new Stage());
    }

    public void handleModifyBook() {
        Book selectedBook = booksTableView.getSelectionModel().getSelectedItem();
        if (selectedBook != null) {
            String newTitle = titleField.getText();
            String newAuthor = authorField.getText();
            int newQuantity = Integer.parseInt(quantityField.getText());

            selectedBook.setTitle(newTitle);
            selectedBook.setAuthor(newAuthor);
            selectedBook.setQuantity(newQuantity);

            service.modifyBook(selectedBook);
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Book modified", "Book was modified successfully!");

            initModelBooks();
        } else {
            MessageAlert.showErrorMessage(null, "Please select a book!");
        }
    }

    @FXML
    TableView<Borrowing> restituiriTableView;
    @FXML
    TableColumn<Borrowing, String> bSubscriberColumn;
    @FXML
    TableColumn<Borrowing, String> bTitleColumn;
    @FXML
    TableColumn<Borrowing, String> bStatusColumn;
    @FXML
    TableColumn<Borrowing, LocalDateTime> bDataColumn;

    private void initModelBorrowings(){
        Iterable<Borrowing> borrowings = service.getAllBorrowings();
        restituiriTableView.getItems().clear();
        for(Borrowing borrowing : borrowings){
            if(Objects.equals(borrowing.getStatus(), "CERERE RETUR")){
                Optional<Book> bookOpt = service.findBookById(borrowing.getBook().getId());
                if (bookOpt.isPresent()){
                    borrowing.setBook(bookOpt.get());
                }
                Optional<Subscriber> subsOpt = service.findSubscriberById(borrowing.getSubscriber().getId());
                if (subsOpt.isPresent()){
                    borrowing.setSubscriber(subsOpt.get());
                }
                restituiriTableView.getItems().add(borrowing);
            }
        }
    }

    private void initializeBorrowings(){
        bSubscriberColumn.setCellValueFactory(cellData -> new SimpleStringProperty(cellData.getValue().getSubscriber().getUsername()));
        bTitleColumn.setCellValueFactory(cellData -> new SimpleStringProperty(cellData.getValue().getBook().getTitle()));
        bStatusColumn.setCellValueFactory(new PropertyValueFactory<>("status"));
        bDataColumn.setCellValueFactory(new PropertyValueFactory<>("borrowingDate"));
        initModelBorrowings();
    }

    public void handleAcceptReturn(){
        Borrowing selectedBorrowing = restituiriTableView.getSelectionModel().getSelectedItem();

        if(selectedBorrowing == null){
            MessageAlert.showErrorMessage(null, "Please select a borrowing!");
        } else {
            service.acceptReturn(selectedBorrowing.getId());
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Return accepted", "Return was accepted successfully!");
            initModelBorrowings();
        }
    }

    public void handleRefuseReturn(){
        Borrowing selectedBorrowing = restituiriTableView.getSelectionModel().getSelectedItem();

        if(selectedBorrowing == null){
            MessageAlert.showErrorMessage(null, "Please select a borrowing!");
        } else {
            service.refuseReturn(selectedBorrowing.getId());
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Return refused", "Return was refused successfully!");
            initModelBorrowings();
        }
    }








}
