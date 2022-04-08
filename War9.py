l = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']

def func_5(l):
    newList = []
    newList += [x for x in l if( 'i' and 'a' )in x]
    return newList


print(func_5(l))

class Frac:
    def __init__(self, a, b):
        self.nominator = a
        self.denominator = b
        self.shortening()
    def disp(self):
        print(int(self.nominator),"/",int(self.denominator), sep = "")
    def shortening(self):
        a = NWD(abs(self.nominator), abs(self.denominator))
        self.nominator /= a
        self.denominator /= a
    def addition(self, other):
        self.nominator = self.nominator * other.denominator + other.nominator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.shortening()
        self.disp()
    def product(self, other):
        self.nominator *= other.nominator
        self.denominator *= other.denominator
        self.shortening()
        self.disp()
    def comparison(self, other):
        a = self.nominator / self.denominator
        b = other.nominator / other.denominator
        if a > b:
            return True
        return False


def abs(n):
    if n < 0:
        return -n
    return n

def NWD(m, n):
    if m > n:
        d = n
        while m % d != 0 or n % d != 0:
            d -= 1
            if d <= 1:
                return 1
        return d
    elif n > m:
        return NWD(n, m)
    else:
        return n