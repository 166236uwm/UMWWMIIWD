import math

def seriesLimit(n):
    i = 1
    s = 0
    while n >= i:
        s += 1 / math.factorial(i)
        i += 1
    return s


def modulo(a,b):
    if isinstance(a, float) or isinstance(b, float):
        return math.fmod(a, b)
    return a % b


def log(a, n):
    k = 2
    while k <= n:
        print(math.log(a, k), end = '|')
        k += 1


def tests(a):
    return math.exp(a), math.e ** a, math.pow(math.e, a)


def evenStringI(str):
    """
    Returns string made of elements of given string with even index numbers
    """
    i = 0
    strnew = ""
    while len(str) > i:
        strnew += str[i]
        i += 2
    return strnew


def lastLetters(str, n = 1):
    """
    Returns number n of last characters in order from left to right
    """
    i = len(str)
    strnew = ""
    while n > 0:
        strnew += str[len(str) - n]
        n -= 1
    return strnew


def reverseString(str):
    """
    Returns reversed string
    """
    length = len(str) - 1
    strnew = ""
    while length >= 0:
        strnew += str[length]
        length -= 1
    return strnew


def longer(str1, str2):
    """
    Returns the longer string of two
    """
    if len(str1) > len(str2):
        return str1
    elif len(str1) == len(str2):
        return str1, str2, " They both are the same lenght"
    else:
        return str2


def sortingMonths():
    months = [
        'Jenuary', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]
    months.sort(key = sortKey)
    return months


def sortKey(m):
    return len(m)



