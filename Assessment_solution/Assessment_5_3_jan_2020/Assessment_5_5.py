def fact(n):
    if n<=0:
        print("Enter number greater than 0.")
    elif n==1:
        return n
    else:
        return n*fact(n - 1)


num = int(input("Enter a number : "))
result = fact(num)
print(result)