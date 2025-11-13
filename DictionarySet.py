# Dictionary in python
#  Dictionaries are used to store data values in key:value pairs
#  They are unordered, mutable (changeable) & don't allow duplicate keys
#  
#
#
#

dict = {
    "name":"nitesh",
    "cgpa": 9.8,
    "marks": [98,97,99],
    3:"number",
    "is_adult": True,
    4:5,
}
print(dict["name"],dict["cgpa"],dict["marks"],dict[3],dict[4])

null_dict = {}


dict["name"] = "Nitesh" #overwrite
dict["surname"] = "raut"
print(dict)

# nested dictionary

student = {
    "name":"rahul kumar",
    "subjects":{
        "phy":85,
        "chem":89,
        "math":56
    }
}
print(student["subjects"]["phy"])

# Dictionary Methods
#  myDict.keys() # returns all keys
#  myDict.values()  # returns all values
#  myDict.items()  # returns all (key, val) pairs as tuples
#  myDict.get("key")  #returns the key according to value
#  myDict.update(newDict)  #inserts the specified item to the dictionary

# dict["key"] = "value" #to assign or add new

print(len(student))
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())

print(student.items())
# change into list then we access the tuple 
my_list = list(student.items())
print(my_list[0])

# difference between the student.get("key") or access the student["key"]
# then it gives second and error if the key is not present but first one give
# return the None

print(student.get("name2")) # --> None return
# print(student["name2"]) # -> error 









# 1. Dictionary Comprehension

# It’s used to create a dictionary quickly — just like you created lists, but with key-value pairs.

# {key_expression: value_expression for item in iterable if condition}
# Example 1: Square of numbers with key-value
squares = {x: x*x for x in range(5)}
print(squares)
# Output: is coming in the dictionary
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example 2: Filter condition inside

even_squares = {x: x*x for x in range(10) if x % 2 == 0}
print(even_squares)
# Output:
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Example 3: Convert a list to a dictionary
names = ["nitesh", "ram", "shyam"]
length_dict = {name: len(name) for name in names}
print(length_dict)
# Output:
# {'nitesh': 6, 'ram': 3, 'shyam': 5}



# set in python
#  Set is mutable but the element is inside immutable
#  Set is the collection of the unordered items.
#  Each element in the set must be unique & immutable.
#  boolean, int, float, str, tuple 
#  not store the list and dictionary because it is mutable so does not stored in the set

nums = {1,2,3,4}

set2 = {1,2,3,2,2,(1,3,4)}
# repeated elements stored only once, so it resolved to {1,2}

null_set = set()  #empty set syntax

collection = {} # empty dictionary so we can do for the sets so we used above method

print(set2)

# Set Methods
# 
#  set.add(el) #adds an element
#  set.remove(el)  #removes the element
#  set.clear()  # empties the set
#  set.pop()   # removes a random value
#
#



set1 = {1,2,3,4}
set2 = {3,4,5}

print(set1,set2,"set1, set2")

print(set1.union(set2),"set union")  #combines both set values & return new
print(set1.intersection(set2),"set intersection")  # combines common values & return new











# 2 Set Comprehension

# It’s used to create a set — which automatically removes duplicates.

# {expression for item in iterable if condition}
# Example 1: Simple set
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)
# Output:
# {1, 2, 3}

# Summary Table

# Type          Syntax                                              Creates
# List         [expr for x in iterable if cond]              List (with duplicates, ordered)
# Set          {expr for x in iterable if cond]              Set (unique elements, unordered)
# Dict         {key: value for x in iterable if cond]        Dictionary (key-value pairs)
nums = [1, 2, 3, 4]

# List
squares_list = [x*x for x in nums]

# Set
squares_set = {x*x for x in nums}

# Dict
squares_dict = {x: x*x for x in nums}

print(squares_list)
print(squares_set)
print(squares_dict)


# Store following word meanings in python dictionary:
   
words = {
   "table":["a piece of furniture","list of facts & figures"],
   "cat":"a small animal"
}
print(words)


# you are given a list of subjects for students. Assume one classroom is required 
# for 1 subject. How many classrooms are needed by all students.

# "python", "java", "C++", "python","javascript","java","python","java","C++","C"

my_set = {"python", "java", "C++", "python","javascript","java","python","java","C++","C"}

print(len(my_set))


# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks1,marks2,marks3 = int(input()),int(input()),int(input())
new_dict = {"math":marks1,"english":marks2,"phy":marks3}
dict = {}
dict.update(new_dict)
print(dict)



#  Figure out a way to store 9 & 9.0 as separate values in the set.
# (you can help of built-in data types)

my_set = {9,"9.0"}

values = {("float",9.0),("int",9)}

print(my_set)
print(values)