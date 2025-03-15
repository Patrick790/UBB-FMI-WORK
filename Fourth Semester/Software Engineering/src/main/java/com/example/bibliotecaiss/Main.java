package com.example.bibliotecaiss;

import com.example.bibliotecaiss.controller.LibrariansController;
import com.example.bibliotecaiss.controller.LoginController;
import com.example.bibliotecaiss.controller.RegisterController;
import com.example.bibliotecaiss.controller.SubscribersController;
import com.example.bibliotecaiss.domain.Librarian;
import com.example.bibliotecaiss.domain.Subscriber;
import com.example.bibliotecaiss.repository.*;
import com.example.bibliotecaiss.service.Service;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

public class Main extends Application {
    private Service service;
    @Override
    public void start(Stage primaryStage) throws IOException {
        Properties props = new Properties();
        try {
            props.load(new FileReader("bd.config"));
        } catch(IOException e) {
            System.out.println("Cannot find bd.config " + e);
        }

        LibrarianDBRepository librarianRepo = new LibrarianDBRepository(props);
        SubscriberDBRepository subscriberRepo = new SubscriberDBRepository(props);
        BookDBRepository bookRepo = new BookDBRepository(props);
        BorrowingDBRepository borrowingRepo = new BorrowingDBRepository(props);
        TerminalDBRepository terminalRepo = new TerminalDBRepository(props);

        service = new Service(subscriberRepo, librarianRepo, bookRepo, borrowingRepo, terminalRepo);

        loginStage(primaryStage);
    }

    public void openSubscriberStage(Subscriber subscriber) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("hello-view.fxml"));
        Stage subscriberStage = new Stage();
        Scene subscriberScene = new Scene(fxmlLoader.load());

        subscriberStage.setTitle("Subscriber");
        subscriberStage.setScene(subscriberScene);

        SubscribersController subscribersController = fxmlLoader.getController();
        subscribersController.setService(subscriber, service, subscriberStage, this);

        subscriberStage.show();


    }

    public void openLibrarianStage(Librarian librarian) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("bibliotecar-view.fxml"));
        Stage librarianStage = new Stage();
        Scene librarianScene = new Scene(fxmlLoader.load());

        librarianStage.setTitle("Librarian");
        librarianStage.setScene(librarianScene);

        LibrariansController librariansController = fxmlLoader.getController();
        librariansController.setService(librarian, service, librarianStage, this);

        librarianStage.show();


    }


    public void loginStage(Stage primaryStage) throws IOException {
        FXMLLoader loginLoader = new FXMLLoader(Main.class.getResource("login.fxml"));

        VBox loginVBox = loginLoader.load();
        LoginController loginController = loginLoader.getController();
        loginController.setMain(this);

        Scene scene = new Scene(loginVBox);

        primaryStage.setTitle("Library App");
        primaryStage.setScene(scene);

        loginController.setService(service, primaryStage);
        primaryStage.show();
    }

    public void openRegisterStage(Stage primaryStage) throws IOException {
        FXMLLoader registerLoader = new FXMLLoader(Main.class.getResource("/register-view.fxml"));

        Stage registerStage = new Stage();
        Scene registerScene = new Scene(registerLoader.load());

        registerStage.setTitle("Register");
        registerStage.setScene(registerScene);

        RegisterController registerController = registerLoader.getController();
        registerController.setService(service, primaryStage);
        registerController.setMain(this);

        registerStage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}