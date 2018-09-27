#coding:utf-8
import json
import time
import struct
import socket
from multiprocessing import Pool

def rpc(sock,in_,params):
    response=json.dumps({"in":in_,"params":params})
    length_prefix=struct.pack("I",len(response))
    sock.sendall(length_prefix)
    sock.sendall(bytes(response,encoding='utf-8'))
    length_prefix=sock.recv(4)
    length,=struct.unpack("I",length_prefix)
    body=sock.recv(length)
    response=json.loads(body)
    return response["out"],response["result"]
def clientrequest(s):

    for i in range(10):
        out,result=rpc(s,"ping","ireader %d" % i)
        print(out,result)
        time.sleep(2)

def sss(s):
    pool = Pool(8)
    # for i in range(10):
    for i in range(10):

     p = pool.apply_async(func=clientrequest, args=(s,))
if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',8080))
    sss(s)
    # pool.start
    # for i in range(10):
    #     out,result=rpc(s,"ping","ireader %d" % i)
    #     print(out,result)
    #     time.sleep(2)
    s.close()