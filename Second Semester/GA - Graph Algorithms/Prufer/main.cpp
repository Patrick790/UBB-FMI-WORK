#include <bits/stdc++.h>
using namespace std;
int v[105],fr[105],matAd[105][105],n,p,u;

// Initializează array-ul fr cu valorile zero
void zero(){

    for(int i=1; i<=n+1; i++)
        fr[i]=0;
}

// Actualizează array-ul fr în funcție de valorile din array-ul v
void reinit(){

    for(int i=p; i<=u; i++)
        fr[v[i]]++;

}

void decodare() // decodare
{
    // Citeste valoarea lui n de la intrare
    cin >> n;

    // Citeste valorile elementelor din array-ul v și actualizează array-ul fr
    for (int i = 1; i <= n; i++)
    {
        cin >> v[i];
        fr[v[i]]++;
    }

    p = 1;   // Primul index al secvenței
    u = n;   // Ultimul index al secvenței

    int count = n;  // Contor pentru numărul total de elemente

    // Procesul de decodare
    while (count)
    {
        int i = 1;

        // Caută primul index i pentru care fr[i] este zero
        while (fr[i])
            i++;

        u++;       // Incrementează u pentru a adăuga un nou element în secvență
        v[u] = i;  // Adaugă valoarea lui i în array-ul v la poziția u

        int j = v[p];   // Obține valoarea elementului de la poziția p în array-ul v

        p++;  // Incrementează p pentru a trece la următorul element din secvență

        // Actualizează matricea de adiacență matAd pentru a reflecta relația între i și j
        matAd[i][j] = matAd[j][i] = 1;

        zero();   // Resetarea array-ului fr la zero
        reinit(); // Actualizarea array-ului fr în funcție de modificările din array-ul v

        count--;  // Decrementarea contorului pentru numărul total de elemente
    }

    cout << endl << "Decodare Prufer, matrice de adiacenta: " << endl;
    // Afisarea matricei de adiacenta
    for (int i = 1; i <= n + 1; i++, cout << '\n')
    {
        for (int j = 1; j <= n + 1; j++)
        {
            cout << matAd[i][j] << " ";
        }
    }

    cout << endl << endl;
}


void codare() //codare
{

    int t[105];
    cin>>n;
    cout<<"Dati vectorul de tati: ";
    for(int i=1; i<=n; i++)
        cin>>t[i];
    int count=n;
    while(count){

        int i, w;
        for(i=1; i<=n; i++)
        {   w=0;
            for(int j=1; j<=n; j++)
                if(t[j]==i) w=1;
            if(w==0) break;
        }
        cout<<t[i]<<" ";
        t[i]=i;
        count--;

    }

}

int main(){

    int cmd;
    cout<<"1 - Decodare | 2 - Codare: ";
    cin>>cmd;
    cmd==1?decodare():codare();
    return 0;

}
