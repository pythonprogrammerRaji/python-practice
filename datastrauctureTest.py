# Level 1 — Easy
#1.  Write a Python program to find the sum and average of all numbers in a list.

list1 = [10, 20, 30, 40, 50]
total = sum(list1)
print("sum of the number is: ",total)
avg = sum(list1)  / len(list1)
print("The average number is: ",avg)

print("-----------------------------------")
#2.  Given a tuple (2, 4, 6, 8, 10), print the first and last elements.

tuple = (2, 4, 6, 8, 10)

print("The first element is tuple", tuple[0])
print("The last element is tuple", tuple[-1])

print("-----------------------------------")

#3.  Convert this list into a set and print:
# fruits = ['apple', 'banana', 'apple', 'cherry', 'banana']
# What will the output be? Why?

fruits = ['apple', 'banana', 'apple', 'cherry', 'banana']
list_set = set(fruits)
print(list_set)   # here in the list apple and banana repeated twist so when convert the list into set the repeated output is {'banana', 'apple', 'cherry'} because set is not allow the duplicate element


print("-----------------------------------")


#4.  Create a dictionary with 3 key-value pairs of student names and marks. Print only the keys.

student_marks = {
    "Aishu" : 80,
    "Ammu" : 70,
    "Kavya" : 65
}
print(student_marks.keys())

print("-----------------------------------")


#5.  Check whether 'apple' is present in the given set:
fruits = {'apple', 'banana', 'mango'}

print("apple" in fruits)

print("-----------------------------------")



# 🔹 Level 2 — Medium
#6. Write a Python program to remove all duplicates from a list using a set.
list2 = [1, 2, 3, 2, 3, 4, 1, 5, 6, 3]
list_unique = set(list2)
print(list_unique)

print("-----------------------------------")

#7. Given this dictionary:
# student = {'name': 'Rajeshwari', 'age': 22, 'course': 'MCA'}
# Add a new key 'college': 'JSS' and print the updated dictionary.

student = {'name': 'Rajeshwari', 'age': 22, 'course': 'MCA'}

student["College"] = "JSS"
print("Updated dictionary",student)

print("-----------------------------------")


#8. Write a program to count frequency of each word in a list using a dictionary.
# Example: words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# Output → {'apple': 3, 'banana': 2, 'orange': 1}

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

word_count = {}

for w in words:
    word_count[w] = word_count.get(w, 0) + 1
print(word_count)

print("-----------------------------------")

#9. Find the intersection and union of two sets:
#
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("The Union of set is: ", A | B)
print("The Intersection of set is", A & B)

print("-----------------------------------")

#10. Convert the following dictionary into a list of tuples:
# student = {'name': 'Rajeshwari', 'course': 'MCA', 'year': 2}
# Expected output: [('name', 'Rajeshwari'), ('course', 'MCA'), ('year', 2)]

student1 = {'name': 'Rajeshwari', 'course': 'MCA', 'year': 2}

dict_items =student1.items()
list_dict = list(dict_items)
print(list_dict)

print("-----------------------------------")

# 🔹 Level 3 — Advanced Thinking
#11. Write a program that takes a list of numbers and prints all unique elements in sorted order.
list3 = [1, 2, 3, 4, 5, 1, 6, 7, 2, 10, 2]
# list3.sort()
unique_num = sorted(set(list3))

print(unique_num)

print("-----------------------------------")

#12. Given a dictionary of students and marks, find the student with the highest marks.

students = {
    'Rajeshwari': 62,
    'Aishwarya': 73,
    'Kiran': 52
}

top_student = max(students, key=students.get)
print(f" Top Student {top_student} with marks {students[top_student]}")
print("-----------------------------------")


#13. Write a program to merge two dictionaries.

student1 = {
    "name" : "aishu",
    "education" : "BCA",
    "marks" : 84,
    "college" : "ACU"

}

student2 = {
    "name" : "Raji",
    "education" : "BSC",
    "marks" : 80,
    "college": "MCU"
}
student1.update(student2)
print(student1)
print("-----------------------------------")


#14. From a list of tuples representing student data:
# Convert it into a dictionary with names as keys and ages as values.
students = [('Rajeshwari', 22), ('Aishwarya', 23), ('Kiran', 22)]
list_item = dict(students)
print(list_item)


print("-----------------------------------")

# Given two lists:
# keys = ['name', 'age', 'course']
# values = ['Rajeshwari', 22, 'MCA']
# Create a dictionary using these two lists.


keys = ['name', 'age', 'course']
values = ['Rajeshwari', 22, 'MCA']
result = dict(zip(keys, values))
print(result)