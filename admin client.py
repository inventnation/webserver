import socket,time
from threading import Thread

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname(socket.getfqdn())
try:
  s.connect((host,10500))
except:
  print("main server is not on")
  time.sleep(4)
  exit()
data=s.recv(1024)
data=data.decode('utf-8')
if data=="type?":
  s.send(bytes("Admin client",'utf-8'))
else:
  print("main server did not allow to establish a proper connection protocall so you need to fix that and i am closeing my self bye")
  time.sleep(8)
  exit()
def send_command():
  while True:
    command=input("Command: ")
    s.send(bytes(str(command),'utf-8'))
def handler():
  while True:
    try:
      data=s.recv(2048)
      data=data.decode('utf-8')
    except:
      print("you are disconnected from the main server")
      time.sleep(6)
      break
    print(data)
display=0
while True:
  if display==0:
    print("connection is established to the main server and is ready to read commands!")
    display+=1
    s1=Thread(target=send_command)
    s1.start()
    h1=Thread(target=handler)
    h1.start()  
