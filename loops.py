# loops are used to repeat instructions
count = 1
while count<=5:
    print("hello")
    count+=1
print(count)

# iterator = count,i,j,x,y, iteration --> how much run in the loop

# print numbers from 1 to 100
# print numbers from 100 to 1
# print the multiplications table of a number n.
# print the elements of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]
# Search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]


count = 1
while count<=100:
    print(count," ")
    count+=1

count = 100
while count>=1:
    print(count," ")
    count-=1

count = 1
n = 5
while count<=10:
    print(n*count," ")
    count+=1

count = 1
squareList = []
while count<=10:
    squareList.append(count*count)
    count+=1
print(squareList)

numTup = (1,4,9,16,25,36,49,64,81,100)
x = 65
i = 0
while i<len(numTup):
    if(x==numTup[i]):
        print("Number found",x,"at pos",i)
        break
    i+=1
if(i>=len(numTup)):
    print("Not found")


# loops in python
# Loops are used for sequential traversal. For traversing list,string,tuples etc.

# for Loops list = [1,2,3]
# for el in list:
    #some work

# for Loops with else               for el in list:
    #some work                          print(el)
#else:                              else:
    # work when loops ends              print("End")

list = [1,2,3,4,5]
tup = (1,2,3,4,2,8,9)
str = "vidyadotcom"
for el in str:
    print(el)

nums = [1,4,9,16,25,36,49,64,81,100]
x = 49
idx = 0
for num in nums:
    if(num == x):
        print("number found at idx",idx)
        break
    idx+=1

# range()
# Range functions returns a sequence of numbers, starting from 0 by default, and
# increments by 1 (by default), and stops before a specified number.
#  start and step is optional
# range(start?,stop,step?)

for el in range(5):
    print(el) # 0 1 2 3 4

for el in range(1,5):
    print(el) # 1 2 3 4

for el in range(1,5,2):
    print(el)  # 1 3



# print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

# pass statement
# pass is a null statement that does nothing. It is used as a placeholder for future code.

for el in range(10):
    pass


# WAP to find the sum of first n numbers. (using while)

sum = 0
idx = 1
n=10
while idx<=n:
    sum+=idx
    idx+=1
print(sum)


# WAP to find the factorial of first n numbers. (using for)

n = 5
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)


















