#program to accept more arguments that defined in

def addition(a,*b):
    for v in b:
        a=a+v
    return a

print(addition(2,3,1,4,20,5))