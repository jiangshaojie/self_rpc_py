from multiprocessing import Process,Pipe
import time
def run(conn):
    conn.send("from child process....")
    conn.send("from child process...2")

    print("child process")

if __name__=='__main__':
    parent_conn,child__conn=Pipe()
    p=Process(target=run,args=(child__conn,))
    p.start()
    time.sleep(10)
    child__conn.send("666")

    p.join()

    print("from child",parent_conn.recv())
    print("from child",parent_conn.recv())
    # child__conn.send("666")
    print(parent_conn.recv())