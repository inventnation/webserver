import socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=socket.gethostbyname(socket.getfqdn())
s.connect((address,10250))
lol=s.recv(1024)
lol=lol.decode('utf-8')
if lol=="type?":
  s.send(bytes("Web Server",'utf-8'))
else:
  print("did not get the 'type?' command the server shuting down...")
  time.sleep(6)
  exit()
tokens=[]
num_stack=[]
#not important-the line below this one holds the title because of the command make_public needs it
title_name=[]

def choice():
  while True:
    choices=input("Y or N: ")
    if choices=="Y"or choices=="y":
      return "yes"
      break
    elif choices=="N"or choices=="n":
      return "no"
      break

def sendCommands(command):
  error=s.recv(1024)
  error=error.decode('utf-8')
  error=str(error).split(",")
  s.send(bytes("W$"+str(command),"utf-8"))
  error=s.recv(1024)
  error=error.decode('utf-8')
  error=str(error).split(",")
  if "ERROR"in error[0]:
    error2=error[1]
    error3=error[2]
    if "SYS"in error2:
      print("SYSTEM ERROR: "+str(error3))
      time.sleep(1000)
    elif "TITLE"in error2:
      print("TITLE ERROR: "+str(error3))
      time.sleep(1000)
    elif "I/O"in error2:
      print("I/O ERROR: "+str(error3))
      time.sleep(1000)
    else:
      print("GENRAL ERROR: YOU FOUND A GREY LINE THAT THE ERRORS DON'T KNOW WHERE IT GOES TO SO THIS ERROR WAS TRIGGERED TO RESOLVE IT")
  elif error[0]=="done":
    pass
def handler(c,a):
  pass

def open_main_file(filename):
  data=open(filename,'r').read()
  data+="<EOF>"
  return data

def lex(filecontents):
  tok=""
  string=""
  expr=""
  n=""
  state=0
  title_activated=0
  isexpr=0
  title_sent=0
  filecontents=list(filecontents)
  for char in filecontents:
    tok+=str(char)
    if tok==" ":
      if state==0:
        tok=""
      else:
        tok=" "
    elif tok=="\n"or tok=="<EOF>":
      #set webserver command on the minor server to allow an exit command
      #if tok=="<EOF>":
        #sendCommands("exit")
      if expr!=""and isexpr==1:
        tokens.append("expr: "+expr)
        expr=""
      elif expr!="" and isexpr==0:
        tokens.append("num: "+expr)
        expr=""
      tok=""
    elif tok=="display " or tok=="print "or tok=="Display "or tok=="Print ":
      tokens.append("print")
      tok=""
    elif tok=="0"or tok=="1"or tok=="2"or tok=="3"or tok=="4"or tok=="5"or tok=="6"or tok=="7"or tok=="8"or tok=="9":
      expr+=str(tok)
      tok=""
    elif tok=="+"or tok=="-"or tok=="*"or tok=="/":
      isexpr=1
      expr+=str(tok)
      tok=""
    elif tok=="title "or tok=="Title ":
      if title_sent==1:
        print("TITLE ERROR: TITLE ALREDY SENT")
        time.sleep(1000)
      else:
        tokens.append("title")
        title_sent+=1
        title_activated+=1
        tok=""
    elif tok=="public" or tok=="Public":
      #also allow the server to handle command called public
      pass
    elif tok== "\"":
      if state==0:
        state=1
      elif state==1:
        tokens.append("string: "+string+"\"")
        string=""
        tok=""
        title_activated=0
        state=0
    elif state==1:
      string+=tok
      tok=""
  #print(tokens)
  return tokens

def parse(toks):
  i=0
  while i< len(toks):
    if toks[i]+" "+toks[i+1][0:6]=="print string":
      print(toks[i+1][8:])
      i+=2
    elif toks[i]+" "+toks[i+1][0:6]=="title string":
      sending=str(toks[i+1][8:]).replace("\"","")
      title_name.append(str(sending))
      sendCommands(sending)
      i+=2
while True:
  line_num=0
  print("do you have a file with a .web to use in here to run? EX:test.web(y/n)")
  ans=choice()
  if ans=="yes":
    print("type path to the file and the file name EX:./test/test")
    file_name=input(":> ")+".web"
    #try:
    if 1==1:
      contents=open_main_file(file_name)
      toks=lex(contents)
      parse(toks)
    #except:
      #print("that was nat able to be opened sorry")
  elif ans=="no":
    print("than have a good day")
    time.sleep(4)
    exit()
