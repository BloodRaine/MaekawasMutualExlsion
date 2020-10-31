import socket
import struct
import vectorclock

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
multicast_group = '224.3.29.71'
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
server_address = ('', PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

vClock = vectorclock.VectorClock
clients = []

print("Server Started")

while True:
    print("waiting")
    data, addr = s.recvfrom(1024)
    if addr not in clients:
        print("recieved new address")
        newEntry = vectorclock.VectorClock
        newEntry.generate(newEntry, 1)
        vClock.merge(vClock, vClock.clock, newEntry.clock)
        
        clients.append(addr)
    s.sendto(data, addr)
    print("sent response")
