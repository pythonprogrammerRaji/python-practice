# def menu():
#     print(f"Simple Calculator")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#
#
#
# while(True):
#     menu()
#     choice = int(input("Enter a your choice number: "))
#
#
#     if choice in (1, 2, 3, 4):
#         num1 = int(input("Enter a First number: "))
#         num2 = int(input("Enter a Second number: "))
#
#     if choice == 1:
#         print(f"Result {num1} + {num2} = {num1 + num2}")
#     elif choice == 2:
#         print(f"Result {num1} - {num2} = {num1 - num2}")
#     elif choice == 3:
#         print(f"Result {num1} * {num2} = {num1 * num2}")
#     elif choice == 4:
#         if num2 == 0:
#             print(f"number not divisible by zero")
#         else:
#             print(f"Result {num1} / {num2} = {num1 / num2}")
#     elif choice == 5:
#         print("Stop the Calculation..! GoodBye👋")
#         break
#     else:
#         print("Invalid choice, Try again")
#
def bank_menu():
    print("\nSimple Banking System Application")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


balance = 1000  # Initial balance

while True:
    bank_menu()
    back_choice = int(input("Enter your Bank option: "))

    if back_choice == 1:
        print("Current bank balance is:", balance)

    elif back_choice == 2:
        amount = int(input("Enter the Amount: "))

        if amount > 0:
            balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    elif back_choice == 3:
        amount = int(input("Enter the Amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    elif back_choice == 4:
        print("Banking transaction completed, visit again")
        break

    else:
        print("Invalid choice, please try again")


# #Grocery Store Menu
# # create a program where users can : Add items to their cart, Remove Items. View the total price, System Exit
def store_menu():
    print("Simple E-commence Application")

    print("1. Add items to their cart")
    print("2. Remove Items")
    print("3. View the total price")
    print("4. System Exit")

cart = []
item_price = []

while(True):
    store_menu()
    store_choice = (input("Enter your choice option: "))

    if store_choice == 1:
        item = input("Enter the item: ")
        price = int(input("Enter a item price: "))
        cart.append(item)
        item_price.append(price)
        print("The cart is:", cart)
    elif store_choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            index= cart.index(item)
            cart.pop(index)
            item_price.pop(index)
            print("Item removed successfully")
        else:
            print("Item not found in cart")

    elif store_choice == 3:
        total= sum(item_price)
        print("Total price is:", total)

    elif store_choice == 4:
        print("System Exit, Thank you")
        break
    else:
        print("Invalid choice pls try again")

# #Educational System
# # Write a program with option to: Add student Details, display student details, Exit

def education_menu():
    print("Simple Backing system Application")

    print("1. Add student Details")
    print("2. display student details")
    print("3. System Exit")

student_details = []

while(True):
    education_menu()
    education_choice = int(input("Enter your choice: "))


    if education_choice == 1:
        print("Add student Details")
        usn = input("enter the USN Number: ")
        name = input("Enter the name: ")
        subject = input("Enter the subjects")

        student = {
            'USN': usn ,
            'Name': name,
            'Subject': subject
        }

        student_details.append(student)
        print("Student details added successfully")


    elif education_choice == 2:
        print("Display student details")
        if not student_details:
            print("No student details available")
        else:
            for student in student_details:
                print("USN",student["USN"])
                print("Name",student["Name"])
                print("Subject",student["Subject"])

    elif education_choice == 3:

        print("Student list Completed, add tomorrow")
        break
    else:
        print("Invalid choice pls try again")