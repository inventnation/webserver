import socket,time
from threading import Thread
from subprocess import call

servers={}
connecting_server=[]
admins_connection={}
all_servers=[]
def connection_checker(c,a):
  for connection in connecting_server:
    try:
      connection.send(bytes("type?",'utf-8'))
      data3=connection.recv(1024)
      data3=data3.decode('utf-8')
      if data3=="Server":
        servers[int(a[1])]=c
        print("Server: "+str(a[0])+" : "+str(a[1])+" is connected!")
      elif data3=="Admin client":
        admins_connection[int(a[1])]=c
        print("Admin Client: "+str(a[0])+":"+str(a[1])+" is connected!")
    except:
      print("Connection: "+str(a[0])+" : "+str(a[1])+" disconnected")
def commands(c,a,command):
  if "scan for "in command[0:9]:
    holder=command[9:]
    if "chatroom "in holder[0:9]:
      holder2=holder[9:]
      for server in all_servers:
        server.send(bytes("got chatroom: "+str(holder2),'utf-8'))
        ans=server.recv(1024)
        ans=server.decode('utf-8')
        if ans=="got it":
          print("serch was found")
        elif ans=="no":
          pass
  elif command=="test":
    print("responsive!")
  elif "list "in command[0:5]:
    holder2=command[5:]
    if holder2=="users":
      for server in all_servers:
        server.send(bytes("list users",'utf-8'))
        ans=server.recv(1024)
        ans=server.decode('utf-8')
        print(str(ans).replace("[","").replace("]","").replace(",","\n"))
      print("done")
def admin_commands(c,a,command):
  holder=command
  if "shutdown server "in holder[0:16]:
    
    shutdown_holder=holder[16:]
    try:
      sock_close=all_servers[int(shutdown_holder)]
      all_servers.remove(sock_close)
      c.send(bytes("Main Server:done",'utf-8'))
    except:
      c.send(bytes("Main Server:ERROR: it does not exist in that number!",'utf-8'))
  elif holder=="test":
    print("responsive!")
def handler(c,a):
  while True:
    try:
      data=c.recv(2048)
      data=data.decode('utf-8')
    except:
      print("Connection: "+str(a[0])+" : "+str(a[1])+" disconnected")
      break
    if "Admin "in data[0:6]:
      holder=data[6:]
      admin_commands(c,a,holder)
    elif "Server: "in data[0:8]:
      holder=data[8:]
      commands(c,a,holder)
host="0.0.0.0"
port=10500
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
while True:
  c,a=s.accept()
  connecting_server.append(c)
  connection_checker(c,a)
  all_servers.append(c)
  connecting_server.remove(c)
  a1=Thread(target=handler,args=(c,a))
  a1.demon=True
  a1.start()
