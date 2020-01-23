#not yet done
def fact(n):
    r = n%10
    q = n//10
    temp = temp + r
    fact(q)
    # print(r)
    # print(q)


num = int(input("Enter a number : "))
fact(num)
# print(fact(num))