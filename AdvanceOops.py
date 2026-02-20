#Getter and Setter

class Back:
    def __init__(self, username, password):
        self.__username = username  #private
        self.__password = password   #private

    def login(self):
        print(f"username: {self.__username} and password: {self.__password}")

    def get_name(self):         #get a name
        return self.__username

    def set_name(self, username):    #set a name
        self.__username = username

    def get_pass(self):            #get a password
        return self.__password

    def set_pass(self, password):    #set a password
        self.__password = password


b = Back("Asha","1234")

print("Before change the username and password")
print(b.get_name())
print(b.get_pass())

print("After change the username and password")

b.set_name("Sindhu")
print(b.get_name())

b.set_pass("9876")
print(b.get_pass())

#Method Overloding : In class same method name and different attributes

class Calculate:
    def add(self, a, b, c=0):
        print( a + b + c )

c = Calculate()
c.add(1, 2)
c.add(1,2, 3)


#Method Overriding : override the another method

class Animal:
    def Sound(self):
        print("This animal makes a sounds")

class Dog(Animal):
    def Sound(self):
        print("Dog barks")

animal = Dog()
animal.Sound()

#Super() : Super keyword used to access the parent class all properties and method

class Boy:
    def __init__(self, name):
        self.name = name

class Student(Boy):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display_info(self):
        print(f" The student name is {self.name} and roll_no is {self.roll_no}")

s = Student("Mahi", "1001")
s.display_info()

#Abstract Class : Its same as class but this have abstract method that did not contain any data and its pass all data in child class
# Note : The Abstract class import from ABC (Abstract base Class)

from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def fruit_color(self):
        pass
class Apple(Fruit):
    def __init__(self, color, fruit):
        self.color = color
        self.fruit = fruit

    def fruit_color(self):
        print(f"{self.fruit} color is {self.color}")

F = Apple("red", "apple")
F.fruit_color()



