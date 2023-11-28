#include <stdio.h>

unsigned long long computingTax(unsigned long long);
#define L1 4000000
#define L2 6000000
#define L3 9000000
#define L4 14000000
#define L5 24000000
#define L6 44000000
#define L7 84000000

unsigned long long computingTax(unsigned long long n)
{
    unsigned long long tax = 0;

    if (0 < n && n <= L1)
    {
        tax = 0;
    }
    else if (L1 < n && n <= L2)
    {
        tax = (n - L1) * 0.05;
    }
    else if (L2 < n && n <= L3)
    {
        tax = (L2 - L1) * 0.05 + (n - L2) * 0.1;
    }
    else if (L3 < n && n <= L4)
    {
        tax = (L2 - L1) * 0.05 + (L3 - L2) * 0.1 + (n - L3) * 0.15;
    }
    else if (L4 < n && n <= L5)
    {
        tax = (L2 - L1) * 0.05 + (L3 - L2) * 0.1 + (L4 - L3) * 0.15 + (n - L4) * 0.2;
    }
    else if (L5 < n && n <= L6)
    {
        tax = (L2 - L1) * 0.05 + (L3 - L2) * 0.1 + (L4 - L3) * 0.15 + (L5 - L4) * 0.2 + (n - L5) * 0.25;
    }
    else if (L6 < n && n <= L7)
    {
        tax = (L2 - L1) * 0.05 + (L3 - L2) * 0.1 + (L4 - L3) * 0.15 + (L5 - L4) * 0.2 + (L6 - L5) * 0.25 + (n - L6) * 0.3;
    }
    else
    {
        tax = (L2 - L1) * 0.05 + (L3 - L2) * 0.1 + (L4 - L3) * 0.15 + (L5 - L4) * 0.2 + (L6 - L5) * 0.25 + (L7 - L6) * 0.3 + (n - L7) * 0.35;
    }
    return tax;
}

int main()
{
    unsigned long long n;
    printf("Input n: ");
    scanf("%llu", &n);
    printf("Output: %llu \n", computingTax(n));
    return 0;
}