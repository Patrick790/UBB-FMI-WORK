#pragma once
#include <string>
#include "Car.h"
#include <vector>

using std::vector;
using std::string;
using std::ostream;

class validateException {
    vector<string> errorMsg;
public:
    validateException(vector<string> errorMessages) : errorMsg{errorMessages } {};

    string getErrorMessages() {
        string fullMsg;
        for (const string e : errorMsg) {
            fullMsg += e + "\n";
        }
        return fullMsg;
    }
};

class carValidator {
public:
    static void validate(const Car& c);
};

void testValidator();