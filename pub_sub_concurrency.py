from threading import Lock,Condition,Thread
import queue
import random
import time


def publish(cv:Condition,shared_buffer:queue.Queue):
    for _ in range(200):
        with cv:
            while shared_buffer.full():
                cv.wait()
            num = random.randint(0,200)
            shared_buffer.put(num)
            cv.notify_all()
            print(f"Produced: {num}")
        time.sleep(0.1)






def consume(cv:Condition,shared_buffer:queue.Queue):
    for _ in range(200):
        with cv:
            while shared_buffer.empty():
                cv.wait()
            print(f"Consumed:{shared_buffer.get()}")
            cv.notify_all()
        time.sleep(0.1)




shared_buffer = queue.Queue(maxsize=5)
cv = Condition()

producer = Thread(target=publish, args=(cv, shared_buffer))
consumer = Thread(target=consume, args=(cv, shared_buffer))

producer.start()
consumer.start()

producer.join()
consumer.join()