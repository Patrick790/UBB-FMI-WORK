package com.client.controllers;

import com.model.Game;
import com.model.Player;
import com.services.IObserver;
import com.services.IService;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import javafx.util.Callback;

import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Collection;
import java.util.Comparator;
import java.util.Objects;

public class MainController implements IObserver {
    public Label indiciu11;
    public Label indiciu21;
    public Label indiciu31;
    public Label indiciu41;
    public Label indiciu51;
    public Label indiciu12;
    public Label indiciu22;
    public Label indiciu32;
    public Label indiciu42;
    public Label indiciu52;
    public Label indiciu13;
    public Label indiciu23;
    public Label indiciu33;
    public Label indiciu43;
    public Label indiciu53;
    public Label indiciu14;
    public Label indiciu24;
    public Label indiciu34;
    public Label indiciu44;
    public Label indiciu54;
    public Label indiciu15;
    public Label indiciu25;
    public Label indiciu35;
    public Label indiciu45;
    public Label indiciu55;

    public TableView scoresTable;
    public TableColumn usernameColumn;
    public TableColumn timeColumn;
    public Label numberOfTries;
    public Label gropiLbl;
    public TableColumn pointsColumn;

    private IService service;

    private Player loggedInPlayer;
    private boolean gameFinished=false;
    private final ObservableList<Game> scores = FXCollections.observableArrayList();


    public void setService(IService service) {
        this.service=service;
    }

    public void setLoggedInPlayer(Player player) {
        this.loggedInPlayer=player;
    }

    public void initialise() {
        usernameColumn.setCellValueFactory(new PropertyValueFactory<>("player"));

        timeColumn.setCellValueFactory(new Callback<TableColumn.CellDataFeatures<Game, String>, ObservableValue<String>>() {
            @Override
            public ObservableValue<String> call(TableColumn.CellDataFeatures<Game, String> data) {
                Game game = data.getValue();
                LocalTime startTime = LocalTime.parse(game.getTime(), DateTimeFormatter.ofPattern("HH:mm:ss"));
                LocalTime endTime = LocalTime.now();
                Duration duration = Duration.between(startTime, endTime);
                long durationInSeconds = duration.getSeconds();
                String durationString = String.valueOf(durationInSeconds);
                return new SimpleStringProperty(durationString);
            }
        });
        pointsColumn.setCellValueFactory(new PropertyValueFactory<>("pct"));

        try{
            var a=service.getScores();
            System.out.println(a);
            scores.setAll(a);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        scoresTable.setItems(scores.sorted(Comparator.comparingInt(Game::getPct).reversed()));
    }
    private String clickAction(int x, int y) {
        try {
            return service.choosePosition(loggedInPlayer.getId(), x, y);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private boolean isGameFinished(String output) {
        return !Objects.equals(output, "NEXT");
    }

    private void finishGame() {
        Game finishedGame;
        try {
            finishedGame = service.getFinishedGameInfo(loggedInPlayer.getId());
        } catch (Exception e) {
            Alert alert = new Alert(Alert.AlertType.ERROR, e.getMessage(), ButtonType.OK);
            alert.show();
            return;
        }
        numberOfTries.setText("PCT: " + finishedGame.getPct());
        gropiLbl.setText("CAPCANE: "+String.join("",finishedGame.getCapcane()));
    }
    public void indiciu11Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(1, 1);
        indiciu11.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu21Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(2, 1);
        indiciu21.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu31Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(3, 1);
        indiciu31.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu41Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(4, 1);
        indiciu41.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu51Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(5, 1);
        indiciu41.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu12Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(1, 2);
        indiciu12.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu22Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(2, 2);
        indiciu22.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu32Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(3, 2);
        indiciu32.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu42Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(4, 2);
        indiciu42.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu52Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(5, 2);
        indiciu41.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu13Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(1, 3);
        indiciu13.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu23Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(2, 3);
        indiciu23.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu33Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(3, 3);
        indiciu33.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu43Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(4, 3);
        indiciu43.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }
    public void indiciu53Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(5, 3);
        indiciu43.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu14Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(1, 4);
        indiciu14.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu24Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(2, 4);
        indiciu24.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu34Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(3, 4);
        indiciu34.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu44Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(4, 4);
        indiciu44.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }
    public void indiciu54Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(5, 4);
        indiciu44.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu15Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(1, 5);
        indiciu14.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu25Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(2, 5);
        indiciu24.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu35Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(3, 5);
        indiciu34.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }

    public void indiciu45Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(4, 5);
        indiciu44.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }
    public void indiciu55Click(MouseEvent mouseEvent) {
        if (gameFinished) {
            return;
        }
        String output = clickAction(5, 5);
        indiciu44.setText(output);
        if (isGameFinished(output)) {
            gameFinished = true;
            finishGame();
        }
    }



    @Override
    public void gameFinished(Collection<Game> games) throws Exception {
//        Platform.runLater(()->{
//            try{
//                scores.setAll(games);
//                scoresTable.setItems(scores.sorted(Comparator.comparingInt(Game::getPct)));
//            }catch(Exception e){
//                throw new RuntimeException(e);
//            }
//            });
        scores.setAll(games);
        scoresTable.setItems(scores.sorted(Comparator.comparingInt(Game::getPct).reversed()));

    }
}
