#!/usr/bin/env python
__author__ = 'webber'
import os,time
import multiprocessing

# worker function
def worker(sign, lock):
    lock.acquire()
    print (sign, 'pid:',os.getpid())
    lock.release()
    time.sleep(1)

# Main
print ('Main:',os.getpid())

plist = []
lock = multiprocessing.Lock()
for j in range(5):
    p = multiprocessing.Process(target=worker,args=('process',lock))
    p.start()
    plist.append(p)
p.join()