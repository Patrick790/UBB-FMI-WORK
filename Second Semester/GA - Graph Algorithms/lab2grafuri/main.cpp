#include <iostream>
#include <fstream>


using namespace std;

ifstream fin("graf.txt");

int n, m, matrice[101][101], x,y;
int vizitat[101][101];
int mini = -1, rez[101];

void dfs(int nod, int nr)
{
    int vcount = 0;
    for(int i=0;i<=n;i++)
        if(matrice[nod][i] && vizitat[nod][i] == 0)
        {
            vizitat[nod][i] = 1;
            rez[nr] = i;
            dfs(i,nr+1);
            vizitat[nod][i] = 0;
            vcount++;
        }
    if (vcount==0 && (mini == -1 || nr < mini))
        mini = nr;
}

int main()
{
    fin>>n;
    while(fin>>x>>y)
        matrice[x][y]=1;

    int x;
    cout<<"Varful sursa: ";
    cin>>x;

    int nr = 0;
    dfs(x,nr);

    cout << x << " ";
    for(int i=0;i<mini;i++)
        cout << rez[i] << " ";

    return 0;
}
