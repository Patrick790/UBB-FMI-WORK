package com.model;

import java.io.Serializable;
import java.util.List;

import static org.hibernate.boot.model.source.internal.hbm.CommaSeparatedStringHelper.split;

public class DTORest implements Serializable {
    private List<String> tries;
    private List<String> capcane;
    private Integer points;
    private String time;
    private String player;
    private int id;



    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public DTORest(Integer id, List<String> tries, List<String> capcane, Integer points, String time, String player) {
        this.id=id;
        this.tries = tries;
        this.capcane = capcane;
        this.points = points;
        this.time = time;
        this.player = player;
    }

    public DTORest() {
    }

    public List<String> getTries() {
        return tries;
    }

    public void setTries(List<String> tries) {
        this.tries = tries;
    }

    public List<String> getCapcane() {
        return capcane;
    }

    public void setCapcane(List<String> capcane) {
        this.capcane = capcane;
    }

    public Integer getPoints() {
        return points;
    }

    public void setPoints(Integer points) {
        this.points = points;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }


}
