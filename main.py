def exc1(n):
    return (1 + (1 / n)) ** n


def eulers(n):
    s = 1
    i = 1
    while i <= n:
        s += 1 / factorial(i)
        i += 1
    return s


def factorial(k):
    if k > 1:
        return k * factorial(k - 1)
    else:
        return k


def NWD(m, n):
    if m > n:
        d = n
        while m % d != 0 or n % d != 0:
            d -= 1
            if d <= 1:
                return "no common divisors"
        return d
    elif n > m:
        NWD(n, m)
    else:
        return n

