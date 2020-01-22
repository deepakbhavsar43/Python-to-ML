# all values of this list are true
# non-zero values are considered true
lis1 = [10, 5, 15, 77]
print(all(lis1))

# all values are false
# 0 is considered as false
lis2 = [0, False, 0]
print(all(lis2))

# one value is false, others are true
lis3 = [10, 0, 40]
print(all(lis3))

# one value is true, others are false
lis4 = [0, 0, True]
print(all(lis4))

# empty iterable - no elements
lis5 = []
print(all(lis5))

# Output:
# True
# False
# False
# False
# True