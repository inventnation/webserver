from socket import *

s=socket(AF_INET,SOCK_STREAM)
host="127.0.0.1"#change this to your real ip address so i can work
port=10000
s.bind((host,port))#binds host and port so i can be used to check for connections on that port and communicate with that ip address
s.listen(5)#waits for one person to connect to start and waits for another while handleing 1 person

server_ip=[]#holds server ip so the the admins can see what server needs to be disconnected
admin_name=[]#holds the name they give to the main server so they can talk
servers=[]#hold servers for scaning and testing responsiveness
admin_clients=[]#holds admins so they can chat to each other to see what they need to get done
connecting=[]

def send(c,msg):
  c.send(bytes(str(msg),'utf-8'))

def recive(c):
  data=c.recv(1024)
  data=data.decode('utf-8')
  return data

def handler():
  while True:
    command=recive(c)
    if "Server: "in command[0:8]:
      command(c,command[8:])
    elif "Admin: "in command[0:7]:
      admin_commands(c,command[7:])

def command(c,command):
  if command=="test":
    send(c,"responsive!")
  elif "scan "in command[0:5]:
    scanning=command[5:]
    if "chatroom "in scaning[0:9]:
      find=0
      for server in servers:
        send(server,"got: "+str(scaning[9:]))
        ans=recive(server)
        if ans=="yes":
          print("Found a chatroom!")
          find+=1
          break
      if find==0:
        print("Chatroom not found!")
		elif "webserver "in scaning[0:10]:
			find=0
			for server in servers:
				send(server,"got: "+str(scaning[10:]))
				ans=recive(server)
				if ans=="yes":
					print("Found a webserver")
					find+=1
					break
			if find==0:
				print("Webserver not found")

def admin_commands(c,command):
  if command=="test":
		print("responsive!")
	elif "list "in command[0:5]:
		if command[5:]=="admins":
			for admin in admin_name:
				print(str(admin)+"\n")
		elif command[5:]=="servers":
			for server in server_ip:
				print(str(server)+"\n")

def connection_checker(c,a):
  send(c,"type?")
  ans=recive(c)
  if ans=="server":
    servers.append(c)
		server_ip.append(a[0])
    print("Server: "+a[0]+" connected on port: "+a[1])
  elif ans=="admin":
    admin_clients.append(c)
		done=0
		name=""
		while done!=1:
			send(c,"name?")
			ans=recive(c)
			checker=str(ans).replace(" ","")
			if checker=="":
				send(c,"ERROR,NAME,NO BLANKS!")
			else:
				name+=str(ans)
				send(c,"Welcome: "+str(name))
				done+=1
    print("Admin: "+str(name)+" is connected!")

while True:
  c,a=s.accept()
  connecting.append(c)
  conection_checker(c,a)
  connectiong.remove(c)
  handler()
