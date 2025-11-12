# arithmetic operators

a = 5
b = 2

print(a+b)
print(a-b)
print(a/b) # it always gives float value in python
print(a*b)
print(a%b) #remainder
print(a**b) # powerfind

#Relational / Comparison Operators
##### -->  (==, !=, >, <, <=, >=)

print(a==b) # False

print(a!=b) # True

print(a>b) # True

print(a<b)  # False

print(a>=b) # True

print(a<=b) #False




### Assignment Operators (=, +=, -=, *=, /=, %=, **=)

a+=4
print(a)
a*=8
print(a)
a=4
a**=2
print(a)



### Logical Operators (not, and , or)
print(not False) #True
print(not True) #False
print(not (a>b))  #False

val1 = True
val2 = False
print("and operator", val1 and val2)

print("or Operator", val1 or val2)

print((a==b) or (a>b)) #True

#type conversion
a,b = 1,2.0
sum = a+b
print(sum)

#Conversion , Casting --> Manually

#error
# Type Casting 
a,b = 1,"2"
c = int(b)
sum = a+c
print(sum)


#input in Python
# input() statement is used to accept values(using keywords) from user

# input() #result for input() is always a str
# int(input()) #int
# float(input()) #float

# name = input("Enter your name: ")
# print("welcome", name)



# a = int(input())
# b = int(input())
# print(a+b)

# side = int(input())
# area = (side*side)
# print(area)

input1,input2 = float(input()),float(input())
# input2 = float(input())
average = (input1+input2)/2
print(average, "average")






