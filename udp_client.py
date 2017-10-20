'''
taken from Black Hat Python
If you want to compute RTT,
get the CPU time with time.clock()
'''


import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("hello", (target_host, target_port))

data, addr = client.recvfrom(4096)

print (data)
