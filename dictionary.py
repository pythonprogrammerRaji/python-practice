# dict {"key":"value"} : the dictionary is a collections of key-value pairs and dict is unorderd and mutable

# 1. create the dict

birthday = {
    "Aishu":"09-10-2002",
    "Keerathana":"22-08-2002",
    "Kavya":"10-04-2003",
    "Chandu":"23-09-2002",
    1:2

}
print(type(birthday))
print(birthday)

# 2. Accessing the dict value using keys
print(birthday["Aishu"])

# using get() methos to access the elements id there have that key in dict
print(birthday.get("Keerathana"))
print(birthday.get("raji","not found"))

# 3. adding and update the dict
birthday["Raji"] = "20-03-2002"
print(birthday)

birthday["Chandu"] = "24-10-2002"
print(birthday)

# 4. Remove the element in dict
birthday.pop(1)
print(birthday)

# dictionary methods
# a. keys() : to return the keys only from dict
print("The all keys",birthday.keys())

# b. values() : to return the values only from dict
print("The all values",birthday.values())

# 3. items(): to return the key-value as a tuple
print(birthday.items())

# 4. update() : update the dict with another dict
new_birthday = {
    "vaishnavi": "07-08-2003",
    "siri":"02-08-2002"
}
print(birthday.update(new_birthday))