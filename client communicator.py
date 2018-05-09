import socket,time
from threading import Thread
from socket import *

servers=[]
clients=[]
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
	send(c,str(servers).replace("[","").replace("]","").replace(",","\n"))
	while True:
		data=recive(c,a)
		if data[0:1]=="$":
			data2=data[1:]
			if "connect "in data2[0:8]:
				pass
			elif data2=="list_servers":
				send(c,str(srvers).replace("[","").replace("]","").replace(",","\n"))
			elif data2=="man_update":
				main_send("Comm: send serverslist")
				serv_list=main_recive()
				serv_list=str(serv_list).split(",")
				send(c,str(serv_list).replace("[","").replace("]","").replace(",","\n"))
			elif data2=="help":
				print("""help-list commands
connect -connects you to a server EX:connect server0,me (you don't type this part in but the reason it allows you to do that is to drag people into the same server as you if you know their ip address)
list_server-list servers that it alredy has listed
man_update-manually updates it for your eyes only it does not update the server list for everyone and will list it to you
exit-exits you from the communicator SAFELY AND IT'S RECOMMANDED TO DO THIS""")
			elif data2=="exit":
				send(c,"thank you for useing the communicator even if you did not get in to a server probably goob-bye!")
				send(c,"you are safe to close the program")
				c.close()

def server_checker(c,a):
	while True:
		servers.clear()
		main_send("Comm: send serverslist")
		serv_list=main_recive()
		serv_list=str(serv_list).split(",")
		server=0
		for serv in serv_list:
			server+=1
			servers.append(serv)
		time.sleep(1200)
		for client in clients:
			send(client,"theres an updated version of the servers list would you would need to type $list_servers you got to wait 10 secs beofere manually update the servers list")

while True:
	c,a=s.acccept()
	clients.append(c)
	sc=Thread(target=server_checker,args=(c,a)
	sc.start()
	handler(c,a)
