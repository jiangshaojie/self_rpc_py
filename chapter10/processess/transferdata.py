from multiprocessing import Queue,Process

def run(qq):
    qq.put(["hello",None,1])
    print("{} run...".format(str(qq)))

if __name__=='__main__':
    q=Queue()
    p=Process(target=run,args=(q,))
    p.start()
    print(q.get())
    print("mian process start...")

