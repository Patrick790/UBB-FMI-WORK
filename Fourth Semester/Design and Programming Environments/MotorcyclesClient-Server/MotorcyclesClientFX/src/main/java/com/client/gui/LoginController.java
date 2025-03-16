package com.client.gui;

import com.client.StartRpcClientFX;
import com.example.User;
import com.services.IMotorcyclesServices;
import com.services.MotorcyclesException;
import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LoginController {
    private IMotorcyclesServices service;

    UsersController usersController;
    private Stage stage;

    private static final Logger logger= LogManager.getLogger();

    private StartRpcClientFX startRpcClientFX;



    @FXML
    private TextField textUsername;
    @FXML
    private TextField textPassword;


    public void setService(IMotorcyclesServices service, Stage stage){
        this.service = service;
        this.stage = stage;
    }

    public void handleLogin() throws MotorcyclesException {
        logger.traceEntry();
        if(textUsername.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a username");
        } else if(textPassword.getText().isEmpty()){
            MessageAlert.showErrorMessage(null, "Add a password");
        } else {
            if(service.login(textUsername.getText(), textPassword.getText(), usersController)) {
                try {
                    User user = service.findAfterUsername(textUsername.getText());
                    startRpcClientFX.openUserStage(user);
                    stage.hide();
                } catch (Exception e){
                    MessageAlert.showErrorMessage(null, "Error: " + e.getMessage());
                }
            } else {
                MessageAlert.showErrorMessage(null, "Incorrect login data");
            }
        }
        logger.traceExit();
    }

    public void setStartRpcClientFX(StartRpcClientFX startRpcClientFX){
        this.startRpcClientFX = startRpcClientFX;
    }
}
