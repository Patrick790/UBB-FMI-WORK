using Lab12.domain;
using Lab12.repository;
using System.Collections.Generic;
using System.Linq;

namespace Lab12.service;

public class Service
{
    private readonly IRepository<string, Achizitie> achizitieRepo;
    private readonly IRepository<string, Factura> facturaRepo;
    private readonly IRepository<string, Document> documentRepo;

    public Service(IRepository<string, Achizitie> achizitieRepo, IRepository<string, Factura> facturaRepo,
        IRepository<string, Document> documentRepo)
    {
        this.achizitieRepo = achizitieRepo;
        this.facturaRepo = facturaRepo;
        this.documentRepo = documentRepo;

        foreach (var achizitie in this.achizitieRepo.FindAll())
        {
            Factura f = facturaRepo.FindAll().FirstOrDefault(factura => factura.Id == achizitie.IdFactura);
            f?.Achizitii.Add(achizitie);
        }
        
    }



    public IEnumerable<Document> DocumentsByYear()
    {
        return documentRepo.FindAll().Where(d => d.DataEmitere.Year == 2023);
    }

    public IEnumerable<Factura> FacturiScadente()
    {
        return facturaRepo.FindAll().Where(f => f.DataScadenta.Month == DateTime.Now.Month);
    }

    public IEnumerable<Factura> FacturiProduseAchizitionate()
    {
        return facturaRepo.FindAll().Where(f => Cantitate(f.Achizitii) >= 3);
    }

    public IEnumerable<(Achizitie, string)> AchizitiiDupaCategorii()
    {
        Categorie categorie = Categorie.Utilities;
        return from factura in facturaRepo.FindAll()
            where factura.Categorie == categorie
            from Achizitie in achizitieRepo.FindAll()
            where Achizitie.IdFactura == factura.Id
            select (Achizitie, factura.Nume);
    }

    public Categorie CeleMaiMulteCheltuieli()
    {
        var count = facturaRepo.FindAll()
            .SelectMany(factura => factura.Achizitii,
                (factura, achizitie) => new { factura.Categorie, TotalCost = achizitie.Cantitate * achizitie.PretProdus })
            .GroupBy(item => item.Categorie)
            .ToDictionary(group => group.Key, group => group.Sum(item => item.TotalCost));

        Categorie categorie = count.OrderByDescending(kv => kv.Value).FirstOrDefault().Key;
        return categorie;
    }


    public int Cantitate(List<Achizitie> achizitii)
    {
        int c = 0;
        foreach (Achizitie achizitie in achizitii)
        {
            c += achizitie.Cantitate;
        }
        return c;
    }
}