################################################################################
#                                                                              #
#                                                                              #
#                                                                              #
#                         NetworkMappingProject                                #
#                                                                              #
#                                                                              #
#       A. Decoster / K. Leou / Y. Lonlas / L. Rateau / W. Winterhalter        #
#                                                                              #
################################################################################

################################################################################
#           #          #                        #                              #
# Iteration # Date     # Name                   # Change(s) Nature             #
#           #          #                        #                              #
################################################################################
#         1 # 01/11/17 # W.Winterhalter         # Creation of the file         #
################################################################################
#         2 # 05/11/17 # W.Winterhalter         # Add draw_graph()             #
#           #          #                        #  - nodes = Ip sources & dest.#
#           #          #                        #  - labels = Protocol         #
################################################################################

#Imports
import sys, os
sys.path.append(os.getcwd() + '\\Documents\\GitHub\\NetworkMappingProject')

import packet, Networkx as nx

#Wireshark plain text file opening (working folder)
capture = open('CaptureWireshark.txt','r')

#Dictionnay containing the abreviations of the protocols
PROTOCOLS = {'Transmission Control Protocol': 'TCP', 'Internet Group Management Protocol': 'IGMPv2',
             'Secure Sockets Layer': 'SSL', 'User Datagram Protocol': 'UDP', 'Simple Service Discovery Protocol': 'SSDP',
             'Address Resolution Protocol': 'ARP'}

#Creation of the global variables
Packet_List = []
P = packet.packet()
protocol_line = False
protocol_line_2 = False

#Packet List Completion
with capture:
    for line in capture:
        tmp = line.split(',')
        if(protocol_line_2):
            prtcl = tmp[0][:len(tmp[0])]
            if("\n" in prtcl):
                prtcl = prtcl[:len(prtcl)-1]
            if(prtcl != None and prtcl in PROTOCOLS):
                P.setProtocol(P.getProtocol() + '(' + PROTOCOLS.get(prtcl) + ')')
                Packet_List[len(Packet_List)-1] = P
            protocol_line_2 = False
        elif(protocol_line):
            prtcl = tmp[0][:len(tmp[0])]
            if("\n" in prtcl):
                prtcl = prtcl[:len(prtcl)-1]
            protocol_line = False
            protocol_line_2 = True
            P = packet.packet(PROTOCOLS.get(prtcl), src, dst)
            Packet_List.append(P)
        elif("Internet Protocol Version 4" in tmp[0]):
            src = tmp[1][6:len(tmp[1])]
            dst = tmp[2][6:len(tmp[2])-1]
            protocol_line = True

graph = []
labels = []

for i in range(len(Packet_List)):
    cp = Packet_List[i]
    #cp.Display()
    if((cp.getIpSrc(), cp.getIpDst()) not in graph):
        graph.append((cp.getIpSrc(), cp.getIpDst()))
        labels.append(cp.getProtocol())

nx.draw_graph(graph, labels, 'shell', 1600, 'red')

#Close the Capture File
capture.close()
