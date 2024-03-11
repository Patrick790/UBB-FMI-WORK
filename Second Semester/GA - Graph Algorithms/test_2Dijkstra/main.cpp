#include    <iostream>
#include    <fstream>
#include    <queue>
#include    <vector>
using namespace std;
ifstream fin("dijkstra.in");
ofstream fout("dijkstra.out");
const int NMax = 50005;
const int oo = (1 << 30);
int N, M;
int D[NMax];
bool InCoada[NMax];
vector < pair <int,int> > G[NMax];
struct compara
{
    bool operator()(int x, int y)
    {
        return D[x] < D[y];
    }
};
priority_queue<int, vector<int>, compara> Coada;
void Citeste()
{
    fin >> N >> M;
    for(int i = 1; i <= M; i++)
    {
        int x, y, c;
        fin >> x >> y >> c;
        G[x].push_back(make_pair(y,c));
    }
}
void Dijkstra(int nodStart)
{
    for(int i = 1; i <= N; i++)
        D[i] = oo;
    D[nodStart]=0;
    Coada.push(nodStart);
    InCoada[nodStart] = true;
    while(!Coada.empty())
    {
        int nodCurent = Coada.top();
        Coada.pop();
        InCoada[nodCurent] = false;
        for(size_t i = 0; i < G[nodCurent].size(); i++)
        {
            int Vecin = G[nodCurent][i].first;
            int Cost = G[nodCurent][i].second;
            if(D[nodCurent] + Cost < D[Vecin])
            {
                D[Vecin] = D[nodCurent] + Cost;
                if(!InCoada[Vecin])
                {
                    Coada.push(Vecin);
                    InCoada[Vecin] = true;
                }
            }
        }
    }
}
void Afiseaza()
{
    for(int i = 2; i <= N; i++)
    {
        if(D[i] != oo)
            fout << D[i] << " ";
        else
            fout << "0 ";
    }
}
int main()
{
    Citeste();
    Dijkstra(1);
    Afiseaza();
}

