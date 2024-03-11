
#include "validator.h"
#include "Repo.h"
#include "Service.h"
#include "UI.h"



void testAll(){
    testDomain();
    testRepo();
    testService();
    testValidator();
}

void startApp(){
    CarRepo repo;
    carValidator val;
    carService srv{repo, val};
    consoleUi ui{srv };

    ui.run();

}
int main() {
    testAll();
    startApp();
    return 0;

}
