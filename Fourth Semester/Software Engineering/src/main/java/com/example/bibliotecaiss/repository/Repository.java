package com.example.bibliotecaiss.repository;

import com.example.bibliotecaiss.domain.Entity;

import java.util.Optional;

public interface Repository <ID, E extends Entity<ID>>{
    Optional<E> findOne(ID id);

    Iterable<E> findAll();

    void save(E entity);

    Optional<E> delete(ID id);

    Optional<E> update(E entity);
}
