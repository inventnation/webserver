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

def recive(c,a):
	try:
		data=c.recv(1024)
		data=data.decode('utf-8')
		return data
	except:
		print("Connection: "+a[0]+" : "+a[1]+" disconnected")

def handler(c,a):
  pass

def webserver_commands(c,a):
	pass

def command():
	pass

def connectin_checker(c):
	send(c,"type?")
	ans=recive(c,a)
	if ans=="Clinet":
		send(c,"Setted up?")
		ans=recive(c,a)
		if ans=="yes":
			send(c,"list num?")
			ans=recive(c,a)
			line_num=0
			password=""
			username=""
			with open("./Main server data/usernames.txt") as f:
				for line in f:
					if line_num==ans:
						username+=line
						break
					else:
						line_num+=1
			line_num=0
			with open("./Main server data/passwords.txt") as f:
				for line in f:
					if line_num==ans:
						password+=line
						break
					else:
						line_num+=1
			while True:
				
	elif ans=="Web server":
		pass

def admin():
	pass

while True:
	c,a=s.accept()
	connecting.append(c)
	connection_checker(c,a)
	connecting.remove(c)
	handler(c,a)
