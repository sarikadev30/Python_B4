# NESTED LOOP

# for i in range(1, 6):
#     for j in range(1, 4):
#         print(f"Guest {i} ate Candy {j}")

# for i in range(2):  # 0 1
#     for j in range(3):  # 0 1 2
#         print("Hello")

# i=0  => j= 0 Hello j=> 1 Hello j=>2  Hello
# i=1  => j= 0 Hello j=> 1 Hello j=>2  Hello
# i=2

# i = 0

# while i < 2:  # i => 0 1
#     j = 0
#     while j < 3:  # 0 1 2
#         print("Hello", i, j)
#         j += 1
#     i += 1

# i=0 => j=0 0<3 => Hello 0 0 => j=1 Hello 0 1 => j=2 Hello 0 2 j=3    => i=1
# i=1 => j=3 3<3 => False
#  i=1 => j=0 0<3 => Hello 1 0 => j=1 Hello 1 1 => j=2 Hello 1 2 j=3    => i=2
# .....................................................................................................

# Father gave the son a target, of completing 10 sets. Each set contains 10 Rounds of a field.

# ..................................................................................................
# PATTERN PROBLEMS

"""

**********
**********
**********
**********
**********

"""
# for i in range(5):
#     for j in range(10):
#         print("*", end="")
#     print()

"""

0123456789
0123456789
0123456789
0123456789
0123456789

"""

"""
12345678
12345678
12345678
12345678
12345678
"""

"""
111111
222222
333333
444444
555555
"""

"""
*
* *
* * *
* * * *
* * * * *

"""

# for i in range(1, 4):
#     for j in range(i):
#         print("*", end=" ")

#     print()

"""
1
12
123
1234
12345
123456

"""

# for i in range(1, 7):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

# for i in range(1, 7):
#     for j in range(i):
#         print(j + 1, end="")
#     print()

"""
1
22
333
4444
55555
666666
"""

"""

******
*****
****
***
**
*

"""

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print(k, end="")
#     print()
