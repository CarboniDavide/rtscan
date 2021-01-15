from abc import ABCMeta, abstractmethod
from core.exceptions.exception import *
import threading
import os
import time

class ProviderError(RtException):
    def __init__(self, message=None, loggable=True):
        super(ProviderError, self).__init__(message, loggable)

class Provider:

    __metaclass__ = ABCMeta
    _name = None
    _max_bytes = 1518

    def __init__(self, device=None):
        self._device = device
        self._object = None
        if device is None:
            return
        self.set_device(device)

    @property
    def name(self):
        return self._name
    
    @property
    def device(self):
        return self._device

    @property
    def obj(self):
        return self._object
    
    @property
    def max_bytes(self):
        return self._max_bytes
    

    @abstractmethod
    def get_next_frame(self):
        pass

    @staticmethod
    def get_all_devices():
        return os.listdir('/sys/class/net/')

    @abstractmethod
    def set_device(self, device=None):
        pass
    
    @abstractmethod
    def loop(self, callback=None, timeout=None):
        
        # dont use time.sleep if None or zero to improve performance
        if timeout is None or timeout == 0:
            while True:
                callback(self.get_next_frame())
            return
        
        while True:
                callback(self.get_next_frame())
                time.sleep(timeout)