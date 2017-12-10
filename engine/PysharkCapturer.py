import os, pyshark, mysql.connector

conn = mysql.connector.connect(host="localhost",user="nmp_user",password="nmp_pa55", database="nmpdb")
cursor = conn.cursor()

def packet_captured(packet):
    ip_src = packet.ip.src
    if(ip_src != None):
        port_src = packet.tcp.srcport
    
    ip_dst = packet.ip.dst
    if(ip_dst != None):
        port_dst = packet.tcp.dstport
    
    prtcl_hl = packet.highest_layer
    if(prtcl_hl != None):
        prtcl_tl = packet.transport_layer
    
    if(ip_src is not None and ip_dst is not None):
        if(prtcl_hl is None):
            prtcl_hl = ""
        if(prtcl_tl is None):
            prtcl_tl = ""

        data = (ip_src)
        print data
        query = ("INSERT IGNORE INTO nmpdb.t_address (ip) VALUES ('" + data + "');")
        print query
        cursor.execute(query)
        conn.commit()
        print("ip source sent !\n")

        data = (ip_dst)
        query = ("INSERT IGNORE INTO nmpdb.t_address (ip) VALUES ('" + data + "');")
        cursor.execute(query)
        conn.commit()
        print("ip destination sent !\n")

        data = (ip_src, port_src, prtcl_hl, prtcl_tl, ip_dst, port_dst)
        query = ("INSERT INTO nmpdb.t_packets (source, port_src, prtcl_hl, prtcl_tl, target, port_dst) VALUES (%s, %s, %s, %s, %s, %s);")
        cursor.execute(query, data)
        conn.commit()
        print("All sent !\n")

#while(True):
capture = pyshark.LiveCapture(interface='Wi-Fi')
capture.sniff(timeout=10)
try:
    capture.apply_on_packets(packet_captured)
except AttributeError as e:
    pass

conn.close()