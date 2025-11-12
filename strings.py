str1 = "this is a string.\nwe are creating.\tit in python"
#tab sequence \t
# one tab space -- 4 spaces


print(str1)                 
str2 = 'we are creating.    t'
print(str2)
str3 = """this is a string"""

# escape sequence characters is neede tab,nextLine,space use \n

# Basic Operations
# concatenations
str1 = "apna"
str2 = "college"
print(len(str2))
print(str1+str2)
print(str1[0])

# length of str
# len(str)
# indexing start from the 0
# we cannot manipulate the data in the string str[4] = "a"
 

#  slicing 
# Accessing part of a string
# str[ starting_idx : ending_idx] ending index is not included
# str[:4] is same as str[0:4]
#  str[1:] is same as str[1:len(str)]


str = "ApnaCollege"
str = str[1:4]
print(str) #pna

# Slicing in negative index
# A p p l e -5 -4 -3 -2 -1

str = "apple"
print(str[-3:-1]) #pl


str = "I am a coder"

str.endswith("er.") #returns true if string ends with substr
str.capitalize() #capitalize 1st char
str.replace("o","a")
str = str.replace("coder","bestcoder")
print(str)

print(str.find("e")) #return 1st index of 1st occurence

str.count("am") #count the occurence of 


#wap to input user's first name and print its length
#wap to find the occurence of '$' in a string

str = input()
print(len(str))
print(str.count('$'))

# Conditional statement
# if-elif-else (syntax)

 
age = 18

if(age>18):
    print("can vote & apply for license")
elif(age < 18):
    print("age can never a vote")
else:
    print("Time to age the license for vote")


#grade student based on marks
marks = 80
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")


#nesting
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# wap to check if a number entered by the user is odd or even
number = int(input())
if(number%2==0):
    print("even")
else:
    print("Odd")

# WAP to find the greatest of 3 numbers entered by the user
number1 = int(input())
number2 = int(input())
number3 = int(input())

if(number1 >= number2 ):
    if(number1>number3):
        print("number",number1,"is greatest amongst of all")
    elif(number1<number3):
        print("number",number3,"is greatest amongst of all")      
elif(number1<number2):
    if(number2>number3):
        print("number",number2,"is greatest amongst of all")
    elif(number2<number3):
        print("number",number3,"is greatest among of them")


if number1 >= number2 and number1 >= number3:
    print("Number", number1, "is the greatest")
elif number2 >= number1 and number2 >= number3:
    print("Number", number2, "is the greatest")
else:
    print("Number", number3, "is the greatest")

# WAP to check if a number is a multiple of 7 or not
if(number%7==0):
    print(number,"is divisble by 7")
else:
    print("number",number," is divisible is not by 7")









