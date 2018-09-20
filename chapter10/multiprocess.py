#coding:utf-8
import json
import struct
import socket
import multiprocessing

def hannle_conn(conn,addr,handlers):
    print(addr,"comes")
    while True:
        length_prefix=conn.recv(4)
        if not length_prefix:
            print(addr,"bye")
            conn.close
            break
        length,=struct.unpack("I",length_prefix)
        body=conn.recv(length) #请求消息体
        try:
            request=json.loads(body)
            in_ = request['in']
            params = request['params']
            print(in_, params)
            handler = handlers[in_]
            handler(conn, params)
        except json.decoder.JSONDecodeError as e:
            # print(json.decoder.JSONDecodeError.msg)
            print("json解析失败")
            # pass


def loop(sock,handlers):
    while True:
        conn,addr=sock.accept()
        p=multiprocessing.Process(target=hannle_conn,args=(conn,addr,handlers))
        p.start()
        p.sock.close()
        # hannle_conn(conn,addr,handlers)

def ping(conn,params):
    send_result(conn,"pong",params)

def send_result(conn,out,result):
    response=json.dumps({"out":out,"result":result})
    length_prefix=struct.pack("I",len(response))
    conn.sendall(length_prefix)
    conn.sendall(bytes(response,encoding='utf-8'))

if __name__=='__main__':
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建TCP套接字
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind(('127.0.0.1',8800))
    sock.listen(1)
    handlers={
        "ping":ping
    }
    loop(sock,handlers) #进入服务循环
