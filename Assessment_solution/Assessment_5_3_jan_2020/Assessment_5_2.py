def pattern(i, n):
    if i<=n:
        print(i, end="")
        i=i+1
        # print("i after increment : ", i)
        pattern(i, n)

# global i
# i=0
num=int(input("Enter a integer : "))
pattern(1, num)