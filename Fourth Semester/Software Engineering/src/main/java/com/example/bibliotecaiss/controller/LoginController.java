package com.example.bibliotecaiss.controller;

import com.example.bibliotecaiss.Main;
import com.example.bibliotecaiss.domain.Librarian;
import com.example.bibliotecaiss.domain.Subscriber;
import com.example.bibliotecaiss.service.Service;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Modality;
import javafx.stage.Stage;

public class LoginController {
    public Button bttnLogin;
    private Service service;
    private Stage stage;

    private Main main;

    @FXML
    private TextField textUsername;

    @FXML
    private TextField textPassword;

    public void setService(Service service, Stage stage){
        this.service = service;
        this.stage = stage;
    }

    public void handleLogin(){
        if (textUsername.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a username");
        }
        else if (textPassword.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a password");
        }
        else {
            Subscriber subscriber = service.findSubscriberByUsername(textUsername.getText());
            if (subscriber != null && service.loginSubscriber(textUsername.getText(), textPassword.getText())){
                try {
                    Subscriber subscriber1 = service.findSubscriberByUsername(textUsername.getText());
                    main.openSubscriberStage(subscriber1);
                    stage.hide();
                } catch (Exception e){
                    MessageAlert.showErrorMessage(null, "Error: " + e.getMessage());
                }
            }
            else if(service.loginLibrarian(textUsername.getText(), textPassword.getText())){
                try {
                    Librarian librarian = service.findLibrarianByUsername(textUsername.getText());
                    main.openLibrarianStage(librarian);
                    stage.hide();
                } catch (Exception e){
                    MessageAlert.showErrorMessage(null, "Error: " + e.getMessage());
                }
            }
            else {
                MessageAlert.showErrorMessage(null, "Incorrect login data");
            }
        }
    }

    public void handleCreateAccount(){
        try{
            FXMLLoader registerLoader = new FXMLLoader(getClass().getResource("/com/example/bibliotecaiss/register-view.fxml"));
            AnchorPane root = registerLoader.load();

            Stage registerStage = new Stage();
            registerStage.setTitle("Register");
            registerStage.initModality(Modality.WINDOW_MODAL);
            registerStage.setResizable(true);
            Scene scene = new Scene(root, 300, 300);
            registerStage.setScene(scene);

            RegisterController registerController = registerLoader.getController();
            registerController.setService(service, registerStage);
            registerController.setMain(main);

            registerStage.show();

            stage.hide();
        } catch (Exception e){
            MessageAlert.showErrorMessage(null, "Error: " + e.getMessage());
        }
    }

    public void setMain(Main main){
        this.main = main;
    }

}
