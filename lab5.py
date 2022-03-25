import lab4


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


class Fruit:
    def __init__(self, color, weight, shape):
        self.color = color
        self.weight = weight
        self.shape = shape
    def isFresh(self):
        if(self.color == "Brown" or self.color == "Black"):
            return False
        return True

class Banana(Fruit):
    def __init__(self,taste):
        self.taste = taste


class Account:
    def __init__(self, startingBalance = 0):
        self.startingBalance = startingBalance
        self.balance = startingBalance

    def externalOutGoingTransfer(self, amount, otherAccount):
        self.startingBalance -= amount
        otherAccount.externalInCommingTransfer(amount)
    def externalInCommingTransfer(self, amount):
        self.balance += amount
    def whatIsMyBalance(self):
        print(self.balance)
    def cashWithdrawal(self, amount):
        self.balance -= amount


class PrivateAccount(Account):
    def salary(self, amount):
        self.balance += amount


class FirmAccount(Account):
    def transferToZUS(self, amount, ZUS):
        ZUS.balance += amount


class Roman:
    def __init__(self, str):
        self.value = str

    def add(self, str):
        self.value = arabicToRoman(lab4.romanToArabic(self.value) + lab4.romanToArabic(str))

    def retract(self, str):
        self.value = arabicToRoman(lab4.romanToArabic(self.value) - lab4.romanToArabic(str))

    def multiply(self, str):
        self.value = arabicToRoman(lab4.romanToArabic(self.value) * lab4.romanToArabic(str))

class Hero:
    def __init__(self, name, lp, tact):
        self.name = name
        self.lifePoints = lp
        self.tacticPoints = tact

    def attacked(self, hit):
        if hit > self.lifePoints:
            self.lifePoints = 0
        else:
            self.lifePoints -= hit

class Archer(Hero):
    def __init__(self, dext):
        self.dexterity = dext

    def attack(self, enemy):
        enemy.lifePoints -= self.dexterity * self.tacticPoints * self.lifePoints


class Warrior(Hero):
    def __init__(self, strength):
        self.strength = strength

    def attack(self, enemy):
        if self.lifePoints >= 20:
            enemy.attacked(self.strength * self.tacticPoints * self.lifePoints)
        else:
            enemy.attacked(self.strength * self.tacticPoints * 150)