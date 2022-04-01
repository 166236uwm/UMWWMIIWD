def zad1(dict):
    return [tuple(x.values()) for x in dict]

class Polynomial:
    def __init__(self, values):
        self.values = values
        self.l = len(self.values)
    def output(self):
        i = 0
        while i < len(self.values):
            if len(self.values) - i - 1 != 0:
                print(self.values[i], "x^", len(self.values) - i - 1, sep = "", end="+")
            else:
                print(self.values[i])
            i += 1
    def addition(self, other):
        """
        adds other to self
        """
        i = self.l
        j = other.l
        while i != j:
            if j > i:
                self.values.insert(0, other.values[i])
                self.l += 1
                i += 1
            elif i > j:
                i = j
        for x in range(0, i - 1):
            self.values[x] += other.values[x]


    def retraction(self, other):
        i = self.l
        j = other.l
        while i != j:
            if j > i:
                self.values.insert(0, other.values[i])
                self.l += 1
                i += 1
            elif i > j:
                i = j
        for x in range(0, i - 1):
            self.values[x] -= other.values[x]


def zad3(n, k):
    if k == n or k == 0:
        return 1
    else:
        return zad3(n - 1, k - 1) + zad3(n - 1, k)


def zad4(*args):
    n = args[len(args)-1]
    a = list(args)
    a.pop(len(a)-1)
    l = []
    for x in a:
        l.append(x**n)
    return l

def zad5():
    str = "I study at the Univeristy of Warmia and Mazury in Olsztyn"
    return str[::4]


def zad6():
    return [i ** 3 for i in range(1, 30)]