using Lab12.domain;

namespace Lab12.repository;

public interface IRepository <TId, TE> where TE : Entity<TId>
{
    IEnumerable<TE> FindAll();
}