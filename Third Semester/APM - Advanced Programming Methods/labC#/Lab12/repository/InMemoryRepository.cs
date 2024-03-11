using Lab12.domain;

namespace Lab12.repository;

public class InMemoryRepository<Id, E> : IRepository<Id, E> where E : Entity<Id>
{
    protected IDictionary<Id, E> entities;

    public InMemoryRepository()
    {
        entities = new Dictionary<Id, E>();
    }

    public IEnumerable<E> FindAll()
    {
        return entities.Values.ToList<E>();
    }

    public E FindOne(Id id)
    {
        return entities[id];
    }

    public E Save(E entity)
    {
        if (entity == null)
            throw new ArgumentNullException("Entity must not be null!");
        entities[entity.Id] = entity;
        return entity;
    }

    public E Delete(Id id)
    {
        if (id == null)
            throw new ArgumentException("Cannot delete null element");
        if (!entities.ContainsKey(id))
            throw new Exception($"Entity with {id} not found");
        E toBeDeleted = entities[id];
        entities.Remove(id);
        return toBeDeleted;
    }


    public E Update(E entity)
    {
        if (entity == null)
            throw new ArgumentException("Cannot update null");
        if (!entities.ContainsKey(entity.Id))
            return default;
        entities[entity.Id] = entity;
        return entity;
    }
    
    
}