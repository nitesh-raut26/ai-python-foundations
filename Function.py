# Functions in Python
#  Block of statements that performs a specific task.

# def func_name(param1, param2...): Function Definition; parameters
#   some work
#   return val

# func_name(arg1, arg2..) function call; arguments


print("mindset",end=" ") #here end define to separates first one is sep="" and end =""
print("is everything")

def sum(a,b):
    s=a+b
    return s
print(sum(6,2))

# average of three number

def average_num(a,b,c):
    average = (a+b+c)/3
    print(average)
    return average
result = average_num(4,7,3)
print(result)

# Default parameters
def cal_prod(a=1,b=3):
    print(a*b)
    return a*b
cal_prod()

# WAF to print the length of a list. (list is the parameter)
# WAF to print elements of a list in a single line. (list is the parameter)
# WAF to find the factorial of n. (n is the parameter)
# WAF to convert USD to INR.
def printList(list):
    print(len(list))
    print(list)
    for item in list:
        print(item,end=" ")
    print()
list = [1,2,34,5,6]
printList(list)


def fact(n):
    i = 1
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print("factorial of number",n,"is",fact)
fact(5)

def usd_inr(amount):
    inr = amount*89
    print(amount,"$ to inr is",inr)
usd_inr(4)


# Recursion
# When a function calls itself repeatdely

# prints n to 1 backwards
def show(n):
    if(n==0):
        print()
        return
    print(n,end=" ")
    show(n-1)
show(20)

# return n!
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
fact = fact(5)
print(fact)

# wap a recursive function to calculate the sum of first n natural numbers.


def sumfirst_number(n):
    if(n==1):
        return 1
    return n+sumfirst_number(n-1)
print(sumfirst_number(10))


# wap a recursive function to print all elements in a list.

def printelement(list,idx):
    if(idx==len(list)):
        print()
        return
    print(list[idx],end=" ")
    printelement(list,idx+1)
list = [1,5,6,9,10,13]
printelement(list,0)















