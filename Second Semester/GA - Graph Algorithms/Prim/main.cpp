#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("graf.txt");
ofstream fout("grafout");
const int inf = 0x3FFFFFFF;
int a[101][101], viz[101], c[101], t[101];

void Prim()
{
    int n, m;
    fin >> n >> m; // Citirea numărului de noduri și muchii
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (i != j)
                a[i][j] = inf; // Inițializarea matricei de adiacență cu infinit pentru toate perechile de noduri

    for (int p, q, cost, i = 1; i <= m; i++)
    {
        fin >> p >> q >> cost; // Citirea informațiilor despre fiecare muchie (nod de plecare, nod de destinație și cost)
        a[p][q] = cost; // Setarea costului în matricea de adiacență pentru ambele direcții
        a[q][p] = cost;
    }

    for (int j = 1; j <= n; j++)
    {
        c[j] = a[1][j]; // Inițializarea costului minim de la nodul sursă (1) la celelalte noduri
        if (j != 1)
            t[j] = 1; // Setarea arborelui minim de acoperire pentru fiecare nod, inițializat cu nodul sursă
    }

    viz[1] = 1; // Nodul sursă este vizitat
    c[0] = inf;
    int cost = 0;

    for (int k = 2; k <= n; k++)
    {
        int min_c = 0;
        for (int i = 1; i <= n; i++)
            if (!viz[i] and c[i] < c[min_c]) // Căutarea nodului nevizitat cu cel mai mic cost
                min_c = i;
        viz[min_c] = 1; // Vizitarea nodului găsit cu cost minim

        for (int i = 1; i <= n; i++)
            if (!viz[i] and c[i] > a[min_c][i]) // Actualizarea costului minim și a arborelui minim de acoperire pentru nodurile nevizitate
            {
                c[i] = a[min_c][i];
                t[i] = min_c;
            }
    }

    for (int i = 1; i <= n; i++)
        cost += c[i]; // Calcularea costului total al arborelui minim de acoperire

    fout << cost << '\n'; // Scrierea costului în fișierul de ieșire
    for (int i = 1; i <= n; i++)
        fout << t[i] << ' '; // Scrierea arborelui minim de acoperire în fișierul de ieșire
}

int main()
{
    Prim(); // Apelarea funcției Prim
    return 0;
}

