package com.services.rest;

import com.example.IRaceRepository;
import com.example.Race;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@CrossOrigin(origins = "http://localhost:3000")
@RestController
@RequestMapping("temarest/races")
public class RaceController {

    @Autowired
    private IRaceRepository raceRepository;

    @PostMapping
    public ResponseEntity<Race> create(@RequestBody Race race) {
        raceRepository.save(race);
        return new ResponseEntity<>(race, HttpStatus.CREATED);
    }

    @GetMapping
    public ResponseEntity<List<Race>> getAllRaces() {
        return new ResponseEntity<>((List<Race>) raceRepository.findAll(), HttpStatus.OK);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Race> getRaceById(@PathVariable Long id) {
        Optional<Race> race = raceRepository.findOne(id);
        return race.map(value -> new ResponseEntity<>(value, HttpStatus.OK))
                .orElseGet(() -> new ResponseEntity<>(HttpStatus.NOT_FOUND));
    }


    @PutMapping("/{id}")
    public ResponseEntity<Race> updateRace(@PathVariable Long id, @RequestBody Race race) {
        Optional<Race> existingRace = raceRepository.findOne(id);
        if (existingRace.isPresent()) {
            race.setId(id);
            raceRepository.update(race);
            return new ResponseEntity<>(race, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteRace(@PathVariable Long id) {
        Optional<Race> existingRace = raceRepository.findOne(id);
        if (existingRace.isPresent()) {
            raceRepository.delete(id);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        } else {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
    }
}
