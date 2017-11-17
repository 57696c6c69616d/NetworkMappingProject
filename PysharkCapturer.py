import pyshark

def packet_captured(packet):
    p = packet.ip.src
    if(p != None):
        print 'IP Source :', p
    p = packet.ip.dst
    if(p != None):
        print 'IP Dest. :', p
    p = packet.highest_layer
    if(p != None):
        transport_protocol = ''
        q = packet.transport_layer
        if q != p and q is not None:
            transport_protocol = q + '/'
        protocol = transport_protocol + p
        print 'Protocol :', protocol
        print('\n')

while(True):
    capture = pyshark.LiveCapture(interface='Wi-Fi')
    try:
        capture.apply_on_packets(packet_captured)
    except AttributeError as e:
        pass
