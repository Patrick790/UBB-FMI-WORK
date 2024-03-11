#include <QApplication>
#include "UI.h"

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    test_domain();
    //test_repo();
    //test_service();

    auto rp = FileRepo{ "melodii.txt"};

    auto srv = Service{rp};
    auto gui = GUI{srv};

    gui.show();
    return QApplication::exec();
}
