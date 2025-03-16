package com.services;

import com.model.Game;
import com.model.Player;

import java.util.Collection;

public interface IService {
    Player login(Player player, IObserver client) throws Exception;
    String choosePosition(int id, int x, int y) throws Exception;

    Game getGameByUsername(String username)throws Exception;

    Collection<Game> getScores() throws Exception;
    Game getFinishedGameInfo(Integer id) throws Exception;
}
