package com.hibernate.user;

import org.hibernate.Session;
import org.hibernate.Transaction;

import java.util.List;
import java.util.Optional;

public class UserHibernateRepository implements UserRepository{
    @Override
    public Optional<User> findOne(Integer id) {
        try(Session session = HibernateUtils.getSessionFactory().openSession()){
            Transaction transaction = null;
            try{
                transaction = session.beginTransaction();
                User user = session.createQuery("from User where id = :id", User.class)
                        .setParameter("id", id)
                        .uniqueResult();
                transaction.commit();
                return Optional.ofNullable(user);
            }catch (RuntimeException ex){
                if(transaction != null)
                    transaction.rollback();
            }
        }
        return Optional.empty();
    }

    @Override
    public Iterable<User> findAll() {
        try(Session session = HibernateUtils.getSessionFactory().openSession()){
            Transaction transaction = null;
            try{
                transaction = session.beginTransaction();
                List<User> users = session.createQuery("from User", User.class)
                        .list();
                transaction.commit();
                return users;
            }catch (RuntimeException ex){
                if(transaction != null)
                    transaction.rollback();
            }
        }
        return null;
    }

    @Override
    public void save(User user) {
        HibernateUtils.getSessionFactory().inTransaction(session -> session.persist(user));

    }

    @Override
    public Optional<User> delete(Integer integer) {
        return Optional.empty();
    }

    @Override
    public Optional<User> update(User entity) {
        return Optional.empty();
    }
}
