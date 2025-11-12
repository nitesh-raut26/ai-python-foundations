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

list = [2,1,3]
list.append(4) #adds one element at the end [2,1,3,4]
list.sort() #sorts in ascending order [1,2,3,4]
list.sort(reverse=True) #sorts in descending order [4,3,2,1]
list.reverse() #reverse list [3,1,2] // [1,2,3,4]
list.insert(2,7) #idx = index, el = element [1,2,7,3,4]
list.append(1) #idx = index, el = element [1,2,7,3,4,1]
list.remove(1) #removes first occurence of element [2,7,3,4,1]
list.pop(2) #idx removes elements at idx  [2,7,4,1]

print(list) # [2,7,4,1]


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


# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.




# WAP to check if a list contains a palindrome of elements. (Hint use copy() method)
# [1,2,3,2,1]   [1,"abc","abc",1]






