package com.rest;

import com.model.DTORest;
import com.model.Game;
import com.persistence.games.GameRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/joc_gropi")
public class Controller {
    @Autowired
    private GameRepository gameRepository;


    @RequestMapping("/greeting")
    public String greeting() {
        return "Hello, World!";
    }

    @RequestMapping(method = RequestMethod.GET)
    public Collection<Game> getAll() {
        return gameRepository.getAll();
    }

    @RequestMapping(value = "/games/{username}", method = RequestMethod.GET)    // http://localhost:8080/test/games/ion
    public Collection<DTORest> getByUsername(@PathVariable String username) {
        Collection<Game> games=gameRepository.getByUsername(username);
        List<DTORest> gameDTOs = new ArrayList<>();
        for (Game game : games) {
            DTORest gameDTO = new DTORest();
            gameDTO.setId(game.getId());
            gameDTO.setPlayer(game.getPlayer());
            gameDTO.setTries(game.getTries());
            gameDTO.setTime(game.getTime());
            gameDTO.setPoints(game.getPct());

            gameDTOs.add(gameDTO);
        }
        return gameDTOs;
    }
    @RequestMapping(value = "/tries/{id}",method = RequestMethod.PUT)
    public Game add(@PathVariable int id, @RequestBody Game game) {
        if(game.getId()==id) {
            gameRepository.updateGame(game);
        }
        return game;
    }
}
