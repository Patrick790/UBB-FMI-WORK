package com.hibernate.user;

import java.util.Optional;

public interface ICrudRepository<ID, E extends Entity<ID>> {
    Optional<E> findOne(ID id);

    Iterable<E> findAll();

    void save(E entity);

    Optional<E> delete(ID id);

    Optional<E> update(E entity);

}
