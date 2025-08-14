# ZeroDivisionError: division by zero
# print(10 / 0)

# ValueError
# x = int(input("Enter a Number: "))
# print("x", x)

# print("Hello World!!!!!!!!!!!!!!!")

# IndexError: list index out of range
# x = [1, 2, 3, 4, 5]
# print(x[6])

# ............................................................
# try-except Block
# x = int(input("Enter a number: "))
# try:
#     a = 10 / x
#     print(a)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# ..........................................................
# Multiple-except block

# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     print(a)
# except ValueError:
#     print("Give Number as Input instead of Characters!....")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# print("Continue....")
# print("Continue....1")
# print("Continue....3")


# ................................................................
# catching multiple excaptions together
# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     print(a)
# except (ValueError, ZeroDivisionError) as e:
#     print("Error: ", e)
# ................................................................
# Generic exception handling
# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     z = [1, 2, 3, 4, 6]
#     print(a)
#     print(z[10])
# except Exception as e:
#     print("Error: ", e)
# ................................................................
# finally
# try:
#     x = int(input("Enter a number: "))
#     a = 10 / x
#     z = [1, 2, 3, 4, 6]
#     print(a)
#     print(z[10])
# except Exception as e:
#     print("Error: ", e)
# finally:
#     print("We are handling all types of error")
# .................................................................
# Raising Error
# def divide(a, b):
#     if b == 0:
#         raise ValueError("b cannot be zero")
#     return a / b


# divide(10, 0)
# ..............................................................
