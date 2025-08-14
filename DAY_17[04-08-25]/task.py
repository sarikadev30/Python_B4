# Local Scope
# def greet():
#     message = "Hello"
#     print(message)


# greet()

# print(message)
# .......................................................................

# Global Scope

# x = 10


# def valFun():
#     y = 23
#     global x
#     print(x)
#     x = 78
#     print(x, y)


# print(x)
# valFun()
# print(x)
# .....................................................................
# Enclosing Scope

# x = 45
# def fun():
#     x = 23  # local scope
#     print(x)

#     def inner():
#         nonlocal x
#         print(x)
#         x = 65  # eclosing scope
#         print(x)

#     inner()
#     print(x)


# fun()

# 23
# 23
# 65

# ................................................................
# print(len("PYTHON"))
# x = 23
# def fun():
#     x = 78
#     print("3", x)

#     def innerFun():
#         global x
#         x = 56
#         print("4", x)

#     innerFun()
#     print("5", x)
# print("1", x)
# fun()
# print("2", x)

# 1, 23
# 3, 78
# 4, 56
# 5, 78
# 2, 56

# ................................................................................
# Built In Scope
# print(len("PYTHON"))
# .................................................................................

# x = 10


# def my_func():
#     x = 20
#     print(x)


# my_func()
# print(x)
# 20
# 10
# .....................................................................

# x = 100

# def change():
#     global x
#     print(x)
#     x = 200
#     print(x)


# change()
# print(x)

"""
100
200
200
"""
# .............................................................
# x = 5


# def outer():
#     x = 10

#     def inner():
#         print(x)

#     inner()


# outer()
# print(x)

"""
10
5
"""


# .............................................................
# def outer():
#     x = "local"

#     def inner():
#         nonlocal x
#         x = "nonlocal"

#     inner()
#     print("x inside outer:", x)


# outer()
# print(x)
"""
x inside outer: nonlocal
error
"""


# ..............................................................
# def func():
#     print(x)


# x = 50
# func()

# ..............................................................
# x = 10

# # print(y)
# y = 78
# print(y)


# def func():
#     global x
#     print(x)
#     x = 20
#     print(x)


# func()

"""
78
10
20
"""
# .....................................................................
# x = "global"


# def outer():
#     x = "outer"

#     def inner():
#         print("inner:", x)


#     print("outer:", x)


# outer()
# # inner()
# print("global:", x)

"""
inner:outer
outer:outer
global:global
"""
# ...................................................................

# sum([1,2,3,4,5])

"""
Flatten a Nested List
**Problem Statement:**
Write a function called `flatten_list` that takes a list containing nested lists and 
returns a flat list with all the elements.
print(flatten_list([1, [2, [3, 4], 5], 6]))  # Output: [1, 2, 3, 4, 5, 6]

"""
# x = [1, 2, 3, 4]
# x.append([3, 4])
# x.append(8)
# print(x)
# x.extend([3, 4])
# print(x)
# y = 0
# print(isinstance(y, list))
# print(isinstance(x, list))

# newL = []
# a = [1, [2, [3, 4], 5], 6]


# def flatten_list(a):
#     newl = []
#     for x in a:
#         if isinstance(x, list):
#             newl.extend(flatten_list(x))
#         else:
#             newl.append(x)
#     return newl


# print(flatten_list([1, [2, [3, 4], 5], 6]))

# DRY RUN
