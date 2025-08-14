# def printF():
#     print("Hello World!...")
# def addF():
#     x = 90
#     y = 78
#     print(x + y)
# addF()
# printF()
# addF()
# printF()
# addF()

# def addFun(x, y):
#     print(x + y)

# addFun(12, 34)
# addFun(10, 20)

# def mulFun(x, y, z):
#     print(x * y * z)

# mulFun(3, 2, 6)


# Default Argument
# def PrintData(x, y=18):
#     print(x, y)


# PrintData("Sam", 32)
# PrintData("Danny")
# # PrintData(34, "Joe")


# Variable Length Arguments
# def Sum(*t):
#     print(t)
#     print(sum(t))


# Sum(1, 2)
# Sum(1, 2, 7, 9)

# KeyWorded Arguments


# def personData(name, city):
#     print(name, city)


# personData("Sam", "Delhi")
# personData(city="Delhi", name="Sam")

"""
PROBLEM-1
Personalized Greeting
Write a function called `greet` that takes a name as a parameter and prints `"Hello, [name]!"`.

greet("Sam")=> Hello, Sam!
"""


# print  =>
# return =>
# def remainder(x, y):
#     print(x % y)


def remainder(x, y):
    return x % y
    print("Hello!...........")


a = 12
c = 78
b = "Hi!...........Python"
print(a)
print(b)
d = remainder(12, 5)
print(d)
# print(remainder(12, 5))
print(c)

# 0 1 1 2 3 5 8 13......
# a b c
#   a b


def fib(n):
    a = 0
    b = 1
    res = []
    for i in range(n):  # 0 1 2 3 4
        res.append(a)
        c = a + b
        a = b
        b = c
    return res


print(fib(8))
