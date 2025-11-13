# File I/O in python
# Python can be used to perform operation on a file.(read & write data)


# Types of all files
# Text Files: .txt, .docx, .log etc.
# Binary Files: .mp4, .mov, .png .jpeg etc.


# open , read & close File
#  we have to open a file before reading or writing.

# f = open("file_name","mode")

# file_name --> sample.txt , demo.txt
# mode --> r:read mode, w:write mode

# data = f.read()
# f.close()


# f.read() --> reads entire file
# f.readline() --> reads one line at a time


# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","w")
# f.write("Then I'll move to js")
# f.close()



# f = open("demo.txt","a")
# f.write("\nThen I'll move to js")
# f.close()



# f = open("demo.txt","r+")
# f.write("Then I'll move to js")
# f.close()

# # with syntax

# with open("demo.txt","a") as f:
#     data = f.read()
#     print(data)
#     f.close()

# with open("demo.txt","w") as f:
#     f.write("new data")
#     f.close()

#  Deleting a File
# using the os module
# Module (like a code library) is a file written by another programmer
# that generally has a functions we can use.
# import os
# os.remove("sample.txt")


#  WAF that replaces all occurences of "java" with "python" in the practice file.
# Read file
with open("pratice.txt","r") as f:
    data = f.read()
data = data.replace("Java", "Python")
with open("pratice.txt","w") as f:
    f.write(data)
    print(data)

# search if the word "learning" exits in the File or not.
def word_match():
    with open("pratice.txt","r") as f:
        data = f.read()
        if(data.find("learning")!=-1):
            print("exist in the file")
        else:
            print("Not exist in the file")
word_match()


# WAP to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.
# if "Python" in line or "Java" in line: we can check directly not using find function for substring.
with open("pratice.txt", "r") as f:
    line_no = 1
    line = f.readline()

    while line != "":
        if "learning" in line:
            print(line_no)
            break
        line_no += 1
        line = f.readline()
    else:
        print(-1)


#  From a file containing numbers seprated by comma, print the count of even numbers.
with open("numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(",") 
    print(nums,"nums")
    count = 0
    for n in nums:
        if int(n) % 2 == 0:
            count += 1

    print(count)

    












