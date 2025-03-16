package com.persistence.players;

import com.model.Player;

public interface IPlayerRepository {
    Player findByUsername(String username);
}
