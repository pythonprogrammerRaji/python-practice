# # for loop
#
# # Level 1 – Easy
# #1. Print numbers from 1 to 10 using a for loop.
#
for i in range(1,11):
    print(i)

# print("-------------------------------")
#
#
# #2.  Print all even numbers between 1 and 20.
for i in range(1,21):
    if i%2==0:
        print(i)

# print("-------------------------------")
#
#
# #3. Print the elements of a list:
fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(fruit)

# print("-------------------------------")
#
# #4. Print each character of a string: "Python"

string = "Python"
for letter in string:
    print(letter)

# print("-------------------------------")
# # Level 2 – Medium
# #5. Print the multiplication table of 5 (from 5 × 1 to 5 × 10).
for i in range(1,11):
    print(f"5 * {i} = {i*5}")
#
#
# print("-------------------------------")
# #6. Calculate the sum of numbers from 1 to 50 using a for loop.
#
total = 0
for i in range(1,51):
   total = total + i

print(total)
#
#
#
#
#
#
# print("-------------------------------")
# #7. Print all numbers divisible by 3 between 1 and 30.
for i in range(1,31):
    if i%3==0:
        print(i)
# print("-------------------------------")
# # Level 3 – Challenge
# #8. Print a pattern:
# #
# # *
# # **
# # ***
# # ****
# # *****
#
for i in range(1,6):
    print("*" * i)
#
#
# print("-------------------------------")
#
#
# # Reverse a string using a for loop.
# # Example: "Python" → "nohtyP"
#
text = "Python"

for i in text[::-1]:
    print(i, end="")
#
# print("-------------------------------")
# # Find the largest number in a list using a for loop:
numbers = [12, 45, 2, 67, 34, 89, 23]
largest = numbers[0]
#
for num in numbers:
    if num > largest:
        largest=num
print(largest)

#
# print("======================================================")
#
# # Level 1 – Basic
#1. Print numbers from 1 to 15 using a for loop.

for i in range(1,16):
    print(i)
#
#
#
# print("*************************************************")
#
# #2. Print all odd numbers between 1 and 20.
#
for i in range(1,21):
    if i%2!=0:
        print(i)

#
# print("*************************************************")
# #3. Find the sum of all numbers in a list → [10, 20, 30, 40, 50].
#
#
l = [10, 20, 30, 40, 50]
total = 0

for num in l:
    total = total+num
print(total)
#
# print("*************************************************")
#
# #4. Print each character of the string "Python".
#
string = "java"
for letter in string[::-1]:
    print(letter)
#
# print("*************************************************")
#
# #5. Print the multiplication table of 5 using a for loop.
#
for i in range(1,11):
    print(f" 5 x {i} = {i*5}")
#
# print("********************** level 2 ***************************")
# # Level 2 – Intermediate
# #
# #6. Count how many vowels are in the string "education".
#
#
s ="education"
count = 0
vowels = "aeiouAEIOU"
for char in s:
    if char in vowels:
        count += 1
#
# print("numbers of vowels",count)
#
# print("*************************************************")
#
# #7. Print all elements of a list in reverse order (without using reverse function).
#
list = [10, 20, 30, 40, 50, 60]
ll = []
for l in list[::-1]:
    ll.append(l)
print(ll)
#
# print("*************************************************")
#
#
# #8. Find the factorial of a number using for loop.
#
fact = 1
i = 1
for i in range(1,6):
    fact *= i
print(fact)
#
# print("*************************************************")
#
#
# #9. Print all numbers between 1 and 50 that are divisible by 3 and 5.
#
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(i)

# print("*************************************************")
#
#
#
#
#
# #10. Given a list [1, 2, 3, 4, 5, 6, 7], print only the odd numbers.
#
list = [1, 2, 3, 4, 5, 6, 7]

for i in list:
    if i%2!=0:
        print(i)
#
# print("********************** level 3 ***************************")
# #Level 3 – Challenge
# #11. Print the Fibonacci sequence for first 10 numbers using for loop.
n = 10
a = 0
b = 1

print(a, b, end=" ")

for i in range(2,n):
    c = a + b
    print(c, end=" ")
    a=b
    b=c
# print("*************************************************")
#
# #12. Write a program to find the maximum number in a list using for loop.
#
list1 = [10, 2, 34, 76, 82, 45]
largest = list1[0]

for num in list1:
    if num > largest:
        largest=num
print(largest)

# print("*************************************************")
#
# # Count the frequency of each character in a string.
#
s1 = "python"
for char in set(s1):
    print(f"{char} : {s1.count(char)}")
#
# # Use nested loops to print a pattern:
# #
# # *
# # **
# # ***
# # ****
# # *****
# #
#
for i in range(1,6):
    print("* " * i)
# #
# # Given a dictionary →
student = {'name': 'Rajeshwari', 'age': 22, 'course': 'MCA'}
# # Print each key and value in separate lines using a for loop.
#
for keys, values in student.items():
    print(f"{keys} : {values}")
#
#
#


print("====================== While loop ========")

# Basic Level:
#1. Print numbers from 1 to 10 using a while loop.

i = 1

while i<=10:
    print(i)
    i += 1
print("-----------------------------------")
#2. Print all even numbers between 1 and 20.
i = 1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

print("-----------------------------------")
#3. Find the sum of numbers from 1 to 50 using a while loop.

i = 1
sum = 0

while i<=50:
    sum += i
    if i == 50:
        print("Sum :",sum)
    i+=1

print("-----------------------------------")
#4. Print the multiplication table of 7 using a while loop.
i = 1

while i<=10:
    print(f"7X{i}={i*7}")
    i+=1
print("-----------------------------------")
# Intermediate Level:
# Ask the user to enter numbers repeatedly until they enter 0, then print the total sum.

total = 0

while True:
    num = int(input("Enter the number: "))
    if num == 0:
        break
    total += num
print("Total", total)

# Write a program to reverse a number (e.g., 1234 → 4321) using a while loop.

num = int(input("Enter num: "))
rev = 0

while num>0:
    digits = num % 100
    rev = rev * 10 + digits
    num //= 10
print("reversed num",rev)



# Print the digits of a number in separate lines using while loop.

num = int(input("Enter num: "))

while num > 0:
    digits = num % 100
    print(digits)
    num //= 10



# Write a program to count how many digits are in a given number.

number = 1234     # initialized
count = 0         # count now empty

while number>0:    #number must be grater than 0
    number = number // 10    # number can divide by 10 for remove th last digit
    count+=1
    print(f"count {number} => {count}")

# 🔐 Advanced / Logic:
# ATM Simulation:
# PIN = 1234
# Give user 3 attempts to enter the correct PIN
# If correct → print “Access Granted”
# If wrong after 3 tries → print “Card Blocked”
#
# pin = 1234
# trails = 1
#
# while trails<=3:
#     user_input =int(input(f"Trails {trails} | pin : "))
#     if user_input == pin:
#         print("Access Granted")
#         break
#     else:
#         trails+=1
# if trails > 3:
#     print("Card Blocked")
#
#
# #10. Guessing Game:
# # Randomly pick a number between 1–10 (use import random)
# # Ask the user to guess until they get it right
# # Count how many tries they took
#
# import random
#
# secrets = random.randint(1, 10)
# tries = 0
#
# while True:
#     guess = int(input("Enter the number (1-10): "))
#     tries += 1
#     if guess == secrets:
#         print(f"🎉 Correct! You guessed it in {tries} tries.")
#         break
#     else:
#         print("wrong Guess , try again")
