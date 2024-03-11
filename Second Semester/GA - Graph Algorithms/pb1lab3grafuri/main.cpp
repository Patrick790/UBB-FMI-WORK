#include <iostream>
#include <fstream>
#include <queue>
#include <vector>


using namespace std;

ifstream fin("dijkstra.in");
ofstream fout("dijkstra.out");

const int NMax = 50005;
const int oo = (1 << 30);

int N, M;
int D[NMax];///vector de distante
bool InCoada[NMax];///stocheaza cand un nod intra in coada

vector < pair < int, int > > G[NMax];///G[1] drumurile care incep in 1 si se termina intr-un anumit nod

struct comparaDistante {
    bool operator()(int x, int y)
    {
        return D[x] > D[y];
    }
};
priority_queue < int, vector< int >, comparaDistante > Coada;

void Citeste() {
    fin >> N >> M;
    for (int i = 1;i <= M; i++)
    {
        int x, y, c; ///nod x, nod y, costul dintre cele doua
        fin >> x >> y >> c;
        G[x].push_back(make_pair(y, c));///pune in G toti vecinii y care au costul c
    }
}

void Afiseaza() {
    for (int i = 2; i <= N; i++)
    {
        if (D[i] != oo)
            fout << D[i] << " ";
        else
            fout << "0 ";
    }
}

void Dijkstra(int nod_start) {
    for (int i = 1; i <= N; i++)
        D[i] = oo;///setez toate distantele la infinit

    D[nod_start] = 0;
    Coada.push(nod_start);
    InCoada[nod_start] = true;
    while (!Coada.empty()) {
        int nod_curent = Coada.top();
        Coada.pop();
        InCoada[nod_curent] = false;
        for (size_t i = 1; i <= G[nod_curent].size(); i++)
        {
            int Vecin = G[nod_curent][i].first;
            int Cost = G[nod_curent][i].second;
            if (D[nod_curent] + Cost < D[Vecin])
            {
                D[Vecin] = D[nod_curent] + Cost;
                if (InCoada[Vecin] == false)
                {
                    Coada.push(Vecin);
                    InCoada[Vecin] = true;


                }
            }
        }

    }


}
int main() {

    Citeste();
    Dijkstra(1);
    Afiseaza();
    fin.close();
    fout.close();
    return 0;
}
