import os, pyshark, socket

#Parameters
TCP_IP = '192.168.1.32'
TCP_PORT = 5005
BUFFER_SIZE = 55

#Connection to the Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

HOST_IP = socket.gethostbyname(socket.gethostname())

def packet_captured(packet):
    ip_src = packet.ip.src
    if(ip_src != None):
        port_src = packet.tcp.srcport
        if((ip_src == HOST_IP or ip_src == TCP_IP) and port_src == str(TCP_PORT)):
            return
    
    ip_dst = packet.ip.dst
    if(ip_dst != None):
        port_dst = packet.tcp.dstport
        if(ip_dst == TCP_IP and port_dst == str(TCP_PORT)):
	    return
    
    prtcl_hl = packet.highest_layer
    if(prtcl_hl != None):
        prtcl_tl = packet.transport_layer
    
    if(ip_src is not None and ip_dst is not None):
        if(prtcl_hl is None):
            prtcl_hl = ""
        if(prtcl_tl is None):
            prtcl_tl = ""

    MESSAGE = ip_src + "," + port_src + "," + prtcl_hl + "," + prtcl_tl + "," + ip_dst + "," + port_dst
    lenght = len(MESSAGE)
    if(lenght < BUFFER_SIZE):
        fill = ","
        for i in range(BUFFER_SIZE-lenght-1):
            fill += "x"
        MESSAGE += fill

    s.send(MESSAGE)
    print("Message sent: %s", MESSAGE)

capture = pyshark.LiveCapture(interface='Wi-Fi')
for packet in capture.sniff_continuously():
    try:
        capture.apply_on_packets(packet_captured)
    except AttributeError as e:
        pass

s.close()
