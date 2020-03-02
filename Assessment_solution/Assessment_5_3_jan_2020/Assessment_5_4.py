#not yet done
def fact(n):
    temp = 0
    if n!=0:
        r = n%10
        q = n//10
        # fact(q)
        # print('value of r : ', r)
        # print('value of q : ', q)
        temp = r + fact(q)
    # print('value of temp : ',temp)
    return temp


# temp=0
num = int(input("Enter a number : "))
# fact(num)
print("The sum of all the digit in the given number is : ",fact(num))