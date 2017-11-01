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

#Imports
import sys, os
sys.path.append(os.getcwd() + '\\Documents\\GitHub\\NetworkMappingProject')

import packet

#Wireshark plain text file opening (working folder)
capture = open('CaptureWireshark.txt','r')

#Creation of the global variables
Packet_List = []
P = packet.packet()
protocol_line = False

#Packet List Completion
with capture:
    for line in capture:
        tmp = line.split(',')
        if(protocol_line):
            prtcl = tmp[0][:len(tmp[0])]
            protocol_line = False
            P = packet.packet(prtcl, src, dst)
            Packet_List.append(P)
        elif("Internet Protocol Version 4" in tmp[0]):
            src = tmp[1][6:len(tmp[1])]
            dst = tmp[2][6:len(tmp[2])]
            protocol_line = True

for i in range(len(Packet_List)):
    Packet_List[i].Display()

#Close the Capture File
capture.close()
