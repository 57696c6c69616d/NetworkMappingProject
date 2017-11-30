import os, pyshark

def packet_captured(packet):
    s = ''
    
    ip_src = packet.ip.src
    if(ip_src != None):
        print 'IP Source :', ip_src
        port_src = packet.tcp.srcport
        print 'Port Source :', port_src
        s += ip_src + ',' + port_src + ','
    
    ip_dst = packet.ip.dst
    if(ip_dst != None):
        print 'IP Dest. :', ip_dst
        port_dst = packet.tcp.dstport
        print 'Port Dest. :', port_dst
        s += ip_dst + ',' + port_dst + ','
    
    prtcl_hl = packet.highest_layer
    if(prtcl_hl != None):
        transport_protocol = ''
        prtcl_tl = packet.transport_layer
        if prtcl_tl != prtcl_hl and prtcl_tl is not None:
            transport_protocol = prtcl_tl + '/'
        protocol = transport_protocol + prtcl_hl
        print 'Protocol :', protocol
        s += protocol
    
    if(ip_src is not None and ip_dst is not None and prtcl_hl is not None):
        os.system('Client.py ' + s)
        print("Packet sent:" + s)

while(True):
    capture = pyshark.LiveCapture(interface='Wi-Fi')
    try:
        capture.apply_on_packets(packet_captured)
    except AttributeError as e:
        pass
#https://docs.djangoproject.com/fr/1.11/intro/tutorial05/
