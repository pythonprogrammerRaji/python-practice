# # 1. Length and indexing
#
# str = input("Enter a string: ")
#
# print("the first character of string", str[0])
# print("the last character of string", str[-1])
# print("total character of length", len(str))
#
# # 2.Slicing
# print("-----------Slicing------------")
#
# print("the first character of string", str[0:3])
# print("the last character of string", str[-4:-1])
# print("Every second character", str[0::2])
#
# # 3.String methods
# sentence = input("Enter the sentence")
#
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.title())
#
# # 4. counting and finding
# name = "Radha Rani"
# print(name.count('a'))
# print(name.find("a"))

# 5. replace and Strip

text = "       Python is powerful programming language     "
print(text.strip())
print(text.replace(" ", "-"))

# 6. palindrome check

word = input("Enter teh word")

word_count = word.lower()

if word == word[::-1]:
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")

# 7. vowel count
string = input("Enter a string")
vowels = "aeiou"
count = 0

for ch in string.lower():
    if ch in vowels:
        count += 1

print("the total vowels in", count)
