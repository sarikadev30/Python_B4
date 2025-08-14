# Tuple
# Creating
# x = (1, 2, 3, "Sam", True, 34.09)
# print(x, type(x))
# Indexing Possible => Slicing Possible
# print(x[1])
# print(x[2:5])
# print(x[-1])

# Updation Not possible
# x.append(5)
# print(x)

# Loop
# for i in x:
#     print(i)

# for i in range(len(x)):
#     print(x[i])

# MErging
# y = (1, 4, 90, 34, 12, 23, "sam")
# t1 = x + y
# print(t1)
# .................................................................................
# K = (1, 6, 7, 40, 0, 4, 66, 46, 33, 89, "Danny", (1, 4, 3, 5), [1, 4, 6])
# print(K[-1:-4:-1])

# z = tuple([1, 2, 3, 4, 6, 9])
# print(z, type(z))

# .................................................................................

# Addition Using List
# x = (1, 2, 3, "Sam", True, 34.09)
# y = "Danny"
# z = list(x)
# z.append(y)
# z[1] = 23
# z = tuple(z)
# print(z, type(z))
# .................................................................................
# Dictionary
# CRUD
# CREATE
# 1.
a = {"Sam": 1, "Danny": 45, "Leo": 9, "Sam": 45}
# 2.
c = dict({"name": "Danny", "age": 34, "isRegular": True})
# print(a, type(a), c, type(c))

# READ
# print(c["age"])
# print(len(c))

# Loop
# for i in c:
#     print(i, c[i])

# d = {
#     "name": ["Anny", "Bunny", "Danny", "Enav"],
#     "age": [25, 36, 22, 12],
#     "income": [90, 75, 80, 93],
# }

# print(d["name"][2])
# print(f"{d["name"][2]} - {d['age'][2]} - {d['income'][2]}")
# print(d["name"][len(d["name"]) - 1], " - ", d["age"][len(d["name"]) - 1])
# .............................................................................
# UPDATE

# replaced value
a["Sam"] = 49
# # add new value
a["Joy"] = 56
# print(a)

# ............................................................................
# DELETE
# pop => remove using key
# a.pop("Joy")
# print(a.pop("Joy"))
# print(a)

# popitem
# a.popitem()
# print(a.popitem())
# print(a)
# clear => clear all the key value pairs
# c.clear()
# print(c)
# del
# del c
# print(c)

# .......................................................
# Functions
# get
print(a.get("Danny"))
print(a.get("Dany", "Not Present"))

# keys
print(a.keys())
# values
print(a.values())

for i in a.values():
    i += 1
    print(i)

# items
print(a.items())
for key, value in a.items():
    print(key, value)
