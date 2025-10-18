# operator : the operator is symbol the perform some task using oen operator with two operands

# 1.arithmetic operator :
# num1 = int(input("Enter the first Number: "))
# num2 = int(input("Enter the second Number: "))
#
# print("Addition", num1 + num2)
# print("Subtract", num1 - num2)
# print("multiplication", num1 * num2)
# print("division", num1 / num2)
# print("flore division", num1 // num2)
# print("modulo", num1 % num2)
# print("exponent", num1 ** num2)

# 2. relational or compression operator

a = 10
b = 100
print("greater than :", a > b)  # greater than F
print("less than : ", a < b)  # less than    T
print("greater than equal to: ", a >= b)  # greater than equal to   F
print("less than equal to: ", a <= b)  # less than equal to    T
print("equal to: ", a == b)  # equal to  F
print("Not equal to: ", a != b)  # Not equal to   T

# 3.Assignment Operator (=)

x = 10
x *= 3  # x = x * 3 => 30
print(x)

# 4. logical operator : used to check the condition in logically and return the output as boolean value (True or False)
# And : if both side is true then its true
# or : either one sde is true is true
# not : opposite for boolean value

a = 10
b = 20

print(a<b and b>a)
print(a!=b or a>b)
print(not(a>b))

print("-----------------------")

# 5. Membership operator (in, not in) : its given specific given text there or not in given string

text = "This is python"
print("python" in text)
print("Java" not in text)
print("5" in text)


