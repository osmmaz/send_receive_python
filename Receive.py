import socket                   # Import socket module
from time import gmtime, strftime
def recive():
   with open('rec'+str(strftime("%Y-%m-%d_%H:%M:%S", gmtime()))+'.png', 'wb') as f: # Creating a meaningful file 

       print("file opened")
       while True:
          conn, addr = s.accept()     # Establish connection with client.
          print ('Got connection from', addr)
          print('receiving data...')
          d = conn.recv(1024)
          data=d
          while d:
             d = conn.recv(1024)
             data=data+d
          
          print('data=%s', (data))
          if not data:
              break
          # write data to a file
          f.write(data)
          f.close()
          print('Successfully get the file')
          conn.send(b'Thank you for connecting')
          conn.close()
          print("good bye")
          break



port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
#s.bind((host, port))           # Bind to the port (if you are using this line delete the next line)
s.bind(("put here the adress", port))            
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')
while True:
   recive()			# Always listening and receiving data
