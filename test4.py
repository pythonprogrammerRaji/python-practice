# 1.Basic Arithmetic & Assignment
# Write a program that:
# Takes two integers a and b.
# Prints the result of
# addition, subtraction, multiplication, division (float), floor division, modulo, and exponent (a ** b).
# Then update a using a += b, a -= b, a *= b and print a after each step.

a = 10
b = 3

print("Addition a and b", a + b)
print("Subtraction a and b", a - b)
print("multiplication a and b", a * b)
print("division a and b", a / b)
print("floor division a and b", a // b)
print("modulo a and b", a % b)
print("exponent a and b", a ** b)

a += b
print("add_assign", a)
a -= b
print("sub_assign", a)
a *= b
print("multiple_assign", a)

print("----------------------------------------")

# 2. Simple Calculator
# Ask the user to:
# Enter two numbers.
# Enter an operator (+, -, *, /).
# Use if-elif to perform the correct calculation and print the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter a operator: ")

if operator == "+":
    print("the addition two numbers", num1 + num2)
elif operator == "-":
    print("the subtract two numbers", num1 - num2)
elif operator == "*":
    print("the multiplication two numbers", num1 * num2)
elif operator == "/" and num2!=0:
    print("the division two numbers", num1 / num2)
elif operator == "/" and num2==0:
    print("can't divide by zero")
print("----------------------------------------")

# 3. Comparison & Logical
# Take an integer from the user and check:
# If it is between 10 and 50 (inclusive).
# If it is NOT a multiple of 5.
# If it is even OR greater than 100.
# Print a message for each condition.

value = int(input("Enter a number: "))

if 10 <= value <= 50:
    print(f"the {value} is between 10 to 50")
if value%5!=0:
    print(f"the {value} is not multiple 5")
if value % 2 == 0 or value > 100:
    print(f"the {value} is even or greater than 100")

print("----------------------------------------")

# 4. Swap Without Third Variable
# Input two numbers and swap their values using only arithmetic operators (+ and - or * and /) and print the swapped result.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before swapping first number", a)  # 10
print("Before swapping second number", b)  # 3

a = a + b
b = a - b
a = a - b
print("After swapping first number", a)  # 3
print("After swapping second number", b)  # 10

print("----------------------------------------")

# 5. Bitwise Bonus (optional)
# Ask the user for two integers and:
# Print the result of a & b, a | b, a ^ b, ~a, and a << 1, a >> 1.

a = int(input("Enter the 1st no: "))
b = int(input("Enter the 2nd no: "))

print("the result of a & b is", a & b)
print("the result of a | b is", a | b)
print("the result of a ^ b is", a ^ b)
print("the result of ~a is", ~a)
print("the result of a << 1 is", a << 1)
print("the result of a >> 1 is", a >> 1)