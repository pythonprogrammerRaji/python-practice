# # conditions : its a decision control statement that used to perform the different actions based on different conditions
#
# # 1. if statement examples
# # Check given number is less than or equal to 10
# x = int(input("Enter a number: "))
#
# if x <= 10:
#     print("x is less than or equal to 10")
#
# print("-------------------------")
#
# # 2. elif statement examples
# # check the time now is eating time or not
#
# time = 2
#
# if time == 8:
#     print("its is breakfast time")
# elif time == 13:
#     print("its is lunch time")
# elif time == 20:
#     print("its is dinner time")
# else:
#     print("Its not time to eat")
#
# print("-------------------------")
#
# # 3. else statement examples
# # check the given number is even or odd
#
# num = int(input("Enter the number: "))
#
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is a odd")

# 4. using operation to perform the condition statements
# check the student attendance and paying the college fees to allowing internals

# attendance = 65
# fess = 10000
#
# if attendance <= 75 or fess == 10000:
#     print("the student allowing for the internals")
# elif attendance < 75 and fess == 8000:
#     print("the student not allowing for the internals ")
# else:
#     print("the student attendance less and fees also not payed")

print("-------------------------")

# 4. Nested if statement examples
# Ticket booking project using nested if

gender = input("Enter the gender: ")
age = int(input("enter the age: "))

if gender=="female":
    print("The ticket is free")
else:
    if age<5:
        print("the ticket is free")
    elif age<=12:
        print("the ticket is child discount, half ticket")
    elif age>=60:
        print("the ticket is discount for senior citizen")
    else:
        print("the ticket is full")


