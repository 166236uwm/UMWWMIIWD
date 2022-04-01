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

def arabicToRoman(num):
    str = ""
    dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    while(num > 0):
        if(num >= 1000):
            str += dict[1000]
            num -= 1000
        elif(num >= 500):
            str += dict[500]
            num -= 500
        elif (num >= 400):
            str += "CD"
            num -= 400
        elif(num >= 100):
            str += dict[100]
            num -= 100
        elif (num >= 90):
            str += "XC"
            num -= 90
        elif(num >= 50):
            str += dict[50]
            num -= 50
        elif(num >= 10):
            str += dict[10]
            num -= 10
        elif (num >= 9):
            str += "IX"
            num -= 9
        elif(num >= 5):
            str += dict[5]
            num -= 5
        else:
            str += dict[1]
            num -= 1
    return str

class Roman:
    def __init__(self, str):
        self.value = str

    def add(self, str):
        self.value = arabicToRoman(romanToArabic(self.value) + romanToArabic(str))

    def retract(self, str):
        self.value = arabicToRoman(romanToArabic(self.value) - romanToArabic(str))

    def multiply(self, str):
        self.value = arabicToRoman(romanToArabic(self.value) * romanToArabic(str))

def zad3(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibb(i-1) + fibb(i - 2)

def zad4(n):
    sum = 0
    for i in range(1, n):
        sum += i ** 3
    return sum

def zad5():
    str = "I study at the Univeristy of Warmia and Mazury in Olsztyn"
    return str[::3]

def zad6(tup):
    min = max = tup[0]
    for i in tup:
        if min > i:
            min = i
        if max < i:
            max = i
