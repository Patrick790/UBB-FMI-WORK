package com.example.bibliotecaiss.repository;

import com.example.bibliotecaiss.domain.Book;

import java.util.Optional;

public interface IBookRepository extends Repository<Long, Book>{
    Optional<Book> findByTitle(String title);
}
