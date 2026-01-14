# for loop : the for loop is used to iterate over a sequence like (list, tuple, string or range) and execute
# a block of code repeatedly for each element

# 1. the for loop is two type
# -> for in sequence : the sequence perform tha task in list, tuple and string etc
# -> for in range() : the range perform the task in given range of number

#1. -> for in sequence :
# list
fruits = ["apple","banana","mango","grapes"]

for fruit in fruits:
    print(fruit)

# tuple
bag = ("red","blue","green")
for balls in bag:
    print(f"{balls} ball")

# string
name = "aishu"

for letter in name:
    print(letter)

# to print the element list and in their using enumerate() function

name1 = "RadhaKrishna"
for index,letter in enumerate(name1):
    print(f"{letter} is in {index}th index")

print("----------------------")
#2. -> for in range()

for i in range(1,11):
    print(i, end=" ")

for i in range(-10, 1):
    print(i , end="")

print("----------------------")

# use brake statement is for loop

cities = ["Bengalore", "Mysure", "Hubbali", "Mangalore"]

for city in cities:
    if city == "Hubbali":
        print(f"Found {city}")
        break
    print(city)
print("----------------------")
# use continue statement is for loop

cities = ["Bengalore", "Mysure", "Hubbali", "Mangalore"]

for city in cities:
    if city == "Hubbali":
        continue
    print(city)


print("----------------------")
# print the table for 2
for i in range(1,11):
    print(f"2X{i}={i*2}")

print("----------------------")
# print the table 2 to 10 using nested for loop
for i in range(2,11): # i is tabel of number 2, 3 ,4, 5 etc iX1=j*2
    for j in range(1,11): # j is number of table 1, 2, 3, 4, 5,etc    iXj=2*j
        print(f"{i} X {j} = {i*j}")

print("----------------------")
# Print multiplication table of 1 to 3
for i in range(1,4):
    for j in range(1,4):
        print(i,"*" ,j, "=", i*j)
print("----------------------")
# Using for loop with if , check the given even number using for and if

for i in range(1,11):
    if i % 2 == 0:
        print(i)


