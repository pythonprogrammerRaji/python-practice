# 1️⃣ Create and Access
# Create a tuple with your name, age, and city.
# Print the first and last elements.

t1 = ("Aishu", 22, "Bidar")
print("name",t1[0])
print("city",t1[-1])


# 2️⃣ Slicing
# Take a tuple of numbers (1,2,3,4,5,6,7,8,9).
# Print only the middle three numbers.
num = (1,2,3,4,5,6,7,8,9)
print(num[3:6])


# 3️⃣ Methods
# Create a tuple with repeated numbers.
# Count how many times a particular number appears and find its first index.
number = (1,2, 3, 3, 4, 5, 2, 5, 2, 6, 7)
print(number.count(2))
print(number.index(2))


# 4️⃣ Tuple Packing & Unpacking
# person = ("Raji", 22, "Bengaluru")
# Unpack into variables name, age, city and print each.
person = ("Raji", 22, "Bengaluru")
name,age,city = person
print(name)
print(age)
print(city)


# 5️⃣ Immutability Test
# Try to change an element and observe the error.

# x


# 6️⃣ Nested Tuples
# Make a tuple that contains another tuple:
# nested = (1, (2,3), 4)
# Access the number 3 using indexing.
nested = (1, (2, 3), 4)
print(nested[1][1])
