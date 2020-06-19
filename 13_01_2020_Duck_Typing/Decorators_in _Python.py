def mydecorator(f):
    def wrapper():
        print("Inside decorator before calling function.")
        f()
        print("Inside decorator after calling function.")
    return wrapper

@mydecorator
def printname():
    print('Deepak')

printname()