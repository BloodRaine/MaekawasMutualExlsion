import socket

HOST = socket.gethostname()  # The server's hostname or IP address
PORT = 65432                 # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

message = input('-> ')

while message.lower().strip() != "q":
    
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024).decode()
    print('Received from server: ' + data)
    message = input('-> ')

s.close()
