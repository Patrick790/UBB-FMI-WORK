#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

ifstream fin("apm.in");
ofstream fout("apm.out");

const int MMax = 400005;

pair<int, int> P[MMax];
int k;

int N, M, Total, TT[MMax], RG[MMax];

struct Muchie{
    int x, y, cost;
}V[MMax];

bool Compare(Muchie a, Muchie b){
    return a.cost < b.cost;
}

void Read(){
    fin >> N >> M;

    for(int i = 1; i <= M; i++)
        fin >> V[i].x >> V[i].y >> V[i].cost;

    sort(V+1, V+M+1, Compare);

    for(int i = 1;i<=N; i++){
        TT[i] = i;
        RG[i] = 1;
    }

}

int Find(int nod){
    while(TT[nod] != nod)
        nod = TT[nod];
    return nod;
}

void Unire(int x, int y){
    if(RG[x] < RG[y])
        TT[x] = y;
    if(RG[x] > RG[y])
        TT[y] = x;
    if(RG[x] == RG[y]){
        TT[x] = y;
        RG[y]++;
    }
}

void Rezolva(){
    for(int i = 1; i <= M; i++)
    {
        int tatal_x = Find(V[i].x);
        int tatal_y = Find(V[i].y);
        if(tatal_x != tatal_y)
        {
            Unire(tatal_x, tatal_y);
            P[++k].first = V[i].x;
            P[k].second = V[i].y;
            Total += V[i].cost;
        }
    }
}

int main() {

    Read();

    Rezolva();

    fout << Total << "\n";
    fout << N-1 <<"\n";

    for(int i = 1; i <= k; i++)
        fout << P[i].first << " " << P[i].second << "\n";

    return 0;
}
