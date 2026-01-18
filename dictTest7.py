# 📝 Practice 1: Create and Access
# Create a dictionary:
# student = {
#     "name": "Aishu",
#     "age": 22,
#     "city": "Bengaluru"
# }
# Print the student’s name.
# Print the student’s city.

student = {
    "name": "Aishu",
    "age": 22,
    "city": "Bengaluru"
}
print(student["name"])
print(student["city"])



# 📝 Practice 2: Add & Update
# Add a new key "course": "MCA" to the dictionary.
# Update "age" to 23.
# Print the updated dictionary.

student["course"] =  "MCA"
student["age"] = 23
print(student)


# 📝 Practice 3: Remove
# Remove "city" using .pop().
# Remove the last inserted item using .popitem().
# Print the dictionary after each step.

print(student.pop("city"))
print(student.popitem())    # to remove the last element in dict
print(student)





# 📝 Practice 4: Loop
# Given:
# marks = {"Math": 90, "Science": 85, "English": 88}
# Print all subjects (keys).
# Print all marks (values).
# Print subject with mark together like:
# Math → 90
# Science → 85
# English → 88

marks = {"Math": 90, "Science": 85, "English": 88}
print("All the students keys",student.keys())
print("all the marks values",marks.values())

print("all key-value pair",marks.items())

# 📝 Practice 5: Dictionary Comprehension
#
# From a list nums = [1,2,3,4,5],
# create a dictionary where the key is the number and the value is its square.
# 👉 Expected: {1:1, 2:4, 3:9, 4:16, 5:25}

nums = [1, 2, 3, 4, 5]
dict_square = {x: x*x for x in nums}
print(dict_square)

print(nums)
print(type(nums))



#
# Do you want me to also give you real-world small problems with dictionaries (like word count, frequency count) after these basics, or first you’ll complete these?
#
# You said:
# i am prapare give questions
# ChatGPT said:
#
# Nice 💪 Since you already prepared, here are dictionary questions for practice (mix of basics + real-world style):
#
# 🔹 Q1. Student Info
#
# Create a dictionary for a student with keys: name, age, course.
#
# Print only the keys.
#
# Print only the values.
#
# Print both keys and values using a loop.
#
# 🔹 Q2. Word Frequency
#
# Take a string input from the user, like:
#
# "python is easy and python is powerful"
#
#
# Build a dictionary that counts how many times each word appears.
# 👉 Expected: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
#
# 🔹 Q3. Highest Marks
#
# Given:
#
# marks = {"Math": 90, "Science": 85, "English": 92, "History": 80}
#
#
# Find the subject with the highest mark.
# 👉 Expected: English → 92
#
# 🔹 Q4. Merge Two Dicts
#
# Given:
#
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
#
#
# Merge them into one dictionary.
#
# 🔹 Q5. Dictionary Comprehension
#
# From nums = [1,2,3,4,5,6,7,8,9,10]
# Create a dictionary of even numbers and their cubes.
# 👉 Expected: {2:8, 4:64, 6:216, 8:512, 10:1000}