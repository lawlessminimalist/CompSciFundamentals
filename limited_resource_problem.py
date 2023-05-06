from threading import BoundedSemaphore, Thread
import time
import random
connectionHandler = BoundedSemaphore(value=10)

class connectionRequester(Thread):
    def __init__(self,connectionHandler:BoundedSemaphore,requesterID:int) -> None:
        super().__init__()
        self.connectionHandler = connectionHandler
        self.requesterID = requesterID

    def access_database(self):
        print(f"Requester {self.requesterID}: Attempting Connection")
        with connectionHandler:
            print(f"Requester {self.requesterID}: Connected to DB")
            time.sleep(random.randint(1,10))

    def run(self) -> None:
        self.access_database()
    
requesters = [connectionRequester(connectionHandler,i) for i in range(200)]

for requester in requesters:
    requester.start()

for requester in requesters:
    requester.join()

