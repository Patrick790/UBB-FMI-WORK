package com.services;

import com.model.Game;

import java.util.Collection;

public interface IObserver {
    void gameFinished(Collection<Game> games) throws Exception;
}
