import socket                   # Import socket module
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()     # Get local machine name

port = 57272

s.connect((host, port))
number = str(s.recv(1024),"utf-8")
print(number)
filename = input("Enter the corresponding file number of the file to access:")
s.send(str.encode(filename))
f=open("Output.txt","w")
print("The data inside the file:\n")
while f:

        data = s.recv(50000) 
        if data:
          file_name = data.decode()
        else:
         break
f.write(data.decode())
f.close()
a=[]
a.append(file_name)
f = open("Krishna.txt","w")
for i in a:
  f.write(i)
print(file_name)
f.close()
print('Successfully got the file')
s.close()
print('connection closed')
