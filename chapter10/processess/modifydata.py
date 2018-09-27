from multiprocessing import Process,Manager
import os

def run(d,l):
    d[os.getpid()]=os.getpid()
    l.append(os.getpid())
    print(l)

if __name__=='__main__':
    manger=Manager()
    l=manger.list(range(5))
    d=manger.dict()
    p_odj=[]

    for i in range(10):
        p=Process(target=run,args=(d,l))
        p.start()
        p_odj.append(p)
    for p in p_odj:
        p.join()

    print(l,d)


