# DELETE
# x = [1, 2, 3, 4, 5, 6, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2]

# pop => Removes by Index
# print(x.pop(), x)
# print(x.pop(-2), x)
# remove  => Removes by Value
# If multiple values , removes only first iteration
# x.remove(2)
# print(x)
# .....................................................................

# stationary = []
# stationary.extend(["pen", "pencil", "notebooks", "marker", "Eraser", "Sharpner"])
# print(stationary)
# stationary.remove("marker")
# print(stationary)
# stationary.pop(2)
# print(stationary)
# stationary.pop()
# print(stationary)

# .......................................................

# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman"]
# for i in range(len(movies)):
#     if i == 3:
#         break
#     print(movies[i])


# ...............................................................................
# movies = ["bahubali", "Spider-Man", "Iron Man", "Superman", "Thor", "Avengers"]
# for i in range(len(movies)):
#     print(movies[i])
#     if i == 2 or i == 4:
#         continue

# .............................................................................

# x = [10, 5, 8, 12, 3]
# print(max(x))
# print(min(x))
# print(sum(x))
# mx = x[0]  # 10 => 12
# for i in range(1, len(x)):
#     if x[i] > mx:
#         mx = x[i]

# print(mx)
# .........................................................................
# Inbuilt Functions
# min
# max
# sum
# len()

x = [1, 3, 4, 2]
firstMax = secondMax = float("-inf")
for i in range(len(x)):
    if x[i] > firstMax:
        secondMax = firstMax
        firstMax = x[i]
    elif firstMax > x[i] > secondMax:
        secondMax = x[i]

print(firstMax, secondMax)

# fM=-inf  sM=-inf
# i=0   1>-inf => sM=fM=-inf fM=1
# i=1   3>1 => sM=fM=1      fM=3
# i=2   4>3 => sM=fM=3      fM=4
# i=3   2>4 => fM>2>sM 4>2>3
