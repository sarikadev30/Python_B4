# 1st Way
# file = open("data.txt", "r")
# print(file.read())

# file.close()

# .....................................................
# 2nd Way => Automatically closes the file

# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)

# ........................................................
# File Modes => When opening files we need to specify the modes

# ...........................................................
# r => read
# w => write
# a => append
# various combinations of all the three
# ............................................................
# W MODE
# We created Empty File => then Write
# with open("notes.txt", "w") as f:
#     f.write("Hi!, I am in Write Mode...")

# No file Created => It creates the file
# with open("q1.txt", "w") as f:
#     f.write("Hi!, I am in Write Mode in Q1...")

# File Already Exists with some data => Overwrites
# with open("data.txt", "w") as f:
#     f.write("Hi!, I am in Write Mode in data...")

# ...............................................................
# A MODE

# File Already Exists => It appends the data in the end
# with open("data.txt", "a") as f:
#     print(f.tell())
#     f.write("Hi!, I am in Append Mode")
#     print(f.tell())

# No file Created => It creates the file
# with open("q1.txt", "a") as f:
#     print(f.tell())
#     f.write("Hi!, I am in Append Mode")
#     print(f.tell())

# ....................................................................

# Variants of Read and Write
# r+
"""
- Opens an existing file for both reading and writing.
- File must exist, or you'll get a `FileNotFoundError`.
- File pointer is at the beginning.
- Does not truncate the file (i.e., does not clear content).
"""

# with open("data.txt", "r+") as f:
#     print(f.read())

with open("data.txt", "r+") as f:
    print(f.read())
    f.seek(1)
    f.write("Bye!...")
    f.seek(0)
    print(f.read())

# .....................................................................
