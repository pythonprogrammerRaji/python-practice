# string => the string is ued to text formate and using ('', "", ''' ''') write the code

name = 'RadhaRani'
Name = "LaxmiDevi"  # here name and Name both are case-sensitive or different
name1 = "Radha"

my_places= '''Golok,
            Brudhavana,
            Dwaraka'''


print(type(name))

print('my First Name is',name)
print("my second name is",Name)
print('''my human being name is''',name1)
print('my places are',my_places)

# numbers types => int, Float, Complex

a = 10
b = 23.67
complex_number = 3+4j
print(type(a))
print(type(b))
print(type(complex_number))

# sequential type
# 1. List[] => all datatypes stored in singal format, list is Mutuble and the list used in []

my_list = [11, 45.54,"Aishu", True, {"city":"police"}]

print(type(my_list))
print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

# To change the 11 to 90 value
my_list[0] = 90
print(my_list)

my_list[3] = False
print(my_list)

# method of list
# 1. append() => to add the element at end of the list
my_list.append(10);
print(my_list)

# 2. Insert() => to add or insert the value at particular position using indexes
my_list.insert(3,3333)
print(my_list)

# 3. remove() => Remove the particular value in list
my_list.remove({'city':'police'})
print(my_list)

# 4. pop() => remove the value at end of the list
my_list.pop()
print(my_list)

# 5. count() => count the number element in list
# list=my_list.count()
# print(list)

# 6. extend() => using to adding a multiple value in the list
my_list.extend([12,30,100])
print(my_list)

# 7. index() => to find the what value is stored in particular index
#

# 8.reverse() => to reverse the list
my_list.reverse()
print(my_list)

# 9. sort() => arranging the all element in list ascending order (only in number not ant other types)
a=[10, 30, 20, 50, 40]
a.sort()
print(a)

# 10. clear() => ued to clear the all elements in list
a.clear()
print(a)

frouit = ["apple","bannana","Mango","Graps","apple","Mango"]

print(frouit)

frouit.append('pineapple')
print(frouit)

frouit.extend(["orange","straberry","sapota"])
print(frouit)

frouit.pop()
print(frouit)

print(frouit.count("Mango"))

frouit.reverse()
print(frouit)

print("-------------------- tuple ------------------------")

# 2.tuple ()=> all datatypes stored in singal format, the tuple write in parentesis (), tuple is immutable

tuple = (22, 34.67, 3+4j, "Mango", {"city":"ballari"})
print(tuple)
print(type(tuple))


tuple1 = [1, 2, 3, 2, 4, 5, 6, 7, 6]
print(tuple1)

print(tuple1[1])
tuple1.index((3))
tuple1.count(2)


