# List Questions

# Q1: Create a list of 5 numbers. Print the sum, maximum, and minimum.

list = [1, 2, 3, 4, 5]
print("the sum of list is", sum(list))
print("the maximum number in list is", max(list))
print("the minimum number in list is", min(list))

print("-------------------------------")

# Q2: Take a list of names from the user (comma separated) and print them sorted alphabetically.

name_input = input("Enter the name:")

# to split the string to list separately
name_list = name_input.split(",")

# to remove the duplicate using set and sorted in alphabetically
sorted_list = sorted(set(name_list))

print("the sorted name in listr is", sorted_list)

print("-------------------------------")

# Q3: Remove duplicates from a list [1, 2, 2, 3, 4, 4, 5] and print the new list.

number = [1, 2, 2, 3, 4, 4, 5]

unique_number = []

for num in number:
    if num not in unique_number:
        unique_number.append(num)

print("The unique number is ", unique_number)

# print("another way of remove the duplicates")
#
# number = [1, 2, 2, 3, 4, 4, 5]
#
# new_number = list(set(number))
#
# print(new_number)

print("-------------------------------")

# Q4: Given list1 = [1, 2, 3] and list2 = [4, 5, 6], combine them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# another way
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)


print("-------------------------------")

# Q5: Reverse the list [10, 20, 30, 40, 50] without using the reverse() method.

list = [10, 20, 30, 40, 50]
rev = 10
rev1 = rev + 40
rev2 = rev + 30
rev3 = rev + 20
rev4 = rev + 10

rev_list = []
rev_list.append(rev1)
rev_list.append(rev2)
rev_list.append(rev3)
rev_list.append(rev4)
rev_list.append(rev)

#another way
list11 = [10, 20, 30, 40, 50]

reversed_list = list11[::-1]
print("the reversed number is",reversed_list)

print(rev_list)

# with reverse() using

# list.reverse()
# print(list)
