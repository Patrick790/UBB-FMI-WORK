package com.client.gui;

import com.example.Participant;
import com.services.IMotorcyclesServices;
import com.services.MotorcyclesException;
import javafx.beans.property.ReadOnlyObjectWrapper;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.Stage;

import java.util.List;

public class ParticipantsController {

    @FXML
    private TableView<Participant> participantsTableView;

    IMotorcyclesServices service;

    private String teamName;

    private Stage stage;

    @FXML
    private TableColumn<Participant, String> nameColumn;

    @FXML
    private TableColumn<Participant, String> capacityColumn;

    private final ObservableList<Participant> modelParticipants = FXCollections.observableArrayList();

    public void setService(IMotorcyclesServices service, Stage stage, String teamName) throws MotorcyclesException {
        this.service = service;
        this.stage = stage;
        this.teamName = teamName;

        initialize();
        initModel();
    }

    private void initModel() throws MotorcyclesException {
        List<Participant> participants = service.findByTeam(teamName);
        participantsTableView.getItems().clear();
        for (Participant participant : participants) {
            participantsTableView.getItems().add(participant);
        }
    }

    private void initialize(){
        participantsTableView.setItems(modelParticipants);
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));
        capacityColumn.setCellValueFactory(cellData -> {
            try {
                return new ReadOnlyObjectWrapper<>(service.getCapacityForParticipant(cellData.getValue())).asString();
            } catch (MotorcyclesException e) {
                throw new RuntimeException(e);
            }
        });
    }



}
