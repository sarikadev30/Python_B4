"""
....*
...***
..*****
.*******
*********

"""

# i => rows
# j=> columns
# k => spaces

# i=1  s=> 4  (n-i)     st=        (2*i-1)
# i=2  s=> 3
# i=3  s=> 2
# i=4  s=> 1             stars=7
# i=5  s=>0              stars=9

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         if i == 0 or i == n or k == 0 or k == 2 * i - 2:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


"""

*********
.*******
..*****
...***
....*

"""


"""
....*
...***
..*****
.*******
*********


....*
...* *
..*   *
.*     *
*********
"""

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):  # 0 => 2*i-1-1 2*i-2
        if i == 1 or i == n or k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


print(chr(66))

"""
*
* *
* * *
* * * *
* * * * *

A
B B
C C C
D D D D
E E E E E

"""
