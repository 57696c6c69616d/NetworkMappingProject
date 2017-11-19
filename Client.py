import sys, socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 55
MESSAGE = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data

#for i in range(len(platform.uname())):
#	print(platform.uname()[i])

#socket.gethostbyaddr('192.168.1.22')
