import socket                   

port = 57272           
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)             
host = socket.gethostname()     
    
s.bind((host, port))            
s.listen(5)                     

print('Server listening....')

while True:
    conn, addr = s.accept()     
    print ('Got connection from', addr)
    dat = "You can access three files of server\n 1.text.txt \n 2.mytext.txt \n 3.file.txt.\n Select respective filenumbers 1 or 2 or 3."
    conn.send(str.encode(dat))
    filenumber = str(conn.recv(1024),"utf-8")
    if(filenumber == '1'):
      filename = "Output.txt"
      print("Requested file from client:"+filename)
      f = open(filename,'rb')
      l = f.read(1024)
    elif(filenumber == '2'):
      filename = "mytext.txt"
      print("Requested file from client:"+filename)
      f = open(filename,'rb')
      l = f.read(1024)
    else:
      filename = "myfile.txt"
      print("Requested file from client:"+filename)
      f = open(filename,'rb')
      l = f.read(1024)
    while (l):
       conn.send(l) 
       l = f.read(1024)
    f.close()
    print('Done copying the file and sent')
    conn.close()
