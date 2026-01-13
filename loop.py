num = int(input("Enter the number to check if is a prime number: ")) # prime number is which number is not divided by 2 is called prime number

varf = False

if (num > 1):
    for j in range(2, num):
        if(num % j) == 0:
            varf = True
            break

if varf:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

if(num>1):
    for j in range(2, num):
        if(num % j) == 0:
            print(num, "is not a prime number")
            print(j, "times", num//j, "is", num)
            break
        else:
            print(num, "is a prime number")
else:
    print(num, "is not a prime number")



