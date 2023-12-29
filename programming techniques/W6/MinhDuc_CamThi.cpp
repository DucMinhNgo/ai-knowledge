#include <stdio.h>

int main()
{
    int a[50][50] = {0}, m, n;
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

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    fclose(fp);
    return 0;
}