# class
class Human:
    #Attributes
    def __init__(self, name, age, course, college):
        self.name = name
        self.age = age
        self.course = course
        self.college = college

    #Method
    def details(self):
            print(f"The {self.name}, and {self.age} yeas old taken a {self.course} course in {self.college} college")
#object
Raji = Human("Rajeshwari",22, "Mca", "Rajarajeshwari College of Engineering")
Aishu = Human("Aishu", 23, "Bca", "Anupama College")

Raji.details()
Aishu.details()
print("-----")
#2.
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_details(self):
        print(f"the Mobile is {self.brand} and this price is {self.price}")

sumsung = Mobile("Sumsung", 55000)
redmi = Mobile("Redmi", 25000)

sumsung.display_details()
redmi.display_details()

print("-------------")

#3

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"The student name is {self.name} and their marks {self.marks}")

Ammu = Student("Keerthana", 78)
kavya = Student("Kavya", 90)
chandu = Student("Chandu", 85)

Ammu.display_info()
kavya.display_info()
chandu.display_info()
print("------------ Task1 --------------")
#
# 🟢 Task 1: Student Class (Basics)
# Create a class Student
#
# Requirements:
#
# Attributes: name, roll_no, marks
#
# Method display() → prints all details
#
# Method result()
#
# If marks ≥ 40 → print "Pass"
#
# Else → print "Fail"
#
# 👉 Create 2 student objects and call both methods.

class Students:
    def __init__(self,name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"the Student roll_no {self.roll_no}, name {self.name} and their marks {self.marks}")

    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

vaishnavi = Students("Vaishnavi", "1001", 50)
neha = Students("Neha", "1002", 68)
jon = Students("Jone", "1003", 38)

vaishnavi.display()
vaishnavi.result()

neha.display()
neha.result()

jon.display()
jon.result()

print("------------ Task2 --------------")
# Task 2: Bank Account Class (Methods + Logic)
#
# Create a class BankAccount
# Attributes:
# account_holder
# balance
# Methods:
# deposit(amount) → add amount to balance
# withdraw(amount)
# If amount ≤ balance → withdraw
# Else → print "Insufficient balance"
# show_balance() → print current balance
# 👉 Create one object, do:
# deposit
# withdraw
# show balance

class BackAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        amount_balance = amount + self.balance
        print(f"add amount to balance {amount_balance}")

    def withdraw(self):
        if self.amount <= self.balance:
            print("withdraw")
        else:
            print("Insufficient balance")

    def show_balance(self):
        amount_balance = self.amount + self.balance
        print(f"current balance {amount_balance}")

SBI = BackAccount("Balayya", 20000)

SBI.deposit(5000)
SBI.withdraw()
SBI.show_balance()

print("------------ Task4 --------------")
# Task 3: Rectangle Class (Calculation)

# Create a class Rectangle
#
# Attributes:
#
# length
#
# width
#
# Methods:
#
# area() → return area
#
# perimeter() → return perimeter
#
# 👉 Create an object and print area & perimeter

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def Perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(2, 5)
print(r.area())
print(r.Perimeter())

