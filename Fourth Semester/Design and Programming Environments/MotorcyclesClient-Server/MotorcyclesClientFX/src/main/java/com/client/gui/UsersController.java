package com.client.gui;

import com.client.StartRpcClientFX;
import com.example.Race;
import com.example.User;
import com.example.Participant;
import com.example.Registration;
import com.services.IMotorcyclesServices;
import com.services.MotorcyclesException;
import com.services.Observable;
import com.services.Observer;
import javafx.beans.property.ReadOnlyObjectWrapper;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Modality;
import javafx.stage.Stage;


import java.sql.SQLException;
import java.util.Optional;
import java.util.Random;

public class UsersController implements Observer {

    public Label teamLabel;
    private Stage stage;
    private IMotorcyclesServices service;

    private StartRpcClientFX startRpcClientFX;



    private User user;

    @FXML
    TableView<Race>  racesTableView;

    @FXML
    TableColumn<Race, Long> raceId;

    @FXML
    TableColumn<Race, Integer> capacity;

    @FXML
    TableColumn<Race, Integer> participantsNo;

    @FXML
    private TextField teamNameField;

    @FXML
    private Button searchButton;

    @FXML
    private Button addParticipantButton;

    @FXML
    private TextField pNameTextBox;

    @FXML
    private TextField pTeamTextBox;

    @FXML Button registerButton;

    @FXML
    private Button logoutButton;

    @FXML
    private TextField rCapacityTextBox;

    @FXML
    private Button addRaceButton;

    @FXML
    private Button addUserButton;

    @FXML
    private TextField usernameTextBox;

    @FXML
    private TextField nameTextBox;

    @FXML
    private TextField passwordTextBox;

    private final ObservableList<Race> raceModel = FXCollections.observableArrayList();


    public void setService(User user, IMotorcyclesServices service, Stage stage, StartRpcClientFX startRpcClientFX) throws MotorcyclesException {
        this.user = user;
        this.service = service;
        this.stage = stage;
        this.startRpcClientFX = startRpcClientFX;
        service.registerObserver(this);
        initModelRaces();

        initializeRaces();
    }

    private void initModelRaces() throws MotorcyclesException {
        Iterable<Race> races = service.getAllRaces();
        racesTableView.getItems().clear();
        for (Race race : races) {
            racesTableView.getItems().add(race);
        }
    }

    private void initializeRaces() throws MotorcyclesException {
        racesTableView.setItems(raceModel);
        raceId.setCellValueFactory(new PropertyValueFactory<>("id"));
        capacity.setCellValueFactory(new PropertyValueFactory<>("capacity"));
        participantsNo.setCellValueFactory(cellData -> {
            try {
                return new ReadOnlyObjectWrapper<>(service.countRegistrationsForRace(cellData.getValue()));
            } catch (MotorcyclesException | SQLException e) {
                throw new RuntimeException(e);
            }
        });
        initModelRaces();
    }

    public void onPressSearch(ActionEvent actionEvent) throws Exception{
        try{
            FXMLLoader participantsLoader = new FXMLLoader(getClass().getResource("/participants-view.fxml"));

            AnchorPane friendsRoot = participantsLoader.load();

            Stage participantsStage = new Stage();
            participantsStage.setTitle("Participants");
            participantsStage.initModality(Modality.WINDOW_MODAL);
            participantsStage.setResizable(true);
            Scene scene = new Scene(friendsRoot, 600, 300);
            participantsStage.setScene(scene);

            ParticipantsController participantsController = participantsLoader.getController();
            String teamName = teamNameField.getText();
            participantsController.setService(service, participantsStage, teamName);

            participantsStage.show();
        } catch (Exception e){
            throw new Exception(e);
        }
    }

    public void onPressAddRace(ActionEvent actionEvent) throws SQLException, MotorcyclesException {
        int capacity = Integer.parseInt(rCapacityTextBox.getText());
        Race race = new Race(capacity);
        Long id = new Random().nextLong();
        race.setId(id);
        service.addRace(race);
        initModelRaces();
        MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Race", "Race successfully added!");
    }


    public void onPressRegister(ActionEvent actionEvent) throws SQLException, MotorcyclesException {
        String name = pNameTextBox.getText();
        String team = pTeamTextBox.getText();

        Optional<Participant> existingParticipant = service.findParticipantByNameAndTeam(name, team);

        if (existingParticipant.isEmpty()) {
            Participant participant = new Participant(name, team);
            Long id = service.getNextParticipantId(); // Get the next ID from the Participant table
            participant.setId(id);
            service.addParticipant(participant);
            existingParticipant = Optional.of(participant);
        }

        // Move the registration creation outside the if block
        registerParticipantForRace(existingParticipant.get());
        initModelRaces();
    }

    public void handleLogout(ActionEvent actionEvent) throws Exception {
        Stage stage = (Stage) logoutButton.getScene().getWindow();
        stage.close();

        startRpcClientFX.loginStage(new Stage());

    }

    private void registerParticipantForRace(Participant participant) throws SQLException, MotorcyclesException {
        Race selectedRace = racesTableView.getSelectionModel().getSelectedItem();

        if (selectedRace != null) {
            // Check if the participant is already registered for the race
            if (!service.isParticipantRegisteredForRace(participant, selectedRace)) {
                Registration registration = new Registration(participant, selectedRace);
                Long registrationId = new Random().nextLong();
                registration.setId(registrationId);
                service.addRegistration(registration);
                initModelRaces();
                MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Registration", "Participant registered successfully!");
            } else {
                MessageAlert.showErrorMessage(null, "Participant is already registered for this race!");
            }
        } else {
            MessageAlert.showErrorMessage(null, "Please select a race!");
        }
    }

    public void onPressAddUser(ActionEvent actionEvent) throws MotorcyclesException {
        String username = usernameTextBox.getText();
        String name = nameTextBox.getText();
        String password = passwordTextBox.getText();
        String hashedPassword = service.hashPassword(password);

        User user = new User(username, name, hashedPassword);

        Long id = new Random().nextLong();
        user.setId(id);
        service.addUser(user);
        pNameTextBox.clear();
        pTeamTextBox.clear();
    }

    @Override
    public void update() throws SQLException, MotorcyclesException {
        initModelRaces();
    }
}
