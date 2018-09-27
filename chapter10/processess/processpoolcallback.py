from multiprocessing import Pool
import time
import os
def run(i):
    print("child process",i)
    time.sleep(1)
    return i
def bar(args):
    print("bar pid",os.getpid())
    print("bar funciton %s" %args)

if __name__=='__main__':
    pool=Pool(3)
    print("main pid",os.getpid())
    for i in range(10):
        p=pool.apply_async(func=run,args=(i,),callback=bar)

    print("end")
    pool.close()
    pool.join()
