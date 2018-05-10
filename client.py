import socket,time
from threading import Thread
from subprocess import call

server_down=0
webserver_owner=0
chat_admin=0
chatroom=0
chatroom_name=""
username=""
file_size=0
file_name=""
global file_transfer
file_transfer=0
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def sendMsg():
  while True:
    if file_transfer==0:
      send=input(str(username)+": ")
      try:
        if chat_admin==0 and chatroom==0:
          s.send(bytes(str(send),'utf-8'))
        elif chat_admin==1 and chatroom==1:
          s.send(bytes("Chatroom: "+str(chatroom_name)+"!@#$%^&*()_++_*Admin: yes!@#$%^&*()_++_*Message: "+str(send),'utf-8'))
        elif chatroom==1 and chat_admin==0:
          s.send(bytes("Chatroom: "+str(chatroom_name)+"!@#$%^&*()_++_*Admin: no!@#$%^&*()_++_*Message: "+str(send),"utf-8"))
      except:
        print("Server is offline!")
    elif file_transfer==1:
      pass
address=socket.gethostbyname(socket.getfqdn())
s.connect((address,10250))
setup=0
while setup!=2:
  lol=s.recv(1024)
  lol=lol.decode('utf-8')
  lol2=open('client data.txt','r')
  line1=lol2.readline()
  if lol=="type?":
    s.send(bytes("Client",'utf-8'))
    setup+=1
  elif lol=="setted up?":
    ans=str(line1).replace("\n","")
    if int(ans)==0:
      s.send(bytes('no','utf-8'))
    elif int(ans)==1:
      s.send(bytes('yes','utf-8'))
  elif lol=="list num?":
    line2=lol2.readline()
    s.send(bytes(str(line2),'utf-8'))
    checker=0
    while True:
      if checker==1:
        check=s.recv(1024)
        check=check.decode('utf-8')
        print("")
        if check=='correct':
          print("correct!")
          time.sleep(4)
          call('cls',shell=True)
          break
        elif check=='wrong':
          print("wrong, try again")
          time.sleep(4)
          call('cls',shell=True)
      password=input("password: ")
      s.send(bytes(str(password),'utf-8'))
      if checker==0:
        checker+=1
    startup=s.recv(1024)
    startup=startup.decode('utf-8')
    print(str(startup))
    lols=s.recv(1024)
    username+=str(lols.decode('utf-8'))
    setup+=1
  elif lol=="setup time":
    exit=0
    setups=0
    anger=0
    while exit!=1:
      recive=s.recv(2048)
      recive=recive.decode('utf-8')
      if setups==0:
        call('cls',shell=True)
        print(recive)
        global usernameing
        usernameing=input("username: ")
        if usernameing=="a name":
          if anger==0:
            print("haha nice try but you know what i ment")
            anger+=1
          elif anger==1:
            print("really again *sighs* stop it or else")
            anger+=1
          elif anger==2:
            print("ok than i will give you one if you will are going to do this!")
            done=0
            account_num=0
            usernameing="reckless person who will get on your nervers"
            while done!=1:
              combine=str(usernameing)+str(account_num)
              s.send(bytes(str(combine),'utf-8'))
              check=c.recv(1024)
              check=check.decode('utf-8')
              if check=="alredy taken":
                account_num+=1
              elif check=="good":
                print("there now the server accepted what i gave you now let's see how many people will not talk to you *laughs evilly*")
                done+=1
        else:
          checker=str(usernameing).replace(" ","")
          if checker=="":
            print("no blanks!")
          elif checker!="":
            s.send(bytes(str(usernameing),'utf-8'))
            check=s.recv(2048)
            check=check.decode('utf-8')
            if check=="alredy taken":
              print("that username is sadly already taken")
            elif check=="good":
              print("that username is available! and now you have taken it!")
              time.sleep(6)
              setups+=1
      elif setups==1:
        call('cls',shell=True)
        print(recive)
        global password_set
        password_set=input("password: ")
        if password_set==username:
          print("you can not have your username as your password sorry")
          time.sleep(6)
        checker=str(password_set).replace(" ","")
        if checker=="":
          print("no blanks!")
          time.sleep(4)
        else:
          exit+=1
          setups+=1
    final_process=[]
    final_process.append(str(usernameing))
    final_process.append(str(password_set))
    s.send(bytes(str(final_process),'utf-8'))
    line_allocation=s.recv(1024)
    line_allocation=line_allocation.decode('utf-8')
    data=open('./client data.txt','w')
    data.write('1\n')
    data.write(str(line_allocation))
    data.close()
    final_message=s.recv(2048)
    final_message=final_message.decode('utf-8')
    print(final_message)
    time.sleep(100000)
    print("you know you left this running for 1.1574074 days right")
    time.sleep(4)
    print("fine i'll let you in without that restart but you will left in a broken state to the servers to the point they miight not know what to do with your client half")
    time.sleep(14)
    setup+=1
while True:
  a1=Thread(target=sendMsg)
  a1.deamon=True
  a1.start()
  try:
    data=s.recv(1024)
    data=data.decode('utf-8')
  except:
    print("Server offline restart to reconnect!")
    server_down+=1
    break
  if "MRS*%: " in data[0:7]:
    holder=data[7:]
    if holder=="shutdown":
      print("i was told by the admins to shutdown sorry")
      time.sleep(6)
      exit()
    elif holder=="add 1 to chat admin":
      chat_admin+=1
      chatroom+=1
    elif holder=="add 1 to chatroom":
      chatrrom+=1
    elif holder=="sub 1 from chat admin":
      chat_admin-=1
      chatroom-=1
    elif holder=="sub 1 from chatroom":
      chatroom-=1
    elif "Chatrooms name"in holder[0:14]:
      name=holder[14:]
      chatroom_name+=str(name)
    elif holder=="clear chatroom name":
      chatroom_name=""
    elif holder=="clear screen":
      call('cls',shell=True)
    elif holder=="switch to file transfer mode":
      file_transfer+=1
      data_size=s.recv(1024)
      data_size=data_size.decode('utf-8')
      file_size+=int(data_size)
      file_names=s.recv(1024)
      file_name=file_names.decode("urf-8")
    elif holder=="chatroom?":
      if chatroom==1:
        s.send(bytes("yes","utf-8"))
        time.sleep(5)
        s.send(bytes(str(chatroom_name),"utf-8"))
      else:
        s.send(bytes("no","utf-8"))
    elif holder=="username":
      s.send(bytes(str(username),"utf-8"))
  elif file_transfer==1:
    print("the file size is "+str(file_size)+" Bytes so do you want to download it (y/n)")
    while True:
      ans=input("Y or N: ")
      if ans=="Y"or ans=="y":
				file=open(str(file_name),"a")
        while True:
          if "SERVER: FILE: "in data[0:14]:
            data2=data[14:]
            if data2=="done":
							file.close()
              break
            else:
							file.write(str(data2))
         else:
          pass
       break
      elif ans=="N"or ans=="n":
      	break
  else:
    print(str(data))
