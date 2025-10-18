# variable and datatypes test
#create variable to store your name,age,height, and is_student and print each variable along with using type
name = "Raji"
age = 22
height = 45.5
is_student = True


print(type(name))
print(name)
print(type(age))
print(age)
print(type(height))
print(height)
print(type(is_student))
print(is_student)

#test-2 : type coversion
#Take a sting input of your age : "21" and convert it to integer and then add 5 to it and print the result

age = input("Enter your age: ")
int_num = int(age)
result = int_num + 5
print(result)

# 3. arithmetic operator
#take the two numbers from user, calculate and print:add,sub,mul,div,floor div,modulo and exponent
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))

print("Addition",num1+num2)
print("Subtract",num1-num2)
print("multiplication",num1*num2)
print("division",num1/num2)
print("flore division",num1//num2)
print("modulo",num1%num2)
print("exponent",num1**num2)

#4 input and output,print() and f-string text
#take name and age as input and print some thing and use f-string for formating

name = input("Enter the name: ")
age = int(input("Enter yor age"))
print(f"Hello {name}! next Year you will be {age+1} Years old")

#5. string concatenation
#take first name and lastname as input nad combine them to create a full name using + operator and also using f-sting and print both of them

first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
print("My full name is " + first_name + " " + last_name)
print(f"My full name is {first_name} {last_name}")




