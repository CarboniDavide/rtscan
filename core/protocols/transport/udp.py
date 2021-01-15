import socket
from struct import *

HEADER_LENGTH = 8

class UDPHeader:

    def __init__(self, value = None):
        self.__value = value
        self.__unpacked = unpack('!HHHH', value)   

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
    def length(self):
        return self.__unpacked[2]

    @property
    def checksum(self):
        return self.__unpacked[3]

    @property
    def size(self):
        return len(self.__value)

    @property
    def unpacked(self):
        return self.__unpacked

class UDPData:

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

class UDP:
    
    def __init__(self, packet = None):
        self.__value = packet
        self.__header = UDPHeader(packet[:HEADER_LENGTH])
        self.__data = UDPData(packet[self.__header.size:])

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
