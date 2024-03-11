using Lab12.domain;

namespace Lab12.repository;

public abstract class FileRepository<Id, E> : InMemoryRepository<Id, E> where E : Entity<Id>
{
    
    public FileRepository(string fileName)
    {
        
    }

    public void ReadFromFile(string fileName)
    {
        try
        {
            StreamReader streamReader = new StreamReader(fileName);
            string data;
            while (true)
            {
                data = streamReader.ReadLine();
                if (data == null)
                    break;

                Save(EntityFromString(data));
            }
        }
        catch (IOException ex)
        {
            Console.WriteLine($"Error reading from file: {ex.Message}");
        }
    }

    protected abstract E EntityFromString(string data);
}
