using System.Runtime.InteropServices.JavaScript;
using Lab12.domain;

namespace Lab12.repository;

public class FacturaFileRepository : FileRepository<string, Factura>
{
    private DocumentFileRepo documentRepo;
    private AchizitieFileRepo achizitieRepo;

    public FacturaFileRepository(string fileName, DocumentFileRepo documentRepo, AchizitieFileRepo achizitieRepo) :
        base(fileName)
    {
        this.documentRepo = documentRepo;
        this.achizitieRepo = achizitieRepo;
        ReadFromFile(fileName);
    }

    protected override Factura EntityFromString(string data)
    {
        string[] properties = data.Split(',');
        string id = properties[0];

        Document document = documentRepo.FindOne(id);

        DateTime dataScadenta;
        Categorie categorie = (Categorie)Enum.Parse(typeof(Categorie), properties[2]);
        DateTime.TryParseExact(properties[1], "d/M/yyyy", null,
            System.Globalization.DateTimeStyles.None, out dataScadenta);
        return new Factura(id, document.Nume, document.DataEmitere, dataScadenta, categorie);
    }
}