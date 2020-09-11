import socket                   # Import socket module
import os                       # Import os module to take screen shot

os.system("gnome-screenshot -f scr.png")
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
print(str(host))
port = 60000                    # Reserve a port for your service.

#s.connect((host, port))        # Use this in case you use it automatically 
s.connect(("put here the host adress", port))
filename='scr.png'
f = open(filename,'rb')
l= os.path.getsize("scr.png")
m = f.read(l)

while (m):
    s.sendall(m)
    print('Sent ',repr(m))
    m = f.read(l)
f.close()


s.close()
print('connection closed')
