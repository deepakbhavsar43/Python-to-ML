def mydecorator(msg='message'):
    def decorated(f):
        def wrapper(*args):
            print('The message is : '+ msg)
            print("Inside decorator before calling function.")
            f(*args)
            print("Inside decorator after calling function.")
        return wrapper
    return decorated



@mydecorator(msg='Hello')
def printname(name,surname):
    print(name+" "+surname)


str_MyName = "Deepak"
str_lastName = "Bhavsar"
printname(str_MyName, str_lastName)