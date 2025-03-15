package com.example.bibliotecaiss.controller;

import com.example.bibliotecaiss.Main;
import com.example.bibliotecaiss.domain.Subscriber;
import com.example.bibliotecaiss.service.Service;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class RegisterController {
    private Service service;
    private Stage stage;
    private Main main;

    @FXML
    private TextField textCNP;
    @FXML
    private TextField textName;
    @FXML
    private TextField textAddress;
    @FXML
    private TextField textPhone;
    @FXML
    private TextField textUsername;

    public void setService(Service service, Stage stage){
        this.service = service;
        this.stage = stage;
    }

    public void handleRegister(){
        if (textCNP.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a CNP");
        }
        else if (textName.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a name");
        }
        else if (textAddress.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add an address");
        }
        else if (textPhone.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a phone number");
        }
        else if (textUsername.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a username");
        }
        else {
            try {
                String username = textUsername.getText();
                String password = service.generatePassword();
                String cnp = textCNP.getText();
                String name = textName.getText();
                String address = textAddress.getText();
                String phone = textPhone.getText();
                Subscriber subscriber = service.findSubscriberByUsername(username);
                if (subscriber == null) {
                    subscriber = new Subscriber(username, password, cnp, name, address, phone);
                    service.registerSubscriber(subscriber);
                }

                main.openSubscriberStage(subscriber);
                stage.hide();
            } catch (Exception e){
                e.printStackTrace();
                MessageAlert.showErrorMessage(null, "Error: " + e.getMessage());
            }
        }
    }

    public void setMain(Main main){
        this.main = main;
    }
}
