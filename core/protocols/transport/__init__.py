from .tcp import TCP
from .udp import UDP
from .icmp import ICMP

class TransportType():
    HOPOPT = 0
    ICMP = 1
    IGMP = 2
    GGP = 3
    IP_IN_IP = 4
    ST = 5
    TCP = 6
    CBT = 7
    EGP = 8
    IGP = 9
    BBN_RCC_MOM = 10
    NVP_II = 11
    PUP = 12
    ARGUS = 13
    EMCON = 14
    XNET = 15
    CHAOS = 16
    UDP = 17