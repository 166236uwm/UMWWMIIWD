import main
import random

def evenStringI(str):
    """
    Returns string made of elements of given string with even index numbers
    """
    return str[::2]


def lastLetters(str, n = 1):
    """
    Returns number n of last characters in order from left to right
    """

    return str[-n:]


def reverseString(str):
    """
    Returns reversed string
    """
    return str[::-1]


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


def insertingName(name, dateOfBirth):
    myData = "My name is {}. My date of birth is {}"
    return myData.format(name, dateOfBirth)


def listingNaturalNums(n):
    """
    Returns n first natural numbers
    """
    nums = [i for i in range(0, n)]
    return nums


def toThePowerOfFive(n):
    """
    Returns n fits natural numbers to the power of five
    """
    nums = [i ** 5 for i in range(0, n)]
    return nums


def listedFactorial(n):
    """
    Returns factorial of first n natural numbers
    """
    nums = [main.factorial(i) for i in range(0, n)]
    return nums


def listOfEulers(n):
    """
    Returns n number of Euler's number raised to the power of n
    """
    nums = [main.eulers(100) ** i for i in listingNaturalNums(n)]
    return nums


def listOfLengths(listOfStr):
    """
    Given a list of strings returns their lengths
    """
    nums = [len(i) for i in listOfStr]
    return nums


def program32():
    """
    This is suposed to add 1 to 10, 2 to 20 etc.
    """
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [10, 20, 40, 40, 50, 60, 70, 80, 90, 100]
    list3 = [[]]
    for x in list1:
        for y in list2:
            list3.append([x,y])
    return list3


def months():
    months = [
        'Jenuary', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]
    random.shuffle(months)
    print(months)
    months.sort()
    return months


def latterThanGiven(names, letter):

    return
