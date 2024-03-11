using Lab12.domain;
using Lab12.repository;
using Lab12.service;
using Lab12.ui;

public class Program
{
    static void Main()
    {
        DocumentFileRepo documentFileRepo = new DocumentFileRepo("..\\..\\..\\data\\documente.txt");
        AchizitieFileRepo achizitieFileRepo = new AchizitieFileRepo("..\\..\\..\\data\\achizitii.txt", "..\\..\\..\\data\\documente.txt");
        FacturaFileRepository facturaFileRepository =
            new FacturaFileRepository("..\\..\\..\\data\\facturi.txt", documentFileRepo, achizitieFileRepo);

        Service service = new Service(achizitieFileRepo, facturaFileRepository, documentFileRepo);

        Ui console = new Ui(service);
        console.Run();
    }
}