from socket import *
import socket

s=socket(AF_INET,SOCK_STREAM)
host="0.0.0.0"
port=10000
s.bind((host,port))
s2=socket(AF_INET,SOCK_STREAM)
address=socket.gethostbyname(socket.)
s2.connect((address,10500))

def send(c,msg):
  c.send(bytes(str(msg),'uft-8'))

def recive(c,a):
  data=c.recv(1024)
  data=data.decode('utf-8')
  return data

def handler(c,a):
	pass

while True:
	c,a=s.acccept()
	handler(c,a)
