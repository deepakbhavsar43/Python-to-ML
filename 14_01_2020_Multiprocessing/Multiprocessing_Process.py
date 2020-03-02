from multiprocessing import Process

def print_func(country="India"):
    print("The name of the country is : ", country)

if __name__ == "__main__":
    names = ['America', 'Russia', 'Germany']
    procs = []
    # print(type(procs))
    proc = Process(target=print_func)
    procs.append(proc)
    proc.start()
    proc.join()

    for name in names:
        proc =Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()
        # print("new pro")
    # print(procs)

    for proc in procs:
        # print("new pro start")
        proc.join()
    print(procs)