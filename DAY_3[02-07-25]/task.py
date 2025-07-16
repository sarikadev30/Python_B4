# Comparison Operators

# Greater Than
# a = 90
# b = 9
# print(a > b)
# print(2 > -3)
# print(0 > -2)

# Greater Than n Equal
# print(3 >= 3)

# print(3 == 3.0)     # Implicit Typecasting


# ram = "ram"
# print(5 == 5)
# print("dam" == "dam")
# print(5 == "5")
# print(ram == "ram")
# print(5 == "ram")
# .........................................................
# print(5 == 5)
# print(5 != 5)
# print(6 == "6")
# print(6 != "6")
# print(6 != 7)

# .........................................................
# fan = 5
# a = "fan"
# b = fan
# print(a == b)  # F
# print(a != b)  # T
# .......................................................
# LOGICAL OPERATORS

# AND   => All the expressions need to be True
# print(True and False)
# print(False and False)
# print(False and True)
# print(True and True)

a = 4
b = 5
c = 3
# print(a > b and b > c)
# d = a > b
# e = b > c
# print(d and e)

# OR => Any one Value needs to be true

# print(True or False)
# print(False or False)
# print(False or True)
# print(True or True)

# a = 4
# b = 5
# c = 3
# print(a > b or b > c)

# NOT  => reverses the value

# print(not True)
# print(not False)
# .............................................................
# Problems
# a = 9 < 11  # T
# b = 2 == 3  # F
# c = 10 > 3  # T
# result = a and (b or c)
# print(result)
# .................................................................

# x = 4 <= 4
# y = 10 < 5
# z = not (x and y)
# print(z)


# .................................................................

# m = 0 != 0
# n = 1 == 1
# o = m and not n
# print(o)


# .................................................................

# p = 6 == 6
# q = 5 != 5
# r = not (p or q)
# print(r)

# .................................................................

# p = 10 < 5
# q = 3 == 3
# r = 7 != 7
# result = not (p or q and r)
# print(result)
# .................................................................
a = 70
# print("Positive: ", a > 0)

# even
# print("Even: ", a % 2 == 0)
# odd
# print("Odd: ", a % 2 != 0)

# multiple of 3 or not | divisible by 3
# print(a % 3 == 0)
#  divisible by 5 and divisible by 7
# print(a % 5 == 0 and a % 7 == 0)
# print(a % 35==0)
# ........................................................
# a=2100

# print((a%4==0 and a%100!=0) or (a%4==0 and a%100==0))
# print((a%4==0 and a%100!=0) or (a%400==0))
