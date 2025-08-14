# Special Functions =>
# Special functions are built-in functions or anonymous functions that enhance
# Python’s expressiveness and functional programming capabilities.

# 1.  lambda function


# def square(x):
#     return x * x


# print(square(12))

# s = lambda x: x * x
# print(s(12))

# .......................................................................
# 2. map function
# syntax : map(function,iterable)

# z = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(len(z)):
#     z[i] *= 2
# print(z)

# x = list(map(lambda a: a * 2, z))
# print(x, z)
# creating a new list
# .......................................................................
# Problem 1. calculate cube of each element of the list

# .............................................................................
# 3. Filter Function
# syntax => filter(function,iterable)

# z = [1, 2, 3, 4, 5, 6, 7, 8]
# x = []
# for i in z:
#     if i % 2 == 0:
#         x.append(i)
# print(x)

# x = list(filter(lambda a: a % 2 == 0, z))
# print(x)
# ........................................................................
"""
Problem 2.  words = ["apple", "banana", "apricot", "cherry", "avocado"]
filter the elements whose length is less than 6
"""
"""
Problem 3.  From a list of integers, filter numbers whose square is less than 50.
ds=[1,2,67,23,11,12,3,67,5,8,6,4,3]
"""
# .........................................................................
# 4.  Sorted => sort the list
# syntax sorted(listName)
# syntax sorted(listName,reverse=True)
# syntax sorted(listName,key, reverse=True)

# ds = [1, 2, 67, 23, 11, 12, 3, 67, 5, 8, 6, 4, 3]
# x = sorted(ds)
# y = sorted(ds, reverse=True)
# print(x, y)
# c = [["Sam", 30], ["Leo", 34], ["Danny", 23], ["Joe", 12], ["Monica", 22]]
# z = sorted(c, key=lambda a: a[0])
# a = sorted(c, key=lambda a: a[1])
# print(z, a)

d = {"a": 3, "b": 1, "c": 2}
pairs = [(2, 2), (4, 1), (1, 3), (3, 6), (7, 9)]

# .............................................................
# 5. len()
# 6. sum()
# 7. isinstance(a,list) => type checking
# print(isinstance(d, dict))
# .................................................................
# 8. zip => combine the iterables
# words = ["apple", "banana", "apricot", "cherry", "avocado"]
# z = [2, 3, 4, 6, 7]
# x = list(zip(z, words, pairs, d))
# print(x)

# 9. dir()
# print(dir("python"))
# print(dir(z))

# 10. reduce
