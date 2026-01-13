# While loop: the program execution repeatedly as loge as condition is True

# While Loop Summary (Quick Revision)
# Concept           Description          	                            Example
# Initialization: 	Define a starting variable before the loop	         i = 1
# Condition : 	    Loop runs while condition is True	while            i <= 5:
# Update   :	    Change variable to avoid infinite loop	             i += 1
# Break      	    Exit loop immediately	                             if x == 0: break
# Continue	        Skip current iteration	                             if x == 3: continue
# 1. count the number 1 to 10 :
i = 1  # initalization
while i <= 10:  # condition
    if i == 6:
        break  # exit the loop
    print(i)  # print the output
    i += 1  # to stop the infinity loop
print("---------------------------------")
# 2. print the numer 1 to 10 reverse order
i = 10
while i >= 1:
    print(i)
    i -= 1
print("---------------------------------")

# 3.to attempt student pass the exam until they pass and he is attempted 100 time then gave up

is_fails = True
i = 1
while is_fails:
    if i % 2 != 0:
        i += 1
        continue
    print("Attempt", i)
    i += 1
    if i > 10:
        break
print("Give up")
print("---------------------------------")
# 4. to print the name how many iteration that times print the name ex: 1st iteration one time name print, 2nd iteration two time peint

i = 0
while i <= 10:
    x = 0
    while x < i:
        print("Aishu", end=" ")  # end="" its print all in one line
        x += 1
    print(" ")
    i += 1

# 5. check the atm pin is correct the user enter pin or not to given 3 trials using the while loop
pin = 1234
trials = 1

while trials <= 3:        # using while loop we can give user to enter the pin in three times
    input_pin = int(input(f"Trial {trials} | Pin : "))
    if input_pin == pin:  # using if condition user have one chance to enter the pin
        print("CORRECT pin access granted 👍")
        break
    else:
        print("INCORRECT pin 🙄")
        trials += 1
if trials > 3:
    print("your code is blocked too many attempts")


# Practice Test — Intermediate to Advanced While Loop Questions
# Try these one by one (no need to rush 💡):
# 1️⃣ Count digits and sum of digits in a number
# Example: 123 → Count = 3, Sum = 6

num = 123
total = 0
count = 0

while True:
    if num:
        digits = num % 100
        num //= 10
        print("count: ", digits)
    total += num
    print("Total",total)


# 2️⃣ Print all multiples of 3 between 1 and 100 (use while loop)

number = 1

while number <= 100 and number % 3 == 0:
    print(f"All multiples of 3: {number}")
    number += 1

# 3️⃣ Find factorial of a number using while loop
# Example: 5! = 120

i = 1
fact = 1
while i <= 5:
    fact *= i
    print(f' {i} Fact is: {fact}')
    i += 1

# 4️⃣ Check whether a number is palindrome or not
#
# Example: 121 → palindrome
#
text = (input("enter a string: "))

while True:
    if text == text[::-1]:
        print(f'{text} is palindrome')
        break
    else:
        print(f'{text} is not a palindrome')
        text += 1


# 5️⃣ Count how many even and odd digits are present in a given number

number = int(input("Enter the counted number: "))
count = 0

while number>0:
    number = number // 10
    count += 1
print(f"{number} : count => {count}")

# 6️⃣ Display Fibonacci series up to n terms using while loop
# Example: 0, 1, 1, 2, 3, 5, 8...

n = 1
a = 0
b = 1

print(a, b, end=" ")

while n<=10:
    c = a+b
    print(c, end=" ")
    a = b
    b = c
    n+=1
#
# 7️⃣ ATM logic (you already did — ✅ keep as reference)
pin = 2345
trails = 1

while trails <= 3:
    user_pin = int(input(f"Trails {trails} | pin: "))
    if user_pin == pin:
        print("Access is correct")
        break
    else:
        print("The incorrect pin, try again")
        trails+=1
if trails > 3:
    print("you attempted so many trails, code is blocked, Try after some time")

# 8️⃣ Guessing game (✅ also done, revise with random)

import random

secrets = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Enter the guessing number: "))
    tries += 1
    if guess == secrets:
        print("Guessing number is Correct 🎉")
        break
    else:
        print("Incorrect")

# 9  Find the largest digit in a given number
# Example: 3492 → 9

exam = [3, 4, 5, 9]
max_largest = exam[0]

while True:
    if exam in max_largest:
        max_largest = exam
        exam+=1

    print(max_largest)



