# x = [1, 2, 3, 4, "Sari", True]
# print(" ".join([str(i) for i in x]))
# ......................................................
# SETS
# x = {4, 21, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 36}
# c = type(x)
# print(c, x)
# print(x[2:3])  # Slicing and Indexing not possible

# Searching
# print(21 in x)
# print(1 not in x)

# functions in sets

# arr = [1, 2, 3, 4, 5, 5, 6, 1, 2, 3, 8, 2, 1, 4]

# List to Set
# a = set(arr)
# print(a, type(a))

# Set to List
# x = {4, 21, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 36}
# b = list(x)
# print(b, type(b))

# Another way to create the List
# c = set((1, 2, 3, 4, 1, 2, 4, 3, 1, 3, 4))
# print(c, type(c))

# CRUD
# Create

# Read
# Loop
# for i in c:
#     print(i, end=" ")

# Update
# Add Element to the list
# c.add(5)
# c.add(0)
# c.add(4) # =>duplicate value not added
# print(c)

# Delete
# remove  => If value is not there, it will raise the error
# c.remove(1)
# c.remove(5)
# print(c)

# discard => If value is not there, it wont raise the error
# c.discard(4)
# c.discard(5)
# print(c)

# clear
# c.clear()
# print(c)

# Add list to the set
# x = [1, 2, 3, 4]
# a = {9, 7, 8, 6, 5}
# print(a, x)
# a.update(x)
# print(a)

# ................................................................
# letters = set("mississippi")
# print(letters, len(letters))
# letters.pop()
# print(letters, len(letters))
# print(letters.pop(), letters)
# letters.pop()
# print(letters)


# .......................................................
# nums = {2, 3, 4, 5, 1}
# print(nums.copy())
# for i in nums.copy():
#     if i > 3:
#         nums.remove(i)

# print(nums)
# nums = {i for i in nums if i < 3}
# print(nums)
