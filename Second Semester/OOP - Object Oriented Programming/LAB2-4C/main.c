
#include "OfertaRepository.h"
#include "UI.h"
#include "Oferta.h"
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>

int main()
{
    //Functia principala main

    testsrepo();
    testsService();
    testsOferta();
    testsVector();

    OfertaRepo* repo = createRepo();
    Service* serv = createService(repo);

    UI* ui = createUI(serv);
    Vector* undoList = createVector(2, (DestroyElementFunctionType) destroyRepo);


    addOferta(serv, "munte", "Fagaras", "20/10/2023", 200);
    addOferta(serv, "mare", "Marea Neagra", "10/10/2024", 600);
    addOferta(serv, "munte", "Brasov", "22/3/2023", 400);
    addOferta(serv, "mare", "Delta", "4/4/2023", 700);
    addOferta(serv, "munte", "Sinaia", "5/4/2023", 800);
    addOferta(serv, "munte", "Sinaia", "5/9/2024", 600);
    startUI(ui, undoList);

    destroyVector(undoList);
    destroyUI(ui);
    return 0;
}