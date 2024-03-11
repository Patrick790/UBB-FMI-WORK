using System.Runtime.InteropServices.JavaScript;
using Lab12.domain;

namespace Lab12.repository;

public class DocumentFileRepo : FileRepository<String, Document>
{
    public DocumentFileRepo(string fileName) : base(fileName)
    {
        ReadFromFile(fileName);
    }

    protected override Document EntityFromString(string data)
    {
        string[] properties = data.Split(',');
        string id = properties[0];
        string nume = properties[1];
        DateTime dataEmitere;
        DateTime.TryParseExact(properties[2], "d/M/yyyy", null, System.Globalization.DateTimeStyles.None,
            out dataEmitere);
        return new Document(id, nume, dataEmitere);
    }
}