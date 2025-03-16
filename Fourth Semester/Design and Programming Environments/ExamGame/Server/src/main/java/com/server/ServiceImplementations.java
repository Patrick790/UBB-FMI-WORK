package com.server;

import com.model.Game;
import com.model.Player;
import com.persistence.games.IGameRepository;
import com.persistence.players.IPlayerRepository;
import com.services.IObserver;
import com.services.IService;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class ServiceImplementations implements IService {
    private final IPlayerRepository playerRepository;
    private final IGameRepository gameRepository;
    private final Map<Integer, IObserver> loggedPlayers;
    private final Map<Integer, Game> games;



    public ServiceImplementations(IPlayerRepository playerRepository, IGameRepository gameRepository) {
        this.playerRepository = playerRepository;
        this.gameRepository = gameRepository;
        loggedPlayers = new ConcurrentHashMap<>();
        games = new HashMap<>();

    }


    @Override
    public Player login(Player player, IObserver client) throws Exception {
        Player playerToLogin = playerRepository.findByUsername(player.getUsername());
        if (playerToLogin == null) {
            throw new Exception("Authentication failed.");
        }
        if (loggedPlayers.get(playerToLogin.getId()) != null) {
            throw new Exception("Player already logged in.");
        }
        loggedPlayers.put(playerToLogin.getId(), client);


        var gr=this.generareCapcane();
        Game game = gameRepository.startGame(playerToLogin.getUsername(),
                LocalDate.now().format(DateTimeFormatter.ofPattern("dd/MM/yyyy")),
                LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss")));
        game.setCapcane(gr);
        System.out.println(gr+"GGRRRRRRRR");
        games.put(playerToLogin.getId(), game);
        gameRepository.updateGame(game);


        return playerToLogin;
    }

    public List<String> generareCapcane(){
        List<String> gr=new ArrayList<>();
        Random random=new Random();
        for (var i=1;i<=5;i++){
            var j=random.nextInt(5)+1;
            gr.add(j+" "+i+";");
        }
        int x= Integer.parseInt(String.valueOf(gr.get(0).charAt(0)));
        int y= Integer.parseInt(String.valueOf(gr.get(0).charAt(2)));
        String ultima=x+" "+y+";";
        while(gr.contains(ultima)){
            x= random.nextInt(5)+1;
            y= random.nextInt(5)+1;
            ultima=x+" "+y+";";
        }
        gr.add(ultima);
        return gr;
    }

    @Override
    public String choosePosition(int id, int x, int y) throws Exception {
        Game game = games.get(id);
        List<String> tries = game.getTries();
        tries.add(x + " " + y+";");
        game.setTries(tries);

        gameRepository.updateGame(game);
        games.put(id, game);

        if (tries.size() >= 5 && !game.getCapcane().contains( x + " " + y+";")) {
            // GATA JOCU CASTIG
            return "WIN";
        }
        if (game.getCapcane().contains(x + " " + y+";")) {
            // PIERDUT
            return "LOSS";
        }
        var pct=game.getPct();
        pct+=2 * y;
        game.setPct(pct);
        gameRepository.updateGame(game);
        return "NEXT";
    }

    @Override
    public Game getGameByUsername(String username) throws Exception {
        return null;
    }

    @Override
    public Collection<Game> getScores() throws Exception {
        return gameRepository.getAll();
    }

    @Override
    public Game getFinishedGameInfo(Integer id) throws Exception {
        Game game = games.get(id);
        games.remove(id);
        Collection<Game> gamesList = gameRepository.getAll();
        for (Game game1 : games.values()) {
            gamesList.removeIf(game2 -> Objects.equals(game1.getId(), game2.getId()));
        }

        for (IObserver loggedPlayer : loggedPlayers.values()) {
            try {
                loggedPlayer.gameFinished(gamesList);
            } catch (Exception e) {
                System.out.println("Error notifying player " + e.getMessage());
            }
        }

        loggedPlayers.remove(id);

        return game;
    }


}
