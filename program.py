# varnum1 = int(input("Enter First Number : "))
# varnum2 = int(input("Enter Second Number : "))
# varnum3 = int(input("Enter Third Number : "))
# varSum = varnum1+varnum2+varnum3
#
# print("The First number", varnum1)
# print("The second number", varnum2)
# print("The third number", varnum3)
#
# print("The sum of three numbers", varSum)

# Second program to using format keyword

# Varnum1 = input("Enter first number: ")
# Varnum2 = input("Enter second number: ")
#
# Sum = float(Varnum1)+float(Varnum2)
#
# print("The sum of {0} and {1} is {2}".format(Varnum1, Varnum2, Sum))

# to write the all code in one single line to perform the Arithmatic operation

#print('The addition of two numbers is %.1f' %(float(input("Enter the first number: ")) + float(input("Enter the Second number: "))))

#print('the subtraction of two numbers is %.1f' %(float(input("Enter the first number: ")) - float(input("Enter the second number: "))))

#print('the product of two number is %.1f' %(float(input("Enter the first value: ")) * float(input("Enter the second value: "))))

#print("The division of two number is %.1f" %(float(input("Enter First Number: ")) / float(input("Enter Second Number: "))))

# the square root nom => 8 is square ri=oot is 2

# num = float(input("Enter a number to find square root : "))
# num_square = num ** 0.5 # 0.5 is root
# print("The square root of %0.2f is %0.2f" %(num, num_square)) #0.2f its point two decimal ex: 8.00 here 00 is 2 decimal after point

# another way to find the square root

import cmath # import the cmath, cmath is a libarary

num1 = eval(input("Enter the number to find the square root: "))
num1_square = cmath.sqrt(num1)
print("The square root of {0} is {1:0.2f} + {2:0.2f}j".format(num1, num1_square.real, num1_square.imag))


