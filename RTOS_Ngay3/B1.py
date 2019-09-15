import threading
import time


def thread_1():
    t1 = 0
    while(True):    
        t1 += 1
        print ("toi la t1, L" + str(t1))
        time.sleep(2)

def thread_2():
    t2 = 0
    while (True):
        t2 += 1
        print ("toi la t2, L" + str(t2))
        time.sleep(3)


thread1 = threading.Thread(target=thread_1)
thread2 = threading.Thread(target=thread_2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
