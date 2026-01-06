# logical operator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > 10 and num2 > 10:
    print("Both numbers are greater than 10")

if num1 < 5 or num2 < 5:
    print("Both numbers are less than 5")

if not num1 > num2:
    print("the first number is not greater than the second number")

# 2.comparison operator
age = int(input("Enter the your age: "))
if age >= 18:
    print("your are an adult")
elif age <= 18:
    print("your are a minor")

# 3. Membership operator

text = input("Enter the string")

print("a" in text)
print("python" not in text)

print("-------------------------------")
# 4. Bitwise operator

a=2
b=8

print(a & b)
print(a | b)
print(a ^ b)
ans1 = a << 2
print("a two position left shift",ans1)
ans2 = b >> 2
print("b two position right shift",ans2)

