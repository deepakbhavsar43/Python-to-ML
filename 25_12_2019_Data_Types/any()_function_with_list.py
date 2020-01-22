# all values are true
lis1 = [10, 20, 30, 40]
print(any(lis1))

# all values are false
lis2 = [0, False]
print(any(lis2))

# one value is false, others are true
lis3 = [0, 10, 5, 15]
print(any(lis3))

# one value is true, others are false
lis4 = [10, 0, False]
print(any(lis4))

# empty iterable
lis5 = []
print(any(lis5))

# Output:
# True
# False
# True
# True
# False