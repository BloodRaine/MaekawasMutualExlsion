import socket
import struct

HOST = socket.gethostname()  # The server's hostname or IP address
PORT = 65432                 # The port used by the server
multicast_group = ('224.3.29.71', PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(0.2)
# s.connect(('',PORT))

ttl = struct.pack('b', 1)
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

message = input('-> ')

while message.lower().strip() != "q":
    s.sendto(message.encode('utf-8'), multicast_group)

    while True:
        try:
            data, address = s.recvfrom(1024)
        except socket.timeout:
            print("Timeout")
            break
        else:
            print('Received from server: ' + str(data))


        message = input('-> ')
print("closing socket")
s.close()
