using Lab12.domain;
using Lab12.service;

namespace Lab12.ui;

public class Ui
{
    private service.Service _service;

    public Ui(service.Service service)
    {
        this._service = service;
    }

    public void Run()
    {
        while (true)
        {
            Console.WriteLine("\nMeniu:");
            Console.WriteLine("0. Exit");
            Console.WriteLine("1. Afisare documente din 2023");
            Console.WriteLine("2. Facturile scadente in luna curenta");
            Console.WriteLine("3. Facturi cu cel putin 3 produse");
            Console.WriteLine("4. Achizitiile din categoria Utilities");
            Console.WriteLine("5. Categoria de facturi cu cele mai multe cheltuieli");
            Console.WriteLine("\n");
            
            Console.WriteLine("Introduceti optiune: ");
            try
            {
                int cmd = int.Parse(Console.ReadLine());
                switch (cmd)
                {
                    case 0:
                        return;
                    case 1:
                        foreach (Document document in _service.DocumentsByYear())
                        {
                            Console.WriteLine(document.Nume + " - " + document.DataEmitere);
                        }

                        break;
                    case 2:
                        foreach (Factura factura in _service.FacturiScadente())
                        {
                            Console.WriteLine(factura.Nume + " - " + factura.DataScadenta);
                        }

                        break;
                    case 3:
                        foreach (Factura factura in _service.FacturiProduseAchizitionate())
                        {
                            Console.WriteLine(factura.Nume + " - " + _service.Cantitate(factura.Achizitii));
                        }

                        break;
                    case 4:
                        foreach (var achizitie in _service.AchizitiiDupaCategorii())
                        {
                            Console.WriteLine(achizitie.Item1.Produs + " " + achizitie.Item2);
                        }

                        break;
                    case 5:
                        Console.WriteLine(_service.CeleMaiMulteCheltuieli());
                        break;
                    default:
                        Console.WriteLine("Comanda invalida.");
                        break;
                }
            }
            catch (FormatException)
            {
                Console.WriteLine("Comanda invalida. Reincercati.");
            }
        }
    }
}