from multiprocessing import Process, Queue
import time

class Test:
    def __init__(self):
        self.cnt = 0

    def say_hello(self):
        print(self.cnt, "Hello!")
        self.cnt += 1

def executor(test):
    test.say_hello()
    time.sleep(1)


if __name__ == "__main__":
    test = Test()
    executor(test) # normal execute

    executor(test) # normal execute

    p = Process(target=executor, args=(test,))
    p.start() # multiprocessing
    p.join()


    q = Process(target=test.say_hello)
    q.start() # multiprocessing
    q.join()

    executor(test) # normal execute