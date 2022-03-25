def addToTuple(t, value):
    l = list(t)
    l.append(value)
    x = tuple(l)
    return x


def addToTupleOtherWay(t, value):
    tup = (value,)
    t += tup
    return t


def removeFromTuple(t, value):
    l = list(t)
    l.remove(value)
    return tuple(l)


def withoutRepetition(l):
    return list(set(l))


def withoutRepetition2(l):
    return list(dict.fromkeys(l))


def printPhoneNumbers(d = {
        "Jacek Soplica": 123456789,
        "Macko z Bogdanca": 987654321,
        "Zbyszko":123432109
    }):
    for x in d:
        print(x, "ma numer", d[x])

def dniOfWeek(l, lang):
    days = {
        "Poniedziałek": "Monday",
        "Wtorek": "Tuesday",
        "Środa": "Wedensday",
        "Czwartek": "Thursday",
        "Piątek": "Friday",
        "Sobota": "Saturday",
        "Niedziela": "Sunday"
    }
    if lang == "pl":
        for x in l:
            print(days[x])
    else:
        for x in days:
            for y in l:
                if y == x:
                    print(x)

def romanToArabic(str):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = list(str)
    sum = 0
    for x in range(0, len(num) - 1):
        if isGreater(dict, num, x):
            sum += dict[num[x]]
        else:
            sum -= dict[num[x]]
    sum += dict[num[len(num)-1]]
    return sum



def isGreater(dict, num, x):
    number = dict[num[x]]
    if number < dict[num[x+1]]:
        return False
    return True


def numsToThePower(l, n):
    return [i ** n for i in l]


def sumOfNumsToThePower(l, n):
    sum = 0;
    for x in l:
        sum += x ** n
    return sum


def mean(l):
    sum = 0
    for i in l:
        sum += i
    return sum / len(l)


def gmean(l):
    sum = 1
    for i in l:
        sum *= i
    return sum ** (1/len(l))