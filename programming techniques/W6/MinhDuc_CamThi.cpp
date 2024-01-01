#include <stdio.h>

#define N 50

void showMatrix(int m, int n, int a[N][N])
{
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
}

void addMatrixFromFile(int &m, int &n, int a[N][N])
{
    FILE *fp = fopen("input.txt", "r");
    fscanf(fp, "%d", &m);
    fscanf(fp, "%d", &n);
    if (fp != NULL)
    {
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                fscanf(fp, "%d", &a[i][j]);
            }
        }
    }

    fclose(fp);
}

int isPrime(int n)
{
    if (n <= 1)
        return 0;

    for (int i = 2; i <= n / 2; i++)
        if (n % i == 0)
            return 0;

    return 1;
}

int computingSumOfPrime(int m, int n, int a[N][N])
{
    int sum = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (isPrime(a[i][j]))
            {
                sum += a[i][j];
            }
        }
    }
    return sum;
}

void saveToFile(int n)
{
    printf("%d\n", n);
    FILE *fp = fopen("output.txt", "w");
    if (fp)
    {
        fprintf(fp, "%d", n);
    }
    fclose(fp);
}

int main()
{
    int a[N][N] = {0}, m, n;
    addMatrixFromFile(m, n, a);
    showMatrix(m, n, a);
    saveToFile(computingSumOfPrime(m, n, a));
    return 0;
}