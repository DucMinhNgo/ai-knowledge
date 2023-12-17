#include <stdio.h>

#define N 50
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
    printf("Input numerator: ");
    scanf("%ld", &t.tu);
    printf("Input denominator: ");
    scanf("%ld", &t.mau);
}

void inputFractionArray(int &m, PHANSO b[N])
{
    do
    {
        printf("Input m: ");
        scanf("%d", &m);
    } while (m <= 0 || m > N);

    for (int i = 0; i < m; i++)
    {
        printf("Input Fraction b[%d]:\n", i + 1);
        inputFraction(b[i]);
    }
}

long GCD(long a, long b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

PHANSO reduce(PHANSO &ps)
{
    int gcd = GCD(ps.tu, ps.mau);

    ps.tu /= gcd;
    ps.mau /= gcd;

    return ps;
}

void showFraction(PHANSO t)
{
    printf("%ld / %ld \n", t.tu, t.mau);
}

void showFactionArray(int m, PHANSO b[N])
{
    for (int i = 0; i < m; i++)
    {
        printf("Show Fraction b[%d]:\n", i + 1);
        showFraction(b[i]);
    }
}

PHANSO operator+(PHANSO t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.mau + t1.mau * t2.tu;
    t.mau = t1.mau * t2.mau;
    return reduce(t);
}

PHANSO operator+=(PHANSO &t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.mau + t1.mau * t2.tu;
    t.mau = t1.mau * t2.mau;

    t1 = reduce(t);
    return t1;
}

PHANSO operator-(PHANSO t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.mau - t1.mau * t2.tu;
    t.mau = t1.mau * t2.mau;
    return reduce(t);
}

PHANSO operator-=(PHANSO &t1, PHANSO t2)
{
    PHANSO t;
    t.tu = t1.tu * t2.mau - t1.mau * t2.tu;
    t.mau = t1.mau * t2.mau;
    t1 = reduce(t);
    return t1;
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

PHANSO findLargestElementInFraction(int m, PHANSO t[N])
{
    PHANSO max = t[0];
    for (int i = 1; i < m; i++)
    {
        if (t[i] > max)
        {
            max = t[i];
        }
    }

    return max;
}

PHANSO sumOfFactionArray(int m, PHANSO t[N])
{
    PHANSO sum = t[0];
    for (int i = 1; i < m; i++)
    {
        sum += t[i];
    }

    return reduce(sum);
}

void arrangingFactionArray(int m, PHANSO t[N])
{
    for (int i = 0; i < m - 1; i++)
    {
        for (int j = i + 1; j < m; j++)
        {
            if (t[i] > t[j])
            {
                PHANSO tempt;
                tempt = t[i];
                t[i] = t[j];
                t[j] = tempt;
            }
        }
    }
}

int main()
{
    PHANSO t, s;
    printf("Input Fraction t:\n");
    inputFraction(t);
    printf("Input Fraction s:\n");
    inputFraction(s);
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
    showFraction(t += s);
    showFraction(t -= s);

    PHANSO b[N];
    int m;
    inputFractionArray(m, b);
    showFactionArray(m, b);
    showFraction(findLargestElementInFraction(m, b));
    showFraction(sumOfFactionArray(m, b));
    arrangingFactionArray(m, b);
    showFactionArray(m, b);

    return 0;
}