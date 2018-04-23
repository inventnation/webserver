from socket import *
from threading import Thread

s=socket(AF_INET,SOCK_STEAM)
host="127.0.0.1"
port=10500
s.bind((host,port))

connecting=[]
all_clients=[]
client_name=[]
client_converter={}
public_webserver={}
public_webserver_names=[]
WIP_webservers={}
WIP_webservers_names=[]

def send(c,msg):
	c.send(bytes(str(msg),'utf-8'))

def recive(c):
	data=c.recv(1024)
	data=data.decode('utf-8')
	return data

def handler(c,a):
  pass

def webserver_commands(c,a):
	pass

def command():
	pass

def connectin_checker(c):
	pass

def admin():
	pass

while True:
	c,a=s.accept()
	connecting.append(c)
	connection_checker(c,a)
	connecting.remove(c)
	handler(c,a)
