package com.client;

import com.client.gui.UsersController;
import com.client.gui.LoginController;
import com.example.User;
import com.network.rpcprotocol.MotorcyclesServicesRpcProxy;
import com.services.IMotorcyclesServices;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Properties;

public class StartRpcClientFX extends Application {

    private IMotorcyclesServices service;

    private static int defaultChatPort = 55555;
    private static String defaultServer = "localhost";

    @Override
    public void start(Stage primaryStage) throws Exception {
        System.out.println("In start");
        Properties clientProps = new Properties();
        try {
            clientProps.load(StartRpcClientFX.class.getResourceAsStream("/motorcyclesclient.properties"));
            System.out.println("Client properties set. ");
            clientProps.list(System.out);
        } catch (IOException e) {
            System.err.println("Cannot find motorcyclesclient.properties " + e);
            return;
        }

        String serverIP = clientProps.getProperty("com.server.host", defaultServer);
        int serverPort = defaultChatPort;

        try {
            serverPort = Integer.parseInt(clientProps.getProperty("com.server.port"));
        } catch (NumberFormatException ex) {
            System.err.println("Wrong port number " + ex.getMessage());
            System.out.println("Using default port: " + defaultChatPort);
        }
        System.out.println("Using server IP " + serverIP);
        System.out.println("Using server port " + serverPort);

        service = new MotorcyclesServicesRpcProxy(serverIP, serverPort);

        loginStage(primaryStage);
    }


    public void openUserStage(User user) throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(StartRpcClientFX.class.getResource("/users-view.fxml"));
        Stage userStage = new Stage();
        Scene userScene = new Scene(fxmlLoader.load());

        userStage.setTitle("Motorcycles App");
        userStage.setScene(userScene);

        UsersController usersController = fxmlLoader.getController();
        usersController.setService(user, service, userStage, this);

        userStage.show();
    }

    public void loginStage(Stage primaryStage)throws Exception{
        FXMLLoader loginLoader = new FXMLLoader(getClass().getResource("/login.fxml"));

        VBox loginVbox = loginLoader.load();
        LoginController loginController = loginLoader.getController();
        loginController.setStartRpcClientFX(this);

        Scene scene = new Scene(loginVbox);

        primaryStage.setTitle("Motorcycles App");
        primaryStage.setScene(scene);

        loginController.setService(service, primaryStage);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch();

    }
}