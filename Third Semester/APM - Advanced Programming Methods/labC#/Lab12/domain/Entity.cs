namespace Lab12.domain;

public class Entity<TID>
{
    public TID Id { get; set; }
    public Entity(){ }
    public Entity(TID id)
    {
        this.Id = id;
    }
    
}