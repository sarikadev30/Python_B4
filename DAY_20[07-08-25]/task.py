# Variants of Read and Write
# r+
"""
- Opens an existing file for both reading and writing.
- File must exist, or you'll get a `FileNotFoundError`.
- File pointer is at the beginning.
"""

# with open("data.txt", "r+") as f:
#     f.write("Bye!...")
#     f.seek(0)
#     print(f.read())
# ..............................................................
# w+
"""
- File created if not exists
- File pointer is at the beginning.
"""

# with open("data2.txt", "w+") as f:
#     f.write("Hi!")
#     f.seek(5)
#     print(f.read())

# ....................................................................
# a+

"""
for appending and reading 
File Pointer is at the end
"""
# with open("data.txt", "a+") as f:
#     # f.seek(2)
#     f.write("Hi....Sam....")
#     f.seek(1)
#     print(f.read())

# ..................................................................
# read() => it reads the file as a single string
# readline() => it reads line  by line
# with open("studentData.txt", "r+") as f:
#     x = f.readline()
#     x = int(x) + 5
#     y = f.readline()
#     y = int(y) + 10
#     print(x, y, f.readline(), f.readline())

# readlines() => read the lines and give output in list

# with open("studentData.txt", "r+") as f:
#     x = f.readlines()
#     y = []
#     for i in x:
#         z = int(i) + 4
#         y.append(str(z))
#     f.seek(0)
#     io = "\n".join(y)
#     f.write(io)

# l = ["Sam", "Joe", "Monica"]
# x = "\n".join(l)
# print(x)
