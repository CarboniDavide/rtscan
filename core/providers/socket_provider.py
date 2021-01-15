import socket, sys
from core.exceptions.exception import *
from .provider import Provider
from mod.mlog import log

class SocketProviderError(RtException):
    def __init__(self, message=None, loggable=True):
        super(SocketProviderError, self).__init__(message, loggable)

class SocketProvider(Provider):
    
    _name = "Socket Provider"
    
    def __init__(self, device=None):
        super(SocketProvider, self).__init__(device)
    
    def get_next_frame(self):
        # get data from socket:
        # recfrom return two values: (data, device informations)
        try:
            res = self._object.recvfrom(self._max_bytes)
        except:
            return None
        
        #device is an array with (device, size, other, other, ip)
        #return frame only from selected device
        return res[0] if res[1][0] == self._device else None

    def set_device(self, device=None):
        try:
            self._object = socket.socket(socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
        except socket.error:
            raise SocketProviderError("Socket provider could not be created.")

        self._device = device

    def loop(self, callback=None, timeout=None):
        super(SocketProvider, self).loop(callback, timeout)