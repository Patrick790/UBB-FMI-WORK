using System.Runtime.InteropServices.JavaScript;

namespace Lab12.domain;

public enum Categorie
{
    Utilities, Groceries, Fashion, Entertainment, Electronics
}

public class Factura : Document
{
    public DateTime DataScadenta { get; set; }
    public List<Achizitie> Achizitii { get; set; }
    public Categorie Categorie { get; set; }
    
    public Factura() { }

    public Factura(string id, string nume, DateTime dataEmitere, DateTime dataScadenta, Categorie categorie)
        : base(id, nume, dataEmitere)
    {
        this.DataScadenta = dataScadenta;
        this.Categorie = categorie;
        this.Achizitii = new List<Achizitie>();
    }
}