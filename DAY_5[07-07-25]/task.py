# Conditional Statements
# if
# if-else
# if-elif-else


# if (condition1):
#     print("Statement 1")
# elif (condition2):
#     print("Statement 2")
# else:
#     print("Statement 3")


# ............................................................
# to check number is positive, negative or zero
# x = int(input("Enter a number : "))
# if x > 0:
#     print("Positive")
# elif x < 0:
#     print("Negative")
# else:
#     print("Its Zero")

# ................................................
# Print "In Range" if the number is in between 20 and 30
# <20  Below
# >30  Above
# 20 or 30  Equal
# ........................................................................
# Problem-I
# - My mother told me to get all of the things if available from the market
# 1. If Rice is available then print Buy rice
# 2. If wheat is available then print buy wheat
# 3. If apple is available then print buy apple
# riceAvailability = True
# wheatAvailability = False
# appleAvailability = True
# ........................................................................
# Nested IF
# Voting Eligibility with ID Check
# Voting age in India is 18. Voter must also have a voter ID.

# age = int(input("Enter age: "))

# if age >= 18:
#     idCheck = input("Do you have a Voter Id ? (yes/no) :").lower()
#     if idCheck == "yes":
#         print("Eligible")
#     else:
#         print("Not Eligible")
# else:
#     print("Not Eligible")

z = 0
# if z > 0:
#     print("Positive")
# else:
#     print("Not Positive")

# Ternary Operator
# print("Positive") if z > 0 else print("Not Positive")

# if z>0:
#     print("Positive")
# elif z<0:
#     print("Negative")
# else:
#     print("Zero")

print("Positive") if z > 0 else print("Negative") if z < 0 else print("Zero")
