import socket, mysql.connector, time, datetime, config
import sys
from thread import *
from Crypto.Cipher import AES

#Parameters
TCP_IP = config.ip
TCP_PORT = config.port
BUFFER_SIZE = 96

#Cipher
key = config.key
iv = config.iv
obj = AES.new(key, AES.MODE_CBC, iv)

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
        encrypted_data = conn.recv(BUFFER_SIZE)
        data = obj.decrypt(encrypted_data)
        print("Data received: %s", data)
        MESSAGE = data
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        logtext = "[" + st + "] " + MESSAGE + "\n"
        log.write(logtext)

        if not data: break
        
        #Sending Data to the Database
        data = data.split(',')

        d = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        query = ("INSERT INTO nmpdb.t_packets (source, mac_src, port_src, prtcl_hl, prtcl_tl, target, mac_dst, port_dst, length) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
        cursor.execute(query, d)
        sql_conn.commit()

    #came out of loop
    conn.close()

with open("log.txt", "a") as log:
    while 1:
    	conn, addr = s.accept()
    	print 'Connection address:', addr
        MESSAGE = 'Connection of ' + str(addr)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        logtext = "[" + st + "] " + MESSAGE + "\n"
        log.write(logtext)
    	
    	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    	start_new_thread(clientthread ,(conn,))

conn.close()

sql_conn.close()
