from .socket_provider import SocketProvider
from .pcapy_provider import PcapyProvider
from .provider import Provider
from core.exceptions import *

class ProviderType():
    Socket = "SocketProvider"
    Pcapy = "PcapyProvider"

def create(providerType, device=None):
        return globals()[providerType](device)