# list is a datastructures and collection of element, its ordered and mutable (changeable)

# Creating the list
list = ["Bru", "Sugar", "milk"]
print(list)

# accesing the list
print(list[0])
print(list[1])
print(list[2])

# modifiaing the list
list[0] = "sunrise"
print(list)

# list methods
# 1. append() : to add the element at end of the list
list.append("Biscuits")
print(list)

# 2. insert() : to insert the lement at paricular postion using index
list.insert(1, "3roses")
print(list)

# 3. remove() : to remove the particular element
list.remove("sunrise")
print(list)

# 4. pop() : remove the element at end of the list
list.pop()
print(list)

# 5.count() : count the number of same element in list
list.count("Bru")
print(list)

# 6.Extend() : extend used add element two or more element in list
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
list1.extend(list2)
print(list1)

# 7. copy() : copy the all element in the list
list2.copy()
print(list2)

# 8. index() : index is identify the value of element present at partcular insdex
print(list1[0])

# 9. reversed() : to reverse the all element in list
list2.reverse()
print(list2)

# 10. sort() : arraging the element in ascending order
num = [50, 20, 40, 10, 30]
num.sort()
print(num)

# list Functions
# 1. len() : return the length of the list
values = [10, 20, 30, 40, 50]
# print(values.len())

# 2. sum() : total all element in a list
# print(values.sum())

# 3. max() : return the maximum value in list
# print(values.max())

# 4. min() : return the minmum element in a list
# print(values.min())

# Nested list : list with another list
nest_list = [1, 2, 3, 4, 5,[10, 20, 30, 40, 50]]
print(nest_list)
print("----------------------------------")

# slicing
# 1,
num = [10,20,30,40,50,60,70]
print(num[2:5])
print(num[:4])
print(num[-3:])
print(num[0:7:2])
print(num[::-1])

print("----------------------------------")
# 2.
fruits = ["apple", "banana", "cherry", "date", "fig", "grapes"]
print(fruits[1:4])
print(fruits[:3])
print(fruits[3:])
print(fruits[-4:-1])
print(fruits[0:5:2])

print("----------------------------------")
# 3.
mixed = [1, "hello", 3.14, True, "World",10]
print(mixed[1:4])
print(mixed[2:])
print(mixed[0:6:2])
print(mixed[-3:-1])
print(mixed[::-1])

print("----------------------------------")
# 4.
names = ["Raji", "Aishu", "Chandu", "Kavya", "Keerthana"]
print(names[1:3])
print(names[1:])
print(names[-2:])
print(names[1:4:2])
print(names[::-1])




