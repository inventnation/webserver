import socket,time,pygame
from threading import Thread
from subprocess import call

webservers={}
webserver_names=[]
all_webservers=[]
client_chat_room={}
usernames={}
user_names=[]
all_clients=[]
chatroom_names=[]
connecting=[]
host="0.0.0.0"
port=10250
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
global exit3
exit3=0
def connection_checker():
  c.send(bytes('type?','utf-8'))
  data3=c.recv(1024)
  data3=data3.decode('utf-8')
  if data3!="Web Server":
    c.send(bytes('setted up?','utf-8'))
    data4=c.recv(1024)
    data4=data4.decode('utf-8')
  if data3=='Web Server':
    c.send(bytes("name?","utf-8"))
    ans=c.recv(1024)
    ans=ans.decode('utf-8')
    ans=str(ans)[2:]
    scan=0
    checker=ans.replace(" ","")
    if checker=="":
      c.send(bytes("ERROR,TITLE,NAME NOT PROVIDED!",'utf-8'))
      return
    for name in webserver_names:
      if name==ans:
        scan+=1
        c.send(bytes("ERROR,TITLE,NAME ALREDY TAKEN!",'utf-8'))
        return
    if scan==0:
      webserver_names.append(str(ans))
      all_webservers.append(c)
      c.send(bytes("done",'utf-8'))
    print("Web Server: "+str(a[0])+" : "+str(a[1])+" is connected")
    return
  elif data3=='Client':
    all_clients.append(c)
    print("Clinet: "+str(a[0])+" : "+str(a[1])+" is connected")
  elif data3=="Graphic Client":
    all_clients.append(c)
    print("Graphic Client: "+str(a[0])+" : "+str(a[1])+" is connected")
  if data4=="yes":
    c.send(bytes('list num?','utf-8'))
    list_num=c.recv(2048)
    list_num=list_num.decode('utf-8')
    try:
      list_num=int(list_num)
      global username
      username=""
      num=0
      with open('./main server data/usernames.txt') as user:
        for line in user:
          lines=str(line).replace("\n","")
          if num==list_num:
            username+=str(lines)
            user_names.append(str(lines))
            break
          else:
            num+=1
      num=0
      with open('./main server data/passwords.txt') as acsess_key:
        for line in acsess_key:
          exit2=0
          while exit2!=1:
            lines2=str(line).replace("\n","")
            if num==list_num:
              while exit2!=1:
                check=c.recv(2048)
                check=check.decode('utf-8')
                if check==lines2:
                  c.send(bytes('correct','utf-8'))
                  exit2+=1
                elif check!=lines2:
                  c.send(bytes('wrong','utf-8'))
              break
            else:
              num+=1
      usernames[str(username)]=c
      c.send(bytes("Welcome to Muti-Chat Version 1.0! use $help to see commands $ is used for commands!",'utf-8'))
      time.sleep(5)
      c.send(bytes(str(lines),'utf-8'))
    except:
      if list_num=="mobile user":
        c.send(bytes("password",'utf-8'))
  elif data4=='no':
    c.send(bytes('setup time','utf-8'))
    time.sleep(1)
    c.send(bytes('please make a name (other people will see it so beaware)!','utf-8'))
    while True:
      check=c.recv(2048)
      check=check.decode('utf-8')
      with open('./main server data/usernames.txt') as file:
        for line in file:
          global look
          look=str(line)
          print(line)
          if line==check:
            c.send(bytes('already taken','utf-8'))
            break
      if look!=check:
        c.send(bytes('good','utf-8'))
        break
    c.send(bytes('now make a password so you can access your account from here','utf-8'))
    create=c.recv(3072)
    create=create.decode('utf-8')
    create=str(create[1:-1]).replace("'","").split(",")
    print(create)
    data1=open('./main server data/usernames.txt','a')
    data1.write(str(create[0]))
    data1.close()
    data2=open('./main server data/passwords.txt','a')
    data2.write(str(create[1]))
    data2.close()
    lines=0
    with open('./main server data/usernames.txt') as line_allocation:
      for line in line_allocation:
        if line=="":
          break
        else:
          lines+=1
    c.send(bytes(str(lines),'utf-8'))
    time.sleep(1)
    c.send(bytes("finished setting up your account and now it is save to restart as i can't do anything after this sorry","utf-8"))
    c.close()
def webserver_commands(c,a,command):
  if "init window("in command[0:12]:
    holder=str(command[12:-1]).split(",")
    pygame.init()
    global window
    window=pygame.display.set_mode(holder[0],holder[1])
  else:
    c.send(bytes("CODE ERROR: the command: "+str(command)+" does not exist",'utf-8'))
def chatroom_commands(c,a,command):
  if command=="delete chatroom":
    c.send(bytes("sorry at this point in time i can not delete any chatrooms...","utf-8"))
def commands(c,a,command):
  if command=="create chatroom":
    try:
      exit2=0
      while exit2!=1:
        c.send(bytes("SERVER:What name do you want to give your chatroom",'utf-8'))
        name=c.recv(2048)
        name=name.decode('utf-8')
        checker=str(name).replace(" ","")
        if checker=="":
          c.send(bytes("this is blank try again",'utf-8'))
          time.sleep(4)
        else:
          execdef=0
          while exit2!=1:
            if execdef==1:
              pass
            else:
              c.send(bytes("SERVER:do you want a password for it?(Y/N)",'utf-8'))
              yorn=c.recv(2048)
              yorn=yorn.decode('utf-8')
              checker=str(yorn).replace(" ","")
              if checker=="":
                c.send(bytes("nice try but it's Y or N only not blank",'utf-8'))
                time.sleep(6)
              elif yorn=="N"or yorn=="n":
                password=''
                client_chat_room[str(name)]=['no',str(password),str(a[0]),[c]]
                c.send(bytes("MRS*%: add 1 to chat admin",'utf-8'))
                c.send(bytes("MRS*%: Chatrooms name"+str(name),'utf-8'))
                time.sleep(2)
                c.send(bytes("chatroom is created now and you are the admin of it type C$ so do commands",'utf-8'))
                exit2+=1
              elif yorn=="Y"or yorn=="y":
                while exit2!=1:
                  c.send(bytes("What do you want to use as a password?",'utf-8'))
                  password=c.recv(2048)
                  password=password.decode('utf-8')
                  checker=str(password).replace(" ","")
                  if checker=="":
                    c.send(bytes("nice try but it can not be blank",'utf-8'))
                  else:
                    client_chat_room[str(name)]=['yes',str(password),str(a[0]),[c]]
                    c.send(bytes("MRS*%: add 1 to chat admin",'utf-8'))
                    c.send(bytes("MRS*%: Chatrooms name"+str(name),'utf-8'))
                    c.send(bytes("chatroom is created now and you are the admin of it type C$ so do commands",'utf-8'))
                    exit2+=1
              else:
                 c.send(bytes("nice try but it's Y or N only not: "+str(yorn),'utf-8'))
                 time.sleep(8)
    except:
      print("Connection: "+str(a[0])+" : "+str(a[1])+" disconnected")
  elif command=="help":
    c.send(bytes("""create chatroom-creates a chatroom
list chatrooms-lists chatrooms
help-lists commands
test send-sends a test message to show you that the server is receiveing your commands
access webserver-opes a webserver for you to explore with
list webservers-lists active webservers
scan-scans for chatrooms or webservers that is not in the server you are in (you will need to put 'chatroom ' to scan for chatrooms and 'webserver ' to scan for webservers in order to find the proper one or it might not work!)
clear screen-clears everything off your screen(works in the chatrooms too)""",'utf-8'))
  elif command=='test send':
    c.send(bytes("we are reciveing your commands!",'utf-8'))
  elif command=="clear screen":
    c.send(bytes("MRS*%: clear screen",'utf-8'))
  elif "scan "in command[0:5]:
    holder=command[5:]
    if "chatroom " in holder[0:9]:
      holder2=holder[9:]
      if holder2=="":
        c.send(bytes("haha nice try you got to put something in that line after 'chatroom ",'utf-8'))
      else:
        s2.send(bytes("Server: scan for chatroom: "+str(holder2),'utf-8'))
  elif "transfer "in command[0:9]:
    pass
  elif "join chatroom "in command[0:14]:
    holder=command[14:]
    found=0
    for chatroom in chatroom_names:
      if holder==chatroom:
        found+=1
        break
    if found==1:
      c.send(bytes("MSR*%: username","utf-8"))
      u_name=c.recv(1024)
      u_name=u_name.decode("utf-8")
      room_list=client_chat_room[str(holder)]
      user_list=room_list[3]
      for user in user_list:
        user.send(bytes("Server Message: "+str(u_name)+" joined your chatroom!"))
      c.send(bytes("MRS*%: add 1 to chatroom","utf-8"))
      c.send(bytes("MRS*%: Chatrooms name","utf-8"))
      
def handler(c,a):
  while exit3!=1:
    try:
      data=c.recv(2048)
      data=data.decode('utf-8')
    except:
      print("Connection: "+str(a[0])+" : "+str(a[1])+" disconnected")
      try:
        all_clients.remove(c)
      except:
        pass
      break
    if "C$"in data[0:2]:
      holder=data[2:]
      chatroom_commands(c,a,holder)
    elif "$"in data[0:1]:
      holder=data[1:]
      commands(c,a,holder)
    elif "W$"in data[0:2]:
      holder=data[2:]
      webserver_commands(c,a,holder)
    else:
      if "Chatroom: "in data[0:10]:
        holder=str(data[10:]).split("!@#$%^&*()_++_*")
        #finish the chat handler
def admin():
  while True:
    try:
      data=s2.recv(2048)
      data=data.decode('utf-8')
      print("a command was recived from the main server!")
    except:
      for connection in all_clients:
        c.send(bytes("main server down have a good day!",'utf-8'))
      time.sleep(10)
      exit3+=1
      break
    if data=="type?":
      s2.send(bytes("Server",'utf-8'))
    elif "got "in data[0:4]:
      holder=data[4:]
      if "chatroom: "in holder[0:10]:
        holder2=holder[10:]
        found=0
        for chatroom in chatroom_names:
          look=chatroom
          if look==holder2:
            s2.send(bytes("got it",'utf-8'))
            found+=1
            break
        if found==0:
          s2.send(bytes("no",'utf-8'))
      elif "webserver: "in holder[0:11]:
        holder2=holder[11:]
        found=0
        for webserver in webservers_names:
          look=webserver
          if look==holder2:
            s2.send(bytes("got it",'utf-8'))
            found+=1
            break
        if found==0:
          s2.send(bytes("no",'utf-8'))
    elif "list "in data[0:5]:
      holder=data[5:]
      if holder=="users":
        s2.send(bytes(str(user_names),"utf-8"))
    print("response was sent was sent!")
address=socket.gethostbyname(socket.getfqdn())
s2.connect((address,10500))
s1=Thread(target=admin)
s1.start()
while exit3!=1:
  try:
    c,a=s.accept()
    connection_checker()
    a1=Thread(target=handler,args=(c,a))
    a1.start()
  except:
    pass
