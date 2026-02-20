# 1. arithmetic operatio

# write a python program that perform the basic arthmetic operator on two numbers define the two teo numbersnas variables within the code and print the results for each operation
num1 = 10
num2 = 20

print("Addition of two number", num1 + num2)
print("Addition of two number", num1 - num2)
print("Addition of two number", num1 * num2)
print("Addition of two number", num1 / num2)

print("-------------------------------")

# 2. Swap two numbers : write a python program that swaps the values of two variables with and without using a third variable

a = 10
b = 20

print(f"Before swap a = {a} and b = {b}")

a = a + b  # 30
b = a - b  # 10
a = a - b  # 20

print(f"After swap a = {a} and b = {b}")

print("--------------------------")

# 3. Simple Greeting Program : write a python program that asks the user for their name and age, then print a personalized greeting message. Use both the + operator and F-string for output

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("hello, " + name + "! You are " + str(age) + " years old")
print(f"Hello, {name} You are {age} years old")

print("--------------------------")

# 4. string manipulation program : write a python program takes a sentence as input from the user, print the sentence in all uppercase and lowercase, relapce all spaces eith underscore and remove the lrading and trailing withspace

text = input("Enter a string: ")

print(text.upper())
print(text.lower())
print(text.replace(" ", "_"))
print(text.strip())

print("--------------------------")

# 5. character count: write a python program that asks the user for a string and print how many charcter are in the steing, excluding spaces

s = input("Enter s sting: ")
print(len(s.replace(" ","")))

print("--------------------------")

# 6. escape sequence : write a python program that suer escape sequences print the output as
# Hello
#       World
# This is a Backlash \

print("Hello\n\tWorld\nThis is a Backlash \\")

print("--------------------------")

# 7. logical operator: write a python program that takes two number as input from user and check
# Both numbers are greater than 10 (using and)
# at least one number is less than 5 (using or)
# The first number is not grater than the second number (using not)

a = int(input("Enter a first number: "))
b = int(input("Entre a second number: "))

print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>b))

print("--------------------------")

# 8. compression operator: create a python program that asks the user for their age and print
# "You are adult" if age is greater than or equal to 18
# "You are a minor" if age is less than 18
# use >= and <= compression operator

age = int(input("Enter a age: "))

if age>=18:
    print("You are adult")
else:
    print("You are a minor")

print("--------------------------")

# 9. Membership operator: write a python program thar take a string as inout from the user check id the letter "a" is in the string and checks if the string doen't contain the word "Python'

word = input("Enter a string: ")

print("a" in word)
print("Python" not in word)

print("--------------------------")

# 10. bitwise operator: given two integer, write a python program that print the result a & b, a | b, and a ^ b
# shits the bits of a two position to the left (a << 2)
# shits the bits of b two position to the right (a >> 2)

a = 2
b = 10

print(a & b)
print(a | b)
print(a ^ b)
print("the left shift: ", a << 2)
print("the right shift: ", b >> 2)

print("--------------------------")

# 11. list manipulatiion : carete a lish of 5 items and add a new item to the end of the lish and another list at the second position
# remove the third item from the list and print the list after each operator

l = [10, "a", 20, True, "main"]

l.append(30)
l.insert(1, 10.00)
l.remove("a")
print(l)

print("--------------------------")

# 12. reversed and sort the list : create a list of numbers and sort it in descending order ans reverse the sorted list and print id
l1 = [10, 20, 40, 60, 30, 50]
print(l1)
l1.sort()
print(l1[::-1])

print("--------------------------")

# 13. Tuple operation: create a tuple with 5 elements
# try to modify one of the elements and what happens
# perform slicing on the tuple to select the second and third elements

t = (10, 20, 30, 40, 50)
print(t[1:3])


print("--------------------------")

# 14 . set operation : create one set with your favorite fruits and another with your friend favorite fruits
# find the union, intersection, and difference between the two sets
# add a new fruit to your set remove the fruit from your set using both .remove() and .discard() waht happens when the fruit does not exisis

Rf = {"apple", 'mango', 'orange'}
Af = {'banana', 'kavi', 'orange'}

print(Rf | Af)
print(Rf & Af)
print(Rf - Af)

Rf.add("painapple")

Rf.remove('orange')
Rf.discard('kavi')

print(Rf)

print("--------------------------")

# 15.  Tuple and set Comparison
# create a list of elements and convert it into both tuple and setprint both the tuple and set and try to add the new elements to the tuple and set what disfferencs do you observed

ll = [1, 2, 3, 4, 5]
print(ll)
t = tuple(ll)
s = set(ll)
print(t)
print(s)

# t[3] = 20   # the tuple con not add new element because tuple is immutable

s.add(23)
print(s)


print("--------------------------")

# 16. Basic directionary Operations : create a dictionary to store information about cities in karnataka and their famous dishes
# and a new city and its dish to the dictionary
# update the dish for bengalore
# remove one city from the dictionary
# use the keys() method to print all city names in the dictionary
# use the values() methods to print all dishes in the dictionary

dishes = {
    "Bengalore": "Bisi Bisi bele bath",
    "Mysore": "Mysore park",
    "Davangere": "Benne dose",
    "Mandya": "Katabath"
}
print(dishes)
dishes["Ballary"] = "Pogal"

dishes["Bengalore"] = "pulihogare"

del dishes["Mysore"]
print(dishes)

print(dishes.keys())
print(dishes.values())

print("--------------------------")

# 17. nested dictionary : create a dictionary to store details of two of your fined, including their names,
# favorite subjects and favorite foods Access and print the favorite food of the one friends

nested_dict = {
    "friend1": {
        "name": "Aishu",
        "subject": "maths",
        "food": "curdRice"
    },
    "friend2": {
        "name": "keerthana",
        "subject": "Science",
        "food": "EggRice"
    }
}

print(nested_dict["friend1"]["food"])
print(nested_dict["friend2"]["food"])

print("--------------------------")

# 18. basic conditions : write a program to check if someone is eligible for a bus pass. id they are below
# 5 years the bus is free, if they are 60 year or older, their get a senior citizen discount.
# Otherwise their pay the full price

years = 80

if years < 5:
    print("The bus is free")
elif years >= 60:
    print("eligible for senior citizen discount")
else:
    print("They pay full price")


print("--------------------------")


# 19, Meal Time checker : create that checks the time of day (24-hour format) and prints whether its time for breakfast, lunch or dinner
# Breakfast : 8Am
# Lunch : 1Pm
# Dinner : 8pm
# If none of these times print"Its not meal time"


time = 20

if time == 8:
    print("its breakfast time")
elif time == 13:
    print("Its a Lunch time")
elif time == 20:
    print("Its a dinner time")
else:
    print("Its not meal time")


print("--------------------------")


# 20. Simple eligible check: Write a program, that check whether a person is eligible for library membership,
# if they are under 18, they get a student membership, if they are 60 or older, they get a senior citizen membership,
# otherwise, they get a regular membership

age = 80

if age < 18:
    print("get a student membership")
elif years >= 60:
    print("eligible for senior citizen membership")
else:
    print("get a regular membership")

print("--------------------------")


# 21. Basic Counting with while Loop
# Write a program that counts from 1 to 10 using a while loop.

i = 1

while i <= 10:
    print(i)
    i += 1

print("--------------------------")

# 22. Odd Numbers Printer
# Create a program that prints all odd numbers between 1 and 20 using a while loop.

i = 1

while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

print("--------------------------")

# 23. Ticket Booking Simulation
# Write a program that simulates a bus ticket booking system.
# The bus has 8 seats.
# Each time a seat is booked, the available seats decrease.
# When there are no seats left, the loop stops and displays the message:
# "All seats are booked."

seats = 8
while seats>0:
    user = int(input("Enter for seat booking: "))
    seats = seats - 1
    print("Reaming Seats: ", seats)

print("All seats is booked")

print("-----------------------------")
# 24. Countdown Timer
# Write a program that counts down from 10 to 1 using a while loop.
# After the countdown is over, print "Happy New Year!"

import time
i = 10

while i>=1:
    time.sleep(1)
    print(i)
    i-=1

print("Happy New Year")

print("--------------------------")


# 25. Multiples of 3
# Write a for loop that prints all multiples of 3 between 1 and 30.

for i in range(1, 31):
    if i % 3 == 0:
        print(i)

print("-----------------------------")

# 26. Sum of First 10 Numbers
# Write a program using a for loop that calculates the sum of numbers from 1 to 10.

count = 0
for i in range(1, 11):
    count += i
print("sum of the 10 numbers :", count)

print("-----------------------------")
# 27. Print Your Name Letter by Letter
# Write a program that takes your name as input and prints each letter of your name using a for loop.

name = input("Enter your name: ")
for letter in name:
    print(letter)


print("-----------------------------")
# 28. Count Vowels in a String
# Write a program that counts how many vowels are in a given string using a for loop

word = input("Enter a string: ").lower()
vowels = "aeiou"

count = 0

for letter in word:
    if letter in vowels:
         count += 1


print(letter)

print("-----------------------------")


# 29. List Manipulation
# Create a list of Kannada foods.
# Use list comprehension to create a new list where each food name is in uppercase.

list1 = ["idly", "Dose", "Palav", "Vada", "Sambar"]

# newlist = [expresstion for item in collection if condition]

new_list = [item.upper() for item in list1]
print(new_list)

print("-----------------------------")
# 30. Sum of Prices
# Create a dictionary of 5 items with their prices.
# Write a program that calculates the total price of all items using a for loop.

dict = {
    "pen": 10,
    "pencil": 5,
    "scale": 10,
    "shapnar": 5,
    "rabber": 5
}

total = 0

for _, values in dict.items():
    total += values

print("total product values of sum is: ", total)

print("-----------------------------")

# 31. List of Squares
# Create a list of numbers from 1 to 10.
# Use list comprehension to generate a list of their squares.

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ls = [item * item for item in list2]
print(ls)

print("-----------------------------")

# 32. Student Data Task
# Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student.
# Loop through the list and print each student's information.

dict_list = [
    {
        "name": "Aishu",
        "age": 22,
        "marks": 80
    },
    {

        "name": "Ammu",
        "age": 23,
        "marks": 85
    },
    {

        "name": "Raji",
        "age": 22,
        "marks": 70
    }
]

for i in dict_list:
    print(i["name"], "-", i["age"], "and", i["marks"])

print("-----------------------------")

# 33. Dictionary Comprehension
# Create a dictionary where the keys are Kannada cities and the values are their populations.
# Use dictionary comprehension to filter out cities with populations below 10 lakhs.

dictionary = {
    "Bengalore": 6,
    "mysore": 15,
    "mandya": 14,
    "ballary": 3
}

new_dict = {p: len(p) for p in dictionary}
print(new_dict)

print("-----------------------------")

# 34. Nested List Challenge
# Write a Python program that takes a list of lists (a 2D list) as input and:
# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.
# maticex =
# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]

rows = int(input("Enter a number of rows: "))
columns = int(input("Enter a numbers of columns: "))

martix = []

for i in range(rows):
    row = []
    for j in range(columns):
        x = int(input("Enter a numbers: "))
        row.append(x)
    martix.append(row)

print(martix)


def add(a, b):
    c = a+b
    print(f"sum of {a} and {b} is {c}")

add(10, 20)

