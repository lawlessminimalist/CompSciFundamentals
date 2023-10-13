from threading import Lock,Thread
import time
# Task
# Extend threading class and simulate philosphers
# each philospher has one chopstick between themself and another
# | . | . | . | . | .

# Made up terms
# num of philosphers = nop
# num of chopsticks = nchop

# Assumptions:
# 1. nop > 1 otherwise no deadlock
# 2. sitting at round table, meaning if three nop then two nchop

nop = 5
chopsticks = [Lock() for _ in range(nop)]

class philosopher(Thread):
    def __init__(self,index,chopsticks) -> None:
        # Call the init on the Thread class
        super().__init__()
        self.index = index
        self.chopsticks = chopsticks
    

    def run(self) -> None:
        # Scheduling threads work here
        # Naive - no deadlock prevention
        chopstick_left:Lock = self.chopsticks[self.index]
        chopstick_right:Lock = self.chopsticks[(self.index+1)%len(self.chopsticks)]
        if self.index == len(chopsticks)-1:
            first_chopstick, second_chopstick = chopstick_left, chopstick_right
        else: 
            first_chopstick, second_chopstick = chopstick_right, chopstick_left

        for _ in range (10):
            # Give the other thread's a chance to acquire the lock
            time.sleep(.5)
            with first_chopstick:
                with second_chopstick:
                    time.sleep(.3)
                    print(f"Philospher {self.index} working")


philosophers = [philosopher(i, chopsticks) for i in range(nop)]

# Start and join the philosopher threads
for philosopher in philosophers:
    philosopher.start()

for philosopher in philosophers:
    philosopher.join()