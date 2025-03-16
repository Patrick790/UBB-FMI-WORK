package com.model;



import javax.persistence.*;
import java.io.Serializable;
import java.util.List;

@javax.persistence.Entity
@Table(name = "games")
public class Game implements Entity<Integer>, Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    int id;

    @Column(name = "player")
    String player;

    @Column(name = "date")
    String date;

    @Column(name = "time")
    String time;

    @Column(name = "pct")
    Integer pct;

    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(name = "tries", joinColumns = @JoinColumn(name = "id"))
    @Column(name = "tries")
    private List<String> tries;

    @ElementCollection(fetch = FetchType.LAZY)
    @CollectionTable(name = "capcane", joinColumns = @JoinColumn(name = "id"))
    @Column(name = "capcane")
    private List<String> capcane;

    public Game() {
        this.id = 0;
        this.player = "";
        this.date = "";
        this.time = "";
        this.tries = null;
        this.capcane = null;
        this.pct = 0;
    }

    public Game(int id, String player, String date, String time, List<String> tries, List<String> capcane) {
        this.id = id;
        this.player = player;
        this.date = date;
        this.time = time;
        this.tries = tries;
        this.capcane = capcane;
        this.pct = 0;
    }

    public Game( String player, String date, String time, List<String> tries, List<String> capcane) {
        this.id = 0;
        this.player = player;
        this.date = date;
        this.time = time;
        this.tries = tries;
        this.capcane = capcane;
        this.pct = 0;
    }

    public Game(String player, String date, String time, List<String> capcane) {
        this.id=0;
        this.player = player;
        this.date = date;
        this.time = time;
        this.tries=null;
        this.capcane = capcane;
        this.pct = 0;
    }

    public Game(int id, String player, String date, String time, List<String> capcane) {
        this.id = id;
        this.player = player;
        this.date = date;
        this.time = time;
        this.tries=null;
        this.capcane = capcane;
        this.pct = 0;
    }

    public Game(String player, String date, String time) {
        this.id = 0;
        this.player = player;
        this.date = date;
        this.time = time;
        this.tries=null;
        this.capcane = null;
        this.pct = 0;
    }

    public Integer getPct() {
        return pct;
    }

    public void setPct(Integer pct) {
        this.pct = pct;
    }

    @Override
    public Integer getId() {
        return id;
    }

    @Override
    public void setId(Integer id) {
        this.id=id;
    }

    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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

    @Override
    public String toString() {
        return "Game{" +
                "id=" + id +
                ", player='" + player + '\'' +
                ", date='" + date + '\'' +
                ", time='" + time + '\'' +
                ", pct=" + pct +
//                ", tries=" + tries +
//                ", gropi=" + gropi +
                '}';
    }

    public boolean hasReachedColumn5() {
        for (String trie : tries) {
            String[] parts = trie.split(" ");
            int column = Integer.parseInt(parts[1]);
            if (column == 5) {
                return true;
            }
        }
        return false;
    }

}

