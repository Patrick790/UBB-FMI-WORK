#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, nr, s=0;
    printf("Introduceti n: ");
    scanf("%d", &n);
    for(i=1;i<=n;i++)
    {
        scanf("%d", &nr);
        s += nr;

    }
    printf("%d", s);

    return 0;
}
