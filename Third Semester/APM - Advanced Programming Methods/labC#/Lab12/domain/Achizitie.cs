﻿namespace Lab12.domain;

public class Achizitie : Entity<string>
{
    public string Produs { get; set; }
    public int Cantitate { get; set; }
    public double PretProdus { get; set; }
    public string IdFactura { get; set; }

    public Achizitie(string id, string produs, int cantitate, double pretProdus, string idFactura)
    {
        base.Id = id;
        Produs = produs;
        Cantitate = cantitate;
        PretProdus = pretProdus;
        IdFactura = idFactura;
    }
}