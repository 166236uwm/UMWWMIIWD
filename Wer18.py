#Bloch Tomasz 166236 Wariant 18

def func_1(a):
    b = set(a)
    for x in b:
        print(x)


def func_2(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    print(2 * func_2(n - 1) + func_2(n - 2) - func_2(n - 3))


def func_3(*arg):
    sum = 1
    for x in arg:
        sum *= x
    return sum


def func_4(str):
    return str[::3]


def func_5():
    nums = range(1, 50)
    newNums =  [x ** 2 for x in nums if x % 2 == 0]
    return newNums


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
    def retract(self, other):
        self.nominator = self.nominator * other.denominator - other.nominator * self.denominator
        self.denominator = self.denominator * other.denominator
        self.shortening()
        self.disp()
    def quotient(self, other):
        self.nominator *= other.denominator
        self.denominator *= other.denominator
        self.shortening()
        self.disp()
    def comparison(self, other):
        if self.nominator == other.nominator and self.denominator == other.denominator:
            return True
        return False


