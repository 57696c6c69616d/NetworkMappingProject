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

class packet:
    
    def __init__(self, protocol="", ip_src="0.0.0.0", ip_dst="0.0.0.0"):
        self.__protocol = protocol
        self.__ip_src = ip_src
        self.__ip_dst = ip_dst
        
    def getProtocol(self):
        return self.__protocol
        
    def getIpSrc(self):
        return self.__ip_src
        
    def getIpDst(self):
        return self.__ip_dst
        
    def Display(self):
        print('Protocol: ' + self.__protocol)
        print('IP Source: ' + self.__ip_src)
        print('IP Destination: ' + self.__ip_dst)
