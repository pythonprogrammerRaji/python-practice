# level1 : Basic
# Write a program to check whether a number is positive, negative, or zero.
number = int(input("Enter the number: "))

if number > 0:
    print("The given number is positive")
elif number < 0:
    print("The given number is negative")
elif number == 0:
    print("Number is equal to zero")
else:
    print("invalid number")



# Write a program that checks whether a given number is even or odd.

num = int(input("Enter a number: "))
if num%2==0:
    print(f" {num} is even")
else:
    print(f"{num} is odd")

# Write a program to find the largest of two numbers.

x = int(input("Enter the 1st no: "))
y = int(input("Enter the 2nd no: "))

if x>y:
    print("x is Largest number than y")
elif x<y:
    print("y is largest number than x")
else:
    print("x and y are equal numbers")


# Write a program to check whether a person is eligible to vote or not (age ≥ 18).

age = int(input("Enter your age: "))

if age>=18:
    print("You are  eligible for vote")
else:
    print("Your are not eligible for vote")

# Level 2 – Intermediate
#
# Write a program to find the largest among three numbers using if-elif-else.

a = int(input("Enter the 1st no: "))
b = int(input("Enter the 2nd no: "))
c = int(input("Enter the 3rd no: "))

if a>b and a>c:
    print("a is Largest number")
elif b>c:
    print("b is largest number")
else:
    print("c is largest number than a and b")


# Write a program to check if a year is a leap year or not.

year = int(input("Enter the year: "))

if (year%4==0 and year%100!=0) or year%400==0:
    print(f" the {year} is leap year")
else:
    print(f" the {year} is not leap year")






# Write a program that takes marks of a student and prints the grade:
# Marks >= 90 → A
# Marks >= 80 → B
# Marks >= 70 → C
# Marks >= 60 → D
# Marks < 60  → F

Marks = int(input("Enter the student Marks: "))

if Marks >= 90:
    print("A")
elif Marks >= 80:
    print("B")
elif Marks >= 70:
    print("C")
elif Marks >= 60:
    print("D")
elif Marks < 60:
    print("F")

# Write a program to check whether a given number is divisible by both 5 and 11.

div = int(input("Enter the number: "))

if div%5==0 and div%11==0:
    print(f"The {div} is divisible only 5 and 11")
else:
    print(f"The {div} is not divisible by both 5 and 11")

# Level 3 – Challenge
#
# Write a program to input a character and check whether it is a vowel or consonant.

character = input("Enter the character: ").lower()
# vowels = "aeiou"


if character in "aeiou":
    print(f"The  {character} is Vowels")
else:
    print(f" The {character} is Consonants")

# Write a program to check whether a given year is a century year (like 1900, 2000, etc.).

year = int(input("Enter the year: "))
if year%100==0:
    print("The given year is century year")
else:
    print("The given year is not a century year")


# Write a program to input three angles and check whether they form a valid triangle or not.

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

if angle1>0 and angle2>0 and angle3>0 and (angle1+angle2+angle3 == 180):
    print('The given angles is valid triangle')
else:
    print('The given angles is not valid triangle')


# Write a program to input marks in three subjects and print whether the student passed or failed (pass only if all subjects ≥ 35).

subjects1 = int(input("Enter the subject1 marks: "))
subjects2 = int(input("Enter the subject2 marks: "))
subjects3 = int(input("Enter the subject3 marks: "))
marks = subjects1+subjects2+subjects3

if marks >= 105:
    print("The student is pass")
else:
    print("the student us fails")