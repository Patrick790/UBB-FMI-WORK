#include <iostream>
#include <fstream>
#include <ranges>
#include <vector>
#include <chrono>
#include <stdexcept>


using namespace std;
using namespace std::chrono;
namespace fs = std::filesystem;

void writeNumber(const string& filename, vector<int> number, int N)
{
    ofstream file(filename);

    if (!file)
    {
        throw runtime_error("Problem in opening the file for writing!");
    }

    for (int i = N - 1; i >= 0; i--)
    {
        file << number[i];
    }

    file.close();
}

void readNumber(const string& filename, vector<int>& number, int& n)
{
    ifstream file(filename);

    if (!file)
    {
        throw runtime_error("Problem in opening the file for reading!");
    }

    file >> n;
    int digit;
    for (int i = 0; i < n; i++)
    {
        file >> digit;
        number.insert(number.begin(), digit);
    }

    file.close();
}

void initializeVectors(vector<int>& number1, vector<int>& number2, int& n)
{
    int n1, n2;
    readNumber("Numar1.txt", number1, n1);
    readNumber("Numar2.txt", number2, n2);

    if (n1 > n2)
    {
        n = n1;
        number2.resize(n, 0);
    }
    else
    {
        n = n2;
        number1.resize(n, 0);
    }
}

void add(const vector<int>& number1, const vector<int>& number2, vector<int>& result, int n)
{
    int carry = 0;
    for (int i = 0; i < n; i++)
    {
        int res = number1[i] + number2[i] + carry;
        result[i] = res % 10;
        carry = res / 10;
    }
    if (carry == 1)
        result.push_back(1);
}

int main(int argc, char** argv)
{
    int n;
    vector<int> number1, number2, result;

    auto startTime = high_resolution_clock::now();

    initializeVectors(number1, number2, n);
    result.resize(n + 1, 0);

    add(number1, number2, result, n);

    cout << "Result vector: ";
    for (int digit : result)
    {
        cout << digit;
    }
    cout << endl;

    writeNumber("Numar3.txt", result, n);

    ifstream file("Numar3.txt");
    if (file)
    {
        string fileContents((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
        cout << "File contents: " << fileContents << endl;
    }
    else
    {
        cerr << "Error: Could not open file Numar3.txt for reading." << endl;
    }

    auto endTime = high_resolution_clock::now();

    cout << duration<double, milli>(endTime - startTime).count() << "ms" << endl;

    return 0;
}