from threading import Thread
from time import sleep

def wait(v: int):
    sleep(v)
    print(v)

lst = [5, 8, 3, 7, 2, 1]
[Thread(target=wait, args=(v,)).start() for v in lst]
