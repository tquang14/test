import threading
import sys
b = 0
flag = 0

def thread_1():
    global flag
    global b
    while(True):
        a = input("nhap x: ")
        if (a == "exit"):
            flag = 3
            break
        else:     
            b = int(a)
            flag = 1

def thread_2():
    global b
    global flag
    while (True):
        if (flag == 3):
            break
        if (flag == 1):
            if (b % 2 == 0):
                print("so chan: ")
            else:
                print("so le")
            flag = 0

thread1 = threading.Thread(target=thread_1)
thread2 = threading.Thread(target=thread_2)
thread1.start()
thread2.start()