using Lab12.domain;

namespace Lab12.repository;

public class AchizitieFileRepo : FileRepository<string, Achizitie>
{
    private string fileFacturi;
    public AchizitieFileRepo(string fileName, string fileFacturi) : base(fileName)
    {
        ReadFromFile(fileName);
        this.fileFacturi = fileFacturi;
    }

    protected override Achizitie EntityFromString(string data)
    {
        string[] properties = data.Split(',');
        string id = properties[0];

        return new Achizitie(
            id,
            properties[1],
            int.Parse(properties[2]),
            double.Parse(properties[3]),
            properties[4]
        );

    }
}