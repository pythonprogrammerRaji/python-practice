# # sets {]: the set is a collections of element unique with unordered and mutable,reindexing and set do not
# # allow the duplicate elements
#
# s = {1, 2, 3, 1, 2, 3, 5, 6, 4}
# print(type(s))
# print(s)
#
# print("---------------set operations----------------------")
# # set operations
# # 1. Union (|) : return all element in both the sets
# s1 = {1, 2, 3, 4, 5, 3, 2}
# s2 = {5, 6, 7, 8, 2, 1, 3, 9}
# print(s1 | s2)
#
# # 2.Intersection (&) : To return the same element only in both sets
# print(s1 & s2)
#
# # 3. difference (-) : To rerun only one set present the element not have another
# print(s1 - s2)
#
# print("---------------set Method----------------------")
# # set methods
# # 1. add() : to add the element in a set
# st = {"apple", "ball", "cat"}
# st.add("dog")
# print(st)
#
# # 2. remove() : to remove the particular element is a set
# st.remove("cat")
# print(st)
#
# # 3. discards () : to removed element not exists in set
# st.discard("ball")
# print(st)
#
# # 4.pop () : to remove any element in a set
# st.pop()
# print(st)
#
# # 5.clear () : clear all the element in set ans return the empty set
# st.clear()
# print(st)
#
# #test
# # Practice 1: Add a New Fruit
# # Create a set with {"apple", "banana"}.
# # Add "mango" and print the set.
#
# fruit = {"apple","banana"}
# fruit.add("mango")
# print(fruit)
#
#
# # 📝 Practice 2: Avoid Duplicates
# # Create a set colors = {"red", "blue"}.
# # Add "red" again and print the set.
# # 👉 Observe that nothing changes.
# colors = {"red","blue"}
# colors.add("red")
# print(colors)
#
#
#
#
# # 📝 Practice 3: Build a Set from User Input
# # Start with an empty set.
# # Ask the user to enter three different numbers (one by one) and add each number using .add().
# # Finally print the set.
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# ss = set()
# ss.add(num1)
# ss.add(num2)
# ss.add(num3)
# print(ss)
#
#
#
# # 📝 Practice 4: Add Inside a Loop
# # Given a list: nums = [1, 2, 2, 3, 4, 4, 5]
# # Create an empty set unique_nums.
# # Use a for loop and .add() to insert each number.
# # Print unique_nums to see only unique numbers.
#
# nums = [1, 2, 2, 3, 4, 4, 5]
# unique_nums = set()
#
# for num in nums:
#     unique_nums.add(num)
#
# print(unique_nums)
import math

# 1️⃣ Remove and Discard
# Create a set {10, 20, 30, 40}
# a) Remove 30 using remove()
# b) Try to remove 50 using remove() and see what happens
# c) Try to discard 50 using discard() and see the difference
# Hint: remove() raises an error if the element isn’t there, but discard() won’t.

setA = {10, 20, 30, 40}

setA.remove(30)
print(setA)
# setA.remove(50)   # the remove raise the keyerror
# print(set1)
setA.discard(50)      # the discard give the output skip the error
print(setA)


# 2️⃣ Union and Intersection
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# Print the union of set1 and set2
# Print the intersection of set1 and set2

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union",set1 | set2)
print("intersection", set1 & set2)


# 3️⃣ Difference
# A = {1,2,3,4}
# B = {3,4,5,6}
# Print elements present in A but not in B.
# Print elements present in B but not in A.
A = {1,2,3,4}
B = {3,4,5,6}
print("elements present in A but not in B.",A-B)
print("elements present in B but not in A.",B-A)



# 4️⃣ Set Comprehension
# From a list nums = [1,2,3,4,5]
# Build a set of squares {1,4,9,16,25} using a set comprehension.
nums = [1,2,3,4,5]
squares = {x*x for x in nums}
print(squares)

# for x in nums:
#     ss = x*x
#     sets = set(ss)
#
# print(sets)

#
# From nums = [1,2,3,4,5,6,7,8,9,10], create a set of even numbers only.
# 👉 Expected: {2,4,6,8,10}
nums1 = [1,2,3,4,5,6,7,8,9,10]
even = {x for x in nums1 if x%2==0}
print(even)



# From the same list, create a set of squares of odd numbers.
# 👉 Expected: {1,9,25,49,81}

odd_square = {x*x for x in nums1 if x%2!=0 }
print(odd_square)
#
# From a string "hello", build a set of characters (observe how duplicates vanish).
# 👉 Expected: {'h','e','l','o'}

string = "hello"
str = set(string)
print(str)