package com.example;

import com.example.Race;

import java.util.List;

public interface IRaceRepository extends Repository<Long, Race>{

    public List<Race> findByCapacity(int capacity);
}
