#include <stdio.h>

struct phanso
{
    long tu, mau;
};
typedef struct phanso PHANSO;

void showFraction(PHANSO t);
long GCD(int x, int y);
void inputFraction(PHANSO &t);

void inputFraction(PHANSO &t)
{
    printf("vui long nhap tu so: ");
    scanf("%ld", &t.tu);
    printf("vui long nhap mau so: ");
    scanf("%ld", &t.mau);
}

long GCD(long x, long y)
{
    long n1, n2;
    if (x > y)
    {
        n1 = x;
        n2 = y;
    }
    else
    {
        n1 = y;
        n2 = x;
    }

    while (n1 != n2)
    {
        if (n1 > n2)
            n1 -= n2;
        else
            n2 -= n1;
    }

    return n1;
}

PHANSO reduce(PHANSO &ps)
{
    int ucln = GCD(ps.tu, ps.mau);
    ps.tu = ps.tu / ucln;
    ps.mau = ps.mau / ucln;

    if (ps.mau != 1)
    {
        if (ps.mau < 0)
        {
            ps.mau = ps.mau * -1;
            ps.tu = ps.tu * -1;
        }
    }

    return ps;
}

void showFraction(PHANSO t)
{
    printf("%ld / %ld \n", t.tu, t.mau);
}

PHANSO operator+(PHANSO t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.mau + t1.mau * t2.tu;
    t.mau = t1.mau * t2.mau;
    return reduce(t);
}

int operator==(PHANSO t1, PHANSO t2)
{
    if (t1.tu * t2.mau == t1.mau * t2.tu)
        return 1;
    return 0;
}

int operator!=(PHANSO t1, PHANSO t2)
{
    if (t1.tu * t2.mau != t1.mau * t2.tu)
        return 1;
    return 0;
}

int operator>=(PHANSO t1, PHANSO t2)
{
    if (t1.tu * t2.mau >= t1.mau * t2.tu)
        return 1;
    return 0;
}

int operator>(PHANSO t1, PHANSO t2)
{
    if (t1.tu * t2.mau > t1.mau * t2.tu)
        return 1;
    return 0;
}

int operator<=(PHANSO t1, PHANSO t2)
{
    if (t1.tu * t2.mau <= t1.mau * t2.tu)
        return 1;
    return 0;
}

int operator<(PHANSO t1, PHANSO t2)
{
    if (t1.tu * t2.mau < t1.mau * t2.tu)
        return 1;
    return 0;
}

PHANSO operator-(PHANSO t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.mau - t1.mau * t2.tu;
    t.mau = t1.mau * t2.mau;
    return t;
}

PHANSO operator*(PHANSO t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.tu;
    t.mau = t1.mau * t2.mau;
    return reduce(t);
}

PHANSO operator/(PHANSO t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.mau;
    t.mau = t1.mau * t2.tu;
    return reduce(t);
}

int main()
{
    PHANSO t = {1, 2}, s = {2, 4};
    showFraction(t + s);
    showFraction(t - s);
    showFraction(t * s);
    showFraction(t / s);
    printf("%d \n", t == s);
    printf("%d \n", t != s);
    printf("%d \n", t > s);
    printf("%d \n", t >= s);
    printf("%d \n", t < s);
    printf("%d \n", t <= s);
    // printf("%d \n", t == s);

    return 0;
}