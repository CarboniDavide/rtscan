import socket
from struct import *

HEADER_BASE_LENGTH = 20

class TCPHeader:

    def __init__(self, value = None):
        self.__value = value
        self.__unpacked = unpack('!HHLLBBHHH', value)   

    def __getitem__(self, key): 
        return self.__value[key]

    def __repr__(self):
        return self.__value
    
    def __str__(self):
        return str(self.__value)

    @property
    def source_port(self):
        return self.__unpacked[0]

    @property
    def destination_port(self):
        return self.__unpacked[1]

    @property
    def sequence(self):
        return self.__unpacked[2] 

    @property
    def acknowledgement(self):
        return self.__unpacked[3]

    @property
    def doff_reserved(self):
        return self.__unpacked[4]

    @property
    def control_flags(self):
        return self.__unpacked[5]

    @property
    def window_size(self):
        return self.__unpacked[6]

    @property
    def check_sum(self):
        return self.__unpacked[7]

    @property
    def urgent_pointer(self):
        return self.__unpacked[8]

    @property
    def header_length(self):
        return self.doff_reserved >> 4

    @property
    def size(self):
        return (self.doff_reserved >> 4 ) * 4

    @property
    def unpacked(self):
        return self.__unpacked

class TCPData:

    def __init__(self, value = None):
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

class TCP:
    
    def __init__(self, packet = None):
        self.__value = packet
        self.__header = TCPHeader(packet[:HEADER_BASE_LENGTH])
        self.__data = TCPData(packet[self.__header.size:])

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
