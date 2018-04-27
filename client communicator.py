from socket import *

s=socket(AF_INET,SOCK_STREAM)
host="0.0.0.0"
port=10000
s.bind((host,port))

def send(c,msg):
  c.send(bytes(str(msg),'uft-8')

def recive(c,a):
  data=c.recv(1024)
  data=data.decode('utf-8')
  return data

