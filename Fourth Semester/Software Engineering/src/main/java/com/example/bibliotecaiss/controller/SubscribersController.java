package com.example.bibliotecaiss.controller;

import com.example.bibliotecaiss.Main;
import com.example.bibliotecaiss.domain.Book;
import com.example.bibliotecaiss.domain.Borrowing;
import com.example.bibliotecaiss.domain.Subscriber;
import com.example.bibliotecaiss.domain.Terminal;
import com.example.bibliotecaiss.service.IService;
import javafx.beans.property.SimpleStringProperty;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Optional;

public class SubscribersController {

    private IService service;
    private Stage stage;
    private Main main;
    private Subscriber subscriber;

    @FXML
    TableView<Book> ExemplareTableView;
    @FXML
    TableColumn<Book, String> titluColumn;
    @FXML
    TableColumn<Book, String> autorColumn;
    @FXML
    TableColumn<Borrowing, Integer> disponibilitateColumn;

    @FXML
    Button logoutButton;
    @FXML
    Button borrowButton;
    @FXML
    Button restituireButton;

    @FXML
    ChoiceBox<Terminal> terminalChoiceBox;

    @FXML
    TextField titleField;
    @FXML
    Button searchButton;
    @FXML
    Button resetButton;

    public void setService(Subscriber subscriber, IService service, Stage stage, Main main) {
        this.subscriber = subscriber;
        this.service = service;
        this.stage = stage;
        this.main = main;

        initializeBooks();
        initializeTerminals();
        initializeBorrowings();
    }

    private void initModelBooks(){
        Iterable<Book> books = service.getAllBooks();
        ExemplareTableView.getItems().clear();
        for(Book book : books){
            int availableQuantity = service.getAvailableQuantity(book.getId());
            Book bookWithAvailableQuantity = new Book(book.getTitle(), book.getAuthor(), availableQuantity);
            bookWithAvailableQuantity.setId(book.getId()); // Set the id of the book
            ExemplareTableView.getItems().add(bookWithAvailableQuantity);
        }
    }

    private void initializeBooks(){
        titluColumn.setCellValueFactory(new PropertyValueFactory<>("title"));
        autorColumn.setCellValueFactory(new PropertyValueFactory<>("author"));
        disponibilitateColumn.setCellValueFactory(new PropertyValueFactory<>("quantity"));
        initModelBooks();
    }

    private void initializeTerminals() {
        Iterable<Terminal> terminals = service.getAllTerminals();
        for(Terminal terminal : terminals){
            terminalChoiceBox.getItems().add(terminal);
        }
    }

    public void handleBorrow(){
        Book selectedBook = ExemplareTableView.getSelectionModel().getSelectedItem();
        Terminal selectedTerminal = terminalChoiceBox.getSelectionModel().getSelectedItem();

        if(selectedBook == null || selectedTerminal == null){
            MessageAlert.showErrorMessage(null, "Select a book and a terminal");
        } else if (service.getAvailableQuantity(selectedBook.getId()) == 0) {
            MessageAlert.showErrorMessage(null, "No more available books");
        } else {
            Borrowing borrowing = new Borrowing(selectedBook, subscriber, selectedTerminal);
            borrowing.setStatus("ACTIV");
            borrowing.setReturnDate(null);

            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            String formattedBorrowingDate = LocalDateTime.now().format(formatter);

            borrowing.setBorrowingDate(LocalDateTime.parse(formattedBorrowingDate, formatter));

            service.addBorrowing(borrowing);
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Book borrowed", "Book successfully borrowed!");
            initModelBooks();
            initializeBorrowings();
        }
    }

    public void handleLogout() throws Exception {
        Stage stage = (Stage) logoutButton.getScene().getWindow();
        stage.close();
        main.loginStage(new Stage());
    }

    public void handleSearch(){
        String title = titleField.getText();
        Optional<Book> bookOpt = service.findByTitle(title);
        if(bookOpt.isPresent()){
            Book book = bookOpt.get();
            ExemplareTableView.getItems().clear();
            int availableQuantity = service.getAvailableQuantity(book.getId());
            Book bookWithAvailableQuantity = new Book(book.getTitle(), book.getAuthor(), availableQuantity);
            bookWithAvailableQuantity.setId(book.getId());
            ExemplareTableView.getItems().add(bookWithAvailableQuantity);
        } else {
            MessageAlert.showErrorMessage(null, "Book not found");
        }
    }

    public void handleReset(){
        titleField.clear();
        initModelBooks();
    }

    @FXML
    TableView<Borrowing> borrowingsTableView;
    @FXML
    TableColumn<Borrowing, String> bTitleColumn;
    @FXML
    TableColumn<Borrowing, LocalDateTime> bDataColumn;
    @FXML
    TableColumn<Borrowing, String> bStatusColumn;

    private void initModelBorrowings(){
        Iterable<Borrowing> borrowings = service.getAllBorrowings();
        borrowingsTableView.getItems().clear();
        for(Borrowing borrowing : borrowings){
            if(borrowing.getSubscriber().getId().equals(subscriber.getId()) && !borrowing.getStatus().equals("RETURNAT")){
                Optional<Book> bookOpt = service.findBookById(borrowing.getBook().getId());
                if(bookOpt.isPresent()){
                    borrowing.setBook(bookOpt.get());
                }
                borrowingsTableView.getItems().add(borrowing);
            }
        }
    }

    private void initializeBorrowings(){
        bTitleColumn.setCellValueFactory(cellData -> new SimpleStringProperty(cellData.getValue().getBook().getTitle()));
        bDataColumn.setCellValueFactory(new PropertyValueFactory<>("borrowingDate"));
        bStatusColumn.setCellValueFactory(new PropertyValueFactory<>("status"));
        initModelBorrowings();
    }

    public void handleReturn(){
        Borrowing selectedBorrowing = borrowingsTableView.getSelectionModel().getSelectedItem();

        if(selectedBorrowing == null){
            MessageAlert.showErrorMessage(null, "Select a borrowing");
        } else {
            service.returnBook(selectedBorrowing.getId());
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Return request ", "Return request registered!");
            initModelBorrowings();
        }
    }
}
