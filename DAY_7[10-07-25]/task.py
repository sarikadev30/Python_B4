# ASSIGNMENT PROBLEM ...........................
# a = 2345
# 2345 => sum+=5 => sum+=4
# sum = 0
# n = a
# while n > 0:
#     r = n % 10
#     sum += r
#     print(r, sum)
#     n = n // 10
#     print(n)

# print("SUm : ", sum)
# ................................................
# FOR LOOP

# for i in sequence:
# statement

# range()
# range(start, end , step)

# for i in range(1, 5, 2):
#     print("Hello World", i)

# step => bydefault => 1
# for i in range(1, 5):
#     print("Hello World", i)

# start => bydefault 0
# for i in range(5):
#     print("Hello World", i)

# for i in range(4, 2, -1):
#     print(i)
# for i in range(5, -1, -1):
#     print(i)
# .....................................................
# Sum of 1 to 10 using for loop
# Factorial of a number
# ....................................................
# FOR LOOP WITH BREAK
# for guest in range(1, 11):
#     if guest == 4:
#         break
#     print("Guest", guest)
# .................................................
# FOR LOOP WITH CONTINUE

# for guest in range(1, 11):
#     if guest == 4:
#         continue
#     print("Guest", guest)
#     print("End........")
#     print("End........")
#     print("End........")

# .................................................
# Arithmetic Progression
a = 2
d = 3
n = 5

# 2, 2+3=5 , 5+3=8 , 8+3=11 , 11+3=14
# a   a+d   a+2*d    a+3*d     a+4*d
# Sum

# i= 0 1 2 3 4
sum = 0
for i in range(n):
    # print(a, i, d, a + i * d)
    sum += a + i * d
print(sum)
