import os, pyshark, socket

#Parameters
TCP_IP = '192.168.1.32'
TCP_PORT = 5005
BUFFER_SIZE = 89

#Connection to the Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

HOST_IP = socket.gethostbyname(socket.gethostname())

def packet_captured(packet):
    ip_src = packet.ip.src
    print("ip_src : %s", ip_src)
    if(ip_src != None):
        try:
            port_src = packet.tcp.srcport
        except AttributeError as e:
            try:
                port_src = packet.udp.srcport
            except AttributeError as e:
                port_src = ""
    print("port_src : %s", port_src)
    #if((ip_src == HOST_IP or ip_src == TCP_IP) and port_src == str(TCP_PORT)):
    #    return

    mac_src = packet.eth.src
    if(mac_src is None):
        mac_src = " "
    print("mac_src : %s", mac_src)
    ip_dst = packet.ip.dst
    print("ip_dst : %s", ip_dst)
    if(ip_dst != None):
        try:
            port_dst = packet.tcp.dstport
        except AttributeError as e:
            try:
                port_dst = packet.udp.dstport
            except AttributeError as e:
                port_dst = ""
    print("port_dst : %s", port_dst)
    #if(ip_dst == TCP_IP and port_dst == str(TCP_PORT)):
    #    return

    mac_dst = packet.eth.dst
    if(mac_dst is None):
        mac_dst = " "
    print("mac_dst : %s", mac_dst)
    prtcl_hl = packet.highest_layer
    if(prtcl_hl is None):
        prtcl_hl = " "
    print("prtcl_hl : %s", prtcl_hl)
    prtcl_tl = packet.transport_layer
    if(prtcl_tl is None):
        prtcl_tl = " "
    print("prtcl_tl : %s", prtcl_tl)

    MESSAGE = ip_src + "," + mac_src + "," + port_src + "," + prtcl_hl + "," + prtcl_tl + "," + ip_dst + "," + mac_dst + "," + port_dst
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
