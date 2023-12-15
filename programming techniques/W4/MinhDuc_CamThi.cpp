#include <stdio.h>

#define N 50

void arrayIntInput(int a[], int &n);
void arrayIntOutput(int a[], int n);
int sumOfEvenElements(int a[], int n);
int productOfOddPositions(int a[], int n);

void arrayIntInput(int a[], int &n)
{
    for (int i = 0; i < n; ++i)
    {
        printf("a[%d] = ", i);
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
    printf("\n");
}

int sumOfEvenElements(int a[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] % 2 == 0)
        {
            sum += a[i];
        }
    }
    return sum;
}

int productOfOddPositions(int a[], int n)
{
    int product = 1;
    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 1)
        {
            product *= a[i];
        }
    }
    return product;
}

int main()
{
    int b[N], m;
    printf("Input m: ");
    scanf("%d", &m);
    arrayIntInput(b, m);
    arrayIntOutput(b, m);
    printf("Sum of Even Elements: %d \n", sumOfEvenElements(b, m));
    printf("Product in Odd Position: %d \n", productOfOddPositions(b, m));
    return 0;
}
