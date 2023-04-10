from math import floor, sqrt
from random import randrange
from sympy import Integers, PolynomialRing

def is_prime(n, k=10):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Tính các giá trị cần thiết
    r = n - 1
    e = 0
    while r % 2 == 0:
        r //= 2
        e += 1
    l = floor((2 * sqrt(euler_phi(r)) * log(n, 2) + 1))

    # Kiểm tra n k lần
    for i in range(k):
        a = randrange(1, l)
        s = Integers(n)
        R = PolynomialRing(s, 'x')
        F = R.quotient(R(x)**r - 1)
        q = F(R(x + a))
        V = F(q**n)
        d = R(x)**e + a
        if V != d:
            return False

    return True

is_prime(7)