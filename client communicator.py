import socket,time
from threading import Thread
from socket import *

servers=[]
s=socket(AF_INET,SOCK_STREAM)
host="0.0.0.0"
port=10000
s.bind((host,port))
s2=socket(AF_INET,SOCK_STREAM)
address=socket.gethostbyname(socket.getfqdn())
s2.connect((address,10500))

def main_send(msg):
	s2.send(bytes(str(msg),'utf-8'))

def main_recive():
	data2=s2.recv(1024)
	data2=data2.decode('utf-8')
	return data2

lol=main_recive()
if lol=="type?":
	main_send("Client Communicator")
else:
	print("did not get type? command form main server shutting down...")
	time.sleep(3)
	exit()

def send(c,msg):
  c.send(bytes(str(msg),'uft-8'))

def recive(c,a):
  data=c.recv(1024)
  data=data.decode('utf-8')
  return data

def handler(c,a):
	pass

def server_checker():
	while True:
		servers.clear()
		main_send("Comm: send serverslist")
		serv_list=main_recive()
		serv_list=str(serv_list).split(",")
		server=0
		for serv in serv_list:
			server+=1
			servers["Server: "+str(server)]=serv
		time.sleep(1200)

sc=Thread(target=server_checker)
sc.start()
while True:
	c,a=s.acccept()
	handler(c,a)
