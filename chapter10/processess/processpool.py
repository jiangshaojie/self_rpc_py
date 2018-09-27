from multiprocessing import Pool
import time

def run(i):
    print("child process",i)
    time.sleep(100)

if __name__=='__main__':
    pool=Pool(10)

    for i in range(10):
        P=pool.apply_async(func=run,args=(i,))

    print("end...")
    pool.close()
    pool.join()

