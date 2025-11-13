# List in python
# A built in data type of different types(integer, float, string etc)
# It can store elements of different types(integer,float,string etc.)
# marks = [87,64,33,95,76]
# student = ["Karan",85,"Delhi"]
# student[0] = "Arjun"  # allowed in python
# len(student) #returns length
# 

# strings are immutable in python
# List are mutable in python

str = "Hello World"
#str[0] = "N" # doesn't support item assignment in string immutable
print(str)
# str.replace("H","N")
# print(str)

marks = [94.4,87.5,95.2,66.4,45.1]
print(type(marks))
marks[0] = 95.5
print(marks)

# we can do slicing also 
print(marks[1:3]) #[87.5, 95.2]
print(marks[-3:-1]) #[95.2, 66.4]


# List methods

my_numbers = [2,1,3]
my_numbers.append(4) #adds one element at the end [2,1,3,4]
my_numbers.sort() #sorts in ascending order [1,2,3,4]
my_numbers.sort(reverse=True) #sorts in descending order [4,3,2,1]
my_numbers.reverse() #reverse my_numbers [3,1,2] // [1,2,3,4]
my_numbers.insert(2,7) #idx = index, el = element [1,2,7,3,4]
my_numbers.append(1) #idx = index, el = element [1,2,7,3,4,1]
my_numbers.remove(1) #removes first occurence of element [2,7,3,4,1]
my_numbers.pop(2) #idx removes elements at idx  [2,7,4,1]

print(my_numbers) # [2,7,4,1]


# Tuples in python
# A bulit-in-data type that lets us create immutable sequences of values.

tup = (87,64,33,95,76,"hello") #tup[0],tup[1]
#tup[0] = 43 #Not allowed in tuple python we cannot mutate immutablity
print(type(tup))
print(tup)
print(tup.index(33)) #return first index of value
print(tup.count(87)) 
print(len(tup))

# Slicing in tuples
print(tup[1:4])
# 🧠 The slicing syntax in Python:

# The general form is:
# sequence[start:end:step]
# Where:
# 	•	start → where to begin (default = 0)
# 	•	end → where to stop (default = end of sequence)
# 	•	step → how many steps to move (default = 1)

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
favoritemovie1 = input()
favoritemovie2 = input()
favoritemovie3 = input()

movie = [favoritemovie1,favoritemovie2,favoritemovie3]
print(movie)



# WAP to check if a list contains a palindrome of elements. (Hint use copy() method)
# [1,2,3,2,1]   [1,"abc","abc",1]


# rev_number = number[::-1]
# This means:
# 	•	start → not given → take from beginning
# 	•	end → not given → go till the end
# 	•	step = -1 → move backward by 1 step (reverse direction)

# So it creates a reversed copy of the list.
number = [1,2,3,2,1]
rev_number = number[::-1]
print(rev_number)
if(number == rev_number):
    print("palindrome")
else:
    print("Not palindrome")


# WAP to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","A","B","B","A"]

# Store the above values in a list & sort them from "A" to "D"
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

my_list = list(tup)
my_list.sort()
print(my_list)


# What is List Comprehension?

# List comprehension is a short and elegant way to create new lists in Python from existing iterables (like lists, strings, or ranges) — all in one line of code.

# It replaces the need for writing long for loops.

# new_list = [expression for item in iterable if condition]

# Meaning:
# 	•	expression → what you want to do with each item
# 	•	item → variable representing each element
# 	•	iterable → sequence (like list, tuple, range)
# 	•	if condition → (optional) filter elements

# Example 1: Square of Numbers

# Without list comprehension 

squares = []
for i in range(5):
    squares.append(i * i)
print(squares)

# With list comprehension:
squares = [i * i for i in range(5)]
print(squares)


# Example 2: Filtering Even Numbers

# Without list comprehension:

evens = []
for num in range(10):
    if num % 2 == 0:
        evens.append(num)
print(evens)

# With list comprehension:
evens = [num for num in range(10) if num % 2 == 0]
print(evens)
# Output:

[0, 2, 4, 6, 8]

#  Example 3: Converting Strings

names = ["nitesh", "ram", "shyam"]
upper_names = [name.upper() for name in names]
print(upper_names)

['NITESH', 'RAM', 'SHYAM']

# Example 4: Using with Condition & Expression

nums = [1, 2, 3, 4, 5]
result = ["even" if i % 2 == 0 else "odd" for i in nums]
print(result)
# Output:
# ['odd', 'even', 'odd', 'even', 'odd']

# Example 5: Nested List Comprehension

# You can even flatten 2D lists:
matrix = [[1,2,3],[4,5,6]]
flatten = [num for row in matrix for num in row]
print(flatten)
# Output:
[1, 2, 3, 4, 5, 6]

