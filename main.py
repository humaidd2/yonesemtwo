class Vehicle:

    def __init__(self, name, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
        self.name = name

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name}, is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name}, is {capacity} passengers"


v = Bus("Audi", 500, 8500)
print(v.seating_capacity(65))

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def areaOfCircle(self):
        return math.pi * (self.radius ** 2)

    def perimeterOfCircle(self):
        return (math.pi * self.radius) * 2


class Bank:
    def __init__(self):
        self.acc_info = {}

    def create_acc(self, acc_num: int, starting_balance=0):
        """
        Create account with my basic bank, beware, I will probably steal all your money haha
        :param acc_num:
        :param starting_balance:
        :return:
        """
        if acc_num in self.acc_info:
            print("Account exists. Please use a different number")
        else:
            self.acc_info[acc_num] = starting_balance
            print(f"Account {acc_num} has been created")

    def deposit_money(self, acc_num, amount):
        """
        Deposit money into an existing account, beware, we spend our customer's money.
        :param acc_num:
        :param amount:
        :return:
        """
        if acc_num in self.acc_info:
            self.acc_info[acc_num] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist, Please Create Accoount")

    def withdraw_money(self, acc_num, amount):
        """
        Widthdraw money from an existing account.
        :param acc_num:
        :param amount:
        :return:
        """
        if acc_num in self.acc_info:
            if self.acc_info[acc_num] >= amount:
                self.acc_info[acc_num] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    def check_balance(self, acc_num):
        """
        Check for the balance of an existing account, if your money is not there, it's probably because I stole it. haha
        :param acc_num:
        :return:
        """
        if acc_num in self.acc_info:
            balance = self.acc_info[acc_num]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")
