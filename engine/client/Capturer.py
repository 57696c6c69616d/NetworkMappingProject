import os, pyshark, socket, config

#Parameters
TCP_IP = config.ip
INTERFACE = config.interface
TCP_PORT = config.port
BUFFER_SIZE = 94

#Connection to the Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

HOST_IP = socket.gethostbyname(socket.gethostname())

def packet_captured(packet):
    ip_src = packet.ip.src
    if(ip_src != None):
        try:
            port_src = packet.tcp.srcport
        except AttributeError as e:
            try:
                port_src = packet.udp.srcport
            except AttributeError as e:
                port_src = " "
    
    #if((ip_src == HOST_IP or ip_src == TCP_IP) and port_src == str(TCP_PORT)):
    #    return

    mac_src = packet.eth.src
    if(mac_src is None):
        mac_src = " "
    
    ip_dst = packet.ip.dst
    if(ip_dst != None):
        try:
            port_dst = packet.tcp.dstport
        except AttributeError as e:
            try:
                port_dst = packet.udp.dstport
            except AttributeError as e:
                port_dst = " "
    
    #if(ip_dst == TCP_IP and port_dst == str(TCP_PORT)):
    #    return

    mac_dst = packet.eth.dst
    if(mac_dst is None):
        mac_dst = " "
    
    prtcl_hl = packet.highest_layer
    if(prtcl_hl is None):
        prtcl_hl = " "
    
    prtcl_tl = packet.transport_layer
    if(prtcl_tl is None):
        prtcl_tl = " "
    
    caplen = packet.length
    if(caplen is None):
        caplen = 0
    
    MESSAGE = ip_src + "," + mac_src + "," + port_src + "," + prtcl_hl + "," + prtcl_tl + "," + ip_dst + "," + mac_dst + "," + port_dst + "," + caplen
    length = len(MESSAGE)
    if(length < BUFFER_SIZE):
        fill = ","
        for i in range(BUFFER_SIZE-length-1):
            fill += "x"
        MESSAGE += fill

    s.send(MESSAGE)
    print("Message sent: %s", MESSAGE)

capture = pyshark.LiveCapture(interface=INTERFACE)
for packet in capture.sniff_continuously():
    try:
        capture.apply_on_packets(packet_captured)
    except AttributeError as e:
        pass

s.close()
