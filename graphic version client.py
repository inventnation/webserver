import socket,time
from tkinter import *
from subprocess import call

window=Tk()
window2=Tk()
window.configure(background="black")
server_down=0
def win_name(name,sec_win=0):
  if sec_win==0:
    window.title(str(name))
  else:
    window2.title(str(name))
win_name("client connecting...",0)
webserver_owner=0
chat_admin=0
chatroom=0
chatroom_name=""
username=""
file_size=0
global file_transfer
file_transfer=0
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=socket.gethostbyname(socket.getfqdn())
connection=0
try:
  s.connect((address,10250))
  connection+=1
except:
  win_name("client connection failed")
  Label(window,text="a connection could not be established to the servers",font="none 24 bold").grid(row=0,column=0,sticky=E)
def send(msg):
  s.send(bytes(str(msg),'utf-8'))
def recive():
  data=s.recv(1024)
  data=data.decode('utf-8')
  return str(data)
def exiting(win=0):
  if win==0:
    window.destroy()
  elif win==1:
    pass
def main_gui():
  window.protocol("WM_DELETE_WINDOW", window.iconify)
  pass
def server_established():
  setup=0
  while setup!=2:
    response=recive()
    if response=="type?":
      send("Graphic Client")
    elif response=="setted up?":
      file=open("./client data.txt")
      ans=file.readline()
      ans=int(ans)
      if ans==0:
        send("no")
      elif ans==1:
        send("yes")
      setup+=1
    elif response=="list num?":
      ans=file.readline()
      send(int(ans))
      setup+=1
  login()
def login():
  try:
    win_name("client login",1)
    exit2=0
    while exit2!=1:
      Label(window2,text="Password: ",font='none 12 bold').grid(row=0,column=0,sticky=E)
      test=Entry(window2,width=30,bg="white")
      test.grid(row=0,column=1,sticky=E)
      def click():
        text2=test.get()
        send(text2)
        ans=recive()
        if ans=="correct":
          Label(window,text="password correct Welcome",fg="green",font="none 12 bold").grid(row=0,column=0,sticky=S)
          window2.destroy()
        elif ans=="wrong":
          Label(window2,text="Password wrong,Try again...",fg="red",font="none 12 bold").grid(row=2,column=0,sticky=S)
      Button(window2,text="SUMMIT",width=6,command=click).grid(row=1,sticky=E)
      window2.mainloop()
  except:
    pass
server_established()
main_gui()
window.mainloop()
setup=0
