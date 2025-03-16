package com.rest;

import com.model.Game;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;

public class Client {
    private static final String URL = "http://localhost:8080/joc_gropi/tries/1";

    public Game add(int id, Game game) {
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.set("Content-Type", "application/json");
        HttpEntity<Game> request = new HttpEntity<>(game, headers);
        ResponseEntity<Game> response = restTemplate.exchange(URL + id, HttpMethod.PUT, request, Game.class);
        return response.getBody();
    }

    public static void main(String[] args) {
        Client client = new Client();
        Game game = new Game();
        game.setId(1);
        game.setPlayer("player2");
        game.setDate("2023-12-31");
        game.setTime("12:00:00");
        game.setPct(100);
        game.setTries(Arrays.asList("1 1", "1 2", "1 3", "1 4", "1 5"));
        game.setCapcane(Arrays.asList("2 5", "2 3", "2 4"));
        Game responseGame = client.add(game.getId(), game);
        System.out.println(responseGame);
    }
}