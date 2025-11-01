# 1. check the number is even or odd

n = int(input("Enter the N: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

print("-------------------------")

# 2.program to find the sum of first N number

n = int(input("Enter the N: "))
sum = 0

for i in range(1, n+1):
    sum += i
print("Sum", sum)

print("-------------------------")

# 3. Factorial of a number

n = int(input("Enter the  number: "))
fact = 1

for i in range(1, n+1):
    fact *= i
print("fact is", fact)
print("-------------------------")

# 4. palindrome ot not

test = input("enter the text: ")

if test == test[::-1]:
    print(f"{test} Palindrome")
else:
    print(f"{test} not a Palindrome")

print("-------------------------")

# 5. Simple Multiplication Table

num = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

print("-------------------------")

# 6. Largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a>b:
    print("a is largest number b")
else:
    print("b is largest number a")

print("-------------------------")

# 7. check positive, negative or zero

num = int(input("Enter the number: "))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is equal to zero")

print("-------------------------")

# 9. count a vowels in a string

test = input("Enter the string: ")
vowels = "aeiouAEIOU"
count = 0

for char in test:
    if char in vowels:
        count += 1

print("Number is Vowels: ", count)

print("-------------------------")

# 10. Reverse a number

test = input("Enter the string: ")
reverse = test[::-1]
print("Reversed string: ",reverse)

print("-------------------------")

# 11. find the maximum element in list
number = [5, 9, 2, 7, 1]
max_num = number[0]

for num in number:
    if num > max_num:
        max_num = num

print("maximum number is: ", max_num)

print("-------------------------")

# 12. check leap year or not

year = int(input("Enter the year: "))

if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is leap")
else:
    print(f"{year} is not leap")

# 11. find the minimum element in list
number = [5, 9, 2, 7, 1]
min_num = number[0]    # the imaging the first number is small

for num in number:    # loop all number in list
    if num < min_num:      # check the current number ib minimum with other number
        min_num = num        # its true update the min_number

print("maximum number is: ", min_num)


# min_num = 5
#
# check number :
# compare 9 < 5 (F)
# compare 2 < 5 (T) , now min-num = 2
# compare 7 < 2 (F)
# compare 1 < 2 (T)   now min_num = 1