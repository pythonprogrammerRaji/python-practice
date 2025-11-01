# tuple (): the tuple is a collection of item ordered and immutable(unchanged) and tuple is similar to list but
# once a created can't be changed

# 1. creating tuple
t11 = (1, 2, 3, 4, 5)
print(type(t11))
print(t11)

t22 = ("apple", 1)
print(t22)

# 2. function of tuple

# 1.len()
T = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10)
print(len(T))

# 2. index()
print(T[0])
print(T[2])
print(T[4])

# 3. count()
print(T.count(10))

# 3. to modify the tuple using list (if want to modify the tuple in directly its rise the error)
fruit = ('apple', 'banana')
print(type(fruit))
m = 'mango'
l = list(fruit)
print(type(l))
l.append(m)
fruit1 = tuple(l)
print(fruit1)

print("---------------- Tuple operation --------------------")

# 1. tuple concentration
t1 =(1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10)
t3 = t1 + t2
print(t3)

#2. repetation
print(t1*2)

#3. checking membership (in and not in)
text = ("the python is good programing", "java", "c", "python")
print("python" in text)
print(2 not in text)

# 4. Nested tuple
nested_tuple = (1, 2, (3, 4))
print(nested_tuple)

