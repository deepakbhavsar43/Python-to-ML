import time

def logtime(func):
    def wrapper(*args):
        start_time = time.time()
        print("Execution started at : ", start_time)
        func(*args)
        end_time = time.time()
        print("Execution ended at : ", end_time)
        total_time=end_time-start_time
        print("Total time taken for execution : ", total_time)
        print("\n\n")

        with open("LogTime.txt",'a',encoding='UTF-8') as LFile:
            LFile.write("For function {} total time required for execution is {}.\n".format(func.__name__, total_time))
    return wrapper

@logtime
def add(x, y):
    time.sleep(3)
    print("ADDITION")
    print(x+y)

@logtime
def sub(x, y):
    time.sleep(4)
    print("SUBTRACTION")
    print(x-y)

add(1, 2)
sub(1, 2)