#include <stdio.h>

int factorial(int);
int combination(int);

int factorial(int n)
{
    int result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }
    return result;
}

int combination(int n, int k)
{
    return factorial(n) / (factorial(k) * factorial(n - k));
}

int main()
{
    int n, k;
    printf("Input n: ");
    scanf("%d", &n);
    printf("Input k: ");
    scanf("%d", &k);

    if (n < k || k < 0)
    {
        printf("n or k invalid \n");
        return 0;
    }
    printf("Result: %d\n", combination(n, k));
    return 0;
}
