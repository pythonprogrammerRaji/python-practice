# function -> function is block of code that runs only when you call it , so we can resue the logic to call the function name anywhere

import math
# 1.
def add(a,b):
    return  a+b

s1 = add(10, 20)
print("Sum two number", s1)

# 2.
def even_or_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(2))
print(even_or_odd(7))

def square(x):
    return x*x

square1 = square(5)
print(f"The square  is ", square1)

def positive(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"
print(positive(-1))

def greater(n1, n2):
    if n1>n2:
        return n1
    elif n1<n2:
        return n2
    else:
       return "Both are equals"

print(greater(10, 20))

# function Test
#1. Write a function that takes two numbers and returns their sum

def sumfunction(a,b):
    return a+b

s = sumfunction(1, 2)
print(s)


#2.Write a function that: takes a number returns "Even" or "Odd"
def even_or_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(2))
print(even_or_odd(7))

#3. Write a function that takes a number returns square and cube
# def cube(num):
#     if num * num:
#         # return square
#     elif

#4. Write a function that takes one number returns "Positive", "Negative" or "Zero"
def positive(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"
print(positive(-1))

#5.  Find greatest of three numbers
# Write a function that takes 3 numbers returns the greatest number

def greatest(a, b, c):
    if a>b and a>c:
        return a
    elif a<b and b>c:
        return b
    elif a<c and b<c:
        return c
    else:
        return "all are equal"

g = greatest(10, 20, 30)
print("greatest  number is", g)



#6.  Simple calculator
# Write a function that takes a, b, and operator (+, -, *, /) returns the result

def calculator(a, b, operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b

c = calculator(10, 20, "+")
print("the operator is", c)

#7. Check eligibility to vote
# Write a function that takes age returns "Eligible" or "Not Eligible"

def vote(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not eligible"

age = vote(12)
print(age)

#8. Print numbers from 1 to n
# Write a function that takes n prints numbers from 1 to n

def number(n):
    for i in range(1,n+1):
        print(i)

num = number(10)
print(num)

print("--------------------Advanced topic-------------")
# Advanced topic
#1.  Write a function that takes name and city.
# City should be default = "Bangalore"
# Print: Name lives in City

def live(name, city="Bangalore"):
    print(f"{name}, lives in {city}")

live("Aishu")

#2.  Write a function bill_amount(price, tax=5)
#Return total amount after tax

def bill_amount(price , tax = 5):
    return price + (price * tax)/100
bill = bill_amount(25)
print("tax include total amount",bill)

# 3️⃣ Write a function power(base, exp=2)
# If exponent not given, return square
# If given, return power

def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 3))

# B. *args (Multiple Arguments)
# Write a function that takes any number of integers and
# Returns their sum

def add(*num):
    return sum(num)

print(add(1, 2, 3, 4, 5))

# 5️⃣ Write a function that takes any number of numbers and
# Returns the largest number

def largest(*number):
    return max(number)

print(largest(10, 30, 20, 5))


# 6️⃣ Write a function that accepts *student marks using args
# Return average marks

def average(*marks):
    return sum(marks) / len(marks)

avg = average(10, 20, 30, 40, 50)
print(f"Average number is {avg}")

# **kwargs (Keyword Arguments)
# 7️⃣ Write a function that accepts student details using **kwargs
# Print each key and value on new line
# Example input:
# name="Rajeshwari", age=22, course="MCA"
def student(**details):
    for  key, value in details.items():
        print(key , ":" , value)

(student(name="Rajeshwari", age =22, course="MCA"))


# 8️⃣ Write a function that accepts employee details
# If salary exists → print salary
# Else → print "Salary not provided"

def employee(**emp):
    if "salary" in emp:
        print("salary", emp["salary"])
    else:
        print("Salary not provided")

employee(name="Radhakrishna", empId= 1001, salary= 10000)

# LAMBDA FUNCTIONS (Important)
# 9️⃣ Write a lambda function to
# Find square of a number

square=  lambda x:x*x
print(square(5))


# 🔟 Write a lambda function to
# Check even or odd

even_odd = lambda a: "Even" if a%2==0 else "Odd"
print(even_odd(4))


# 1️⃣1️⃣ Write a lambda function that
# Returns greater of two numbers

greate = lambda a,b : a if a>b else b
print(greate(10, 20))

# 1️⃣2️⃣ Using lambda + list
# Square all numbers in [1,2,3,4,5]

nums = [1,2,3,4,5]
sqrt = list(map(lambda x:x*x, nums))
print(sqrt)
