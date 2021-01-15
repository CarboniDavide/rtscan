from core.providers.provider import Provider
from core.exceptions.exception import *
from mod.mlog import log
import socket, sys

try:
    import pcapy
except ImportError:
    pcapy = None
    log.warning("Pcapy module is not installed in this machine.")

class PcapyProviderError(RtException):
    def __init__(self, message=None, loggable=True):
        super(PcapyProviderError, self).__init__(message, loggable)

class PcapyProvider(Provider):
    
    _name = "Pcapy Provider"
    
    def __init__(self, device=None):
        if not pcapy:
            raise PcapyProviderError("Unable to istantiate Pcapy provider. Pcapy module not found in this machine.")
        super(PcapyProvider, self).__init__(device)

    def get_next_frame(self):
        try:
            return self._object.next()[1]
        except:
            return None
        
    def get_all_devices(self):
        return pcapy.findalldevs()

    def set_device(self, device=None):
        cap = pcapy.open_live(device, self._max_bytes, True, 0)
        self._object = cap
        self._device = device
        
    def loop(self, callback=None, timeout=None):
        super(PcapyProvider, self).loop(callback, timeout)