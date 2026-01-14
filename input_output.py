age = 22  # input
print(age)  # output

# User input
boy_name = input("Boy Name: ")
boy_age = int(input("Boys Age: "))
girl_name = input("Girl Name: ")
girl_age = int(input("Girls Age: "))

# perform some activites to code
# abs is absolute value (it has given a negative values also positive)
age_diff = abs(boy_age - girl_age)

# output
print(boy_name + " Loves " + girl_name + " Age Difference " + str(age_diff))  # string Concatenation
print(f"{girl_name} loves {boy_name} Age Difference  {age_diff}")  #f-formatting String

# home work

name = input("Enter your name: ")
age = int(input("Enter your number"))
print(f"Hello, {name}")
