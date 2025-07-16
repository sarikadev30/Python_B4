# Data Types => int float bool str
# Primitive => int float bool str
# Non Primitive => list dictionary set tuple

# x = "Sam"
# print(x, x[1], x[2])
# # x[1] = "b"
# x = "Sbm"
# print(x, x[1], x[2])

# ..............................................................
# LIST  => store multiple values

# CREATE
# x = [1, 2, 3, 4, "Sam", 3.0, True]
# print(x)
# print(len(x))
# print(type(x))
# ...................................................................................................
# READ
# Indexing => Positive Indexing => 0 .... n-1
# print(x[0])
# print(x[5])

# Indexing => Negative Indexing =>  -n.......-1
# print(x[-2])

# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]

# print(K[-1][-1])
# print(K[-4])

# marks = [23, 13, 78, 45, 67, 34, 56]
#  Loops
# for i in marks:
#     print(i)

# for j in range(len(marks)):
#     print(marks[j])
# .................................................................................................
# Give 4 gracing marks to the subjects at odd indexes and subract 2 marks from even indexed subjects
# marks[2] += 3
# print(marks)

# .................................................................................................
# SLICING
# x = [1, 2, 3, 4, "Sam", 3.0, True]
# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]
#      0 1  2   3      4       5     6     7

# X[start:end:step]
# print(x[2:5:1])
# print(x[:4:])
# print(x[6:3:-1])
# print(x[-1:-4:-1])
# print(K[(len(K) - 1) : 4 : -1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[-4:-1])
# print(thislist[:4])
# print(thislist[2:5])
# print(thislist[2:])

# ..............................................................................
# UPDATE

# Replace =>
# x = [1, 2, 3, 4, "Sam", 3.0, True]
# x[-1] = False
# print(x)

# Addition =>
# append  => add the element at the end
# x.append(4.5)
# print(x)
# x.append([1, 2, 3, 4, 5, 6, 7, 89])
# print(x)

# insert => at particular index I can add element
# x.insert(0, 23)
# print(x)
# x.insert(4, ["Hi", "Sam", "Bye"])
# print(x)

# extend => adds the lists together
# y = ["Hi", "Sam", "Bye"]
# # x.extend(y)
# y.extend(x)
# print(y)

# ...................................................................
# CRUD => CREATE READ UPDATE DELETE

# PROBLEM 1 **Perform the following tasks :**
# 1. **Create list of superheroes**
# 2. **push 4 superheroes in the List**
# 3. **Print the List**

x = []
