import socket, mysql.connector
import sys
from thread import *

#Parameters
#Attention aux interfaces liees aux vms
TCP_IP = '192.168.1.32' #socket.gethostbyname(socket.gethostname())
TCP_PORT = 5005
BUFFER_SIZE = 89

#Connection to the Database
sql_conn = mysql.connector.connect(host="localhost",user="nmp_user",password="nmp_pa55", database="nmpdb")
cursor = sql_conn.cursor()

#Connection with the Client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

#Function for handling connections. This will be used to create threads
def clientthread(conn):
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(BUFFER_SIZE)
        print("Data received: %s", data)

        if not data: break
        
        #Sending Data to the Database
        data = data.split(',')
        ip_src = data[0]
        query = ("INSERT IGNORE INTO nmpdb.t_address (ip) VALUES ('" + ip_src + "');")
        cursor.execute(query)
        sql_conn.commit()

        ip_dst = data[5]
        query = ("INSERT IGNORE INTO nmpdb.t_address (ip) VALUES ('" + ip_dst + "');")
        cursor.execute(query)
        sql_conn.commit()

        d = (ip_src, data[1], data[2], data[3], data[4], ip_dst, data[6], data[7])
        query = ("INSERT INTO nmpdb.t_packets (source, mac_src, port_src, prtcl_hl, prtcl_tl, target, mac_dst, port_dst) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")
        cursor.execute(query, d)
        sql_conn.commit()

    #came out of loop
    conn.close()

while 1:
	conn, addr = s.accept()
	print 'Connection address:', addr
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))

conn.close()

sql_conn.close()
