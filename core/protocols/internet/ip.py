import socket
from struct import *

HEADER_LENGTH = 20

class IPHeader:

    def __init__(self, value = None):
        self.__value = value
        self.__unpacked = unpack('!BBHHHBBH4s4s', value)   

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
    def version(self):
        return self.__unpacked[0] >> 4

    @property
    def ihl(self):
        return self.__unpacked[0] & 0b00001111

    @property
    def type_of_service(self):
        return self.__unpacked[1]

    @property
    def total_lenght(self):
        return self.__unpacked[2]

    @property
    def identification(self):
        return self.__unpacked[3]

    @property
    def flags(self):
        return self.__unpacked[4] >> 13

    @property
    def fragment_offset(self):
        return self.__unpacked[4] & 0b0001111111111111

    @property
    def time_to_live(self):
        return self.__unpacked[5]

    @property
    def protocol(self):
        return self.__unpacked[6]

    @property
    def header_checksum(self):
        return self.__unpacked[7]

    @property
    def source_ip_address(self):
        return socket.inet_ntoa(self.__unpacked[8])

    @property
    def destination_ip_address(self):
        return socket.inet_ntoa(self.__unpacked[9])

    @property
    def unpacked(self):
        return self.__unpacked

    @property
    def size(self):
        return self.ihl * 4

class IPData:

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

class IP:
    
    def __init__(self, packet = None):
        self.__value = packet
        self.__header = IPHeader(packet[:HEADER_LENGTH])
        self.__data = IPData(packet[self.__header.size:])

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
