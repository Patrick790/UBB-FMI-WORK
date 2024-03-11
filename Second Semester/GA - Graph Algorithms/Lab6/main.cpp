#include <bits/stdc++.h>

using namespace std;

const int NMAX = 1e3+5;

ifstream fin("1.in");

int n,m;

vector < int > graf[NMAX];

int cost[NMAX][NMAX], reziduri[NMAX][NMAX];
int viz[NMAX], pred[NMAX];

void citire(){
    int x, y, z;
    fin >> n >> m;
    for(int i = 1; i <= m; i++){
        fin >> x >> y >> z;
        x++;
        y++;
        cost[x][y] += z;
        graf[x].push_back(y);
        graf[y].push_back(x);
    }
}

int bfs(){
    for(int i = 0; i <= n; i++)
        viz[i] = 0;
    queue< int > noduri;
    noduri.push(1);
    viz[1] = 1;
    while(!noduri.empty()){
        int nc = noduri.front();
        cout << "Nod curent: " << nc << " | ";

        for(int i = 0; i < graf[nc].size()&&nc!=n;i++){
            int nv = graf[nc][i];

            if(reziduri[nc][nv] == cost[nc][nv] || viz[nv]==1)continue;

            cout << nv << " ";
            viz[nv] = 1;
            noduri.push(nv);

            pred[nv] = nc;
        }

        cout << '\n';

        noduri.pop();
    }
    return viz[n];
}

int edmonds_karp(){

    int noduri, fminim, flux;
    flux = 0;
    while(bfs()==1){
        for(int i = 0; i < graf[n].size(); i++)
        {
            int nc = graf[n][i];

            if(cost[nc][n] == reziduri[nc][n] || viz[nc] == 0)
                continue;
            pred[n] = nc;
            fminim = 550000005;
            for(noduri = n; noduri != 1; noduri = pred[noduri]){
                fminim = min(fminim,cost[pred[noduri]][noduri]-reziduri[pred[noduri]][noduri]);
            }
            if(fminim == 0)
                continue;
            for(noduri = n; noduri != 1; noduri = pred[noduri]){
                reziduri[pred[noduri]][noduri] += fminim;
                reziduri[noduri][pred[noduri]] -= fminim;
            }
            flux += fminim;
        }
    }
    return flux;

}

int main() {

    citire();
    cout << edmonds_karp();
    return 0;
}
