#include <stdio.h>

#define N 50

void arrayIntInput(int a[], int &n);
void arrayIntOutput(int a[], int n);

void arrayIntInput(int a[], int &n)
{
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
}

void arrayIntOutput(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        if (i > 0)
        {
            printf(" ");
        }
        printf("%d", a[i]);
    }
}

int main()
{
    int b[N], m;
    arrayIntInput(b, m);
    arrayIntOutput(b, m);
    return 0;
}
