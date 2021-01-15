import socket
from struct import *
import sys

HEADER_LENGTH = 14

class EthernetHeader:

    def __init__(self, value=None):
        self.__value = value
        self.__unpacked = unpack('!6s6sH', value)

    def __get_hex_address(self, addr):
        if sys.version_info[0] == 2:
            return "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(addr[0]) , ord(addr[1]) , ord(addr[2]), ord(addr[3]), ord(addr[4]) , ord(addr[5]))
        
        return "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (addr[0] , addr[1] , addr[2], addr[3], addr[4] , addr[5])

    def __getitem__(self, key): 
        return self.__value[key]

    def __repr__(self):
        return self.__value
    
    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @property
    def unpacked(self):
        return self.__unpacked

    @property
    def protocol(self):
        return socket.ntohs(self.__unpacked[2])

    @property
    def destination_mac_address(self):
        return self.__get_hex_address(self.__value[0:6])

    @property
    def source_mac_address(self):
        return self.__get_hex_address(self.__value[6:12])

    @property
    def size(self):
        return len(self.__value)

class EthernetData:

    def __init__(self, value=None):
        self.__value = value

    def __getitem__(self, key):
        return self.__value[key] 

    def __repr__(self):
        return self.__value
    
    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @property
    def size(self):
        return len(self.__value)

class Ethernet:
    
    def __init__(self, frame=None):
        self.__value = frame
        self.__header = EthernetHeader(frame[:HEADER_LENGTH])
        self.__data = EthernetData(frame[HEADER_LENGTH:])

    def __repr__(self):
        return self.__value
    
    def __str__(self):
        return str(self.__value)
    
    @property
    def value(self):
        return self.__value

    @property
    def header(self):
        return self.__header

    @property
    def data(self):
        return self.__data

    @property
    def crc(self):
        return self.__crc