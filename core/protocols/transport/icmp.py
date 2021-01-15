import socket
from struct import *

HEADER_LENGTH = 4

class ICMPHeader:

    def __init__(self, value = None):
        self.__value = value
        self.__unpacked = unpack('!BBH', value)   

    def __getitem__(self, key): 
        return self.__value[key]

    def __repr__(self):
        return self.__value
    
    def __str__(self):
        return str(self.__value)

    @property
    def type(self):
        return self.__unpacked[0]

    @property
    def code(self):
        return self.__unpacked[1]

    @property
    def checksum(self):
        return self.__unpacked[2]

    @property
    def size(self):
        return len(self.__value)

    @property
    def unpacked(self):
        return self.__unpacked

class ICMPData:

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

class ICMP:
    
    def __init__(self, packet = None):
        self.__value = packet
        self.__header = ICMPHeader(packet[:HEADER_LENGTH])
        self.__data = ICMPData(packet[self.__header.size:])

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
