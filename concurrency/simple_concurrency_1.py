from threading import Lock,Thread,Event

## Two Threads ##
# T1: incrememnt var
# T2: print var
# objective: print var before it's modified using a lock or event

class Locks1:
    def __init__(self) -> None:
        self.count = 0
        self.pen = Lock()
        self.event = Event()

    def incrementVar(self):
        for _ in range(10):
            with self.pen:
                self.count +=10

    def printVar(self):
        for _ in range(10):
            with self.pen:
                print(self.count)

functions = Locks1()

T1 = Thread(target=functions.incrementVar)
T2 = Thread(target=functions.printVar)

T1.start()
T2.start()
T1.join()
T2.join()





