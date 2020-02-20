import psutil


class MyProcess:
    def __init__(self):
        # Total CPU Cores
        print(psutil.cpu_count())

    def Running(self):
        # Iterate over all running process
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                processID = proc.pid
                print(processID, ' ::: ', processName)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    # def Memory(self, proc):
    # self.mem = proc.memory_info().rss()
    # return self.mem


if __name__ == "__main__":
    obj1 = MyProcess()
    obj1.Running()
