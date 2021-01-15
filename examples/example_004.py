import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from core import *

def recv_pkts(packet):
    if packet is None:
        return
    eth_c = Ethernet(packet)
    if eth_c.header.protocol == InternetType.IPv4:
        ip_c = IP(eth_c.data.value)
        if ip_c.header.protocol == TransportType.TCP and str(ip_c.header.source_ip_address) == '192.168.1.1':
            tcp_c = TCP(ip_c.data.value)
            if str(tcp_c.header.destination_port) == '443':
                print('Source Port : ' + str(tcp_c.header.source_port) + ' Dest Port : ' + str(tcp_c.header.destination_port) + ' Sequence Number : ' + str(tcp_c.header.sequence) + ' Acknowledgement : ' + str(tcp_c.header.acknowledgement) + ' TCP header length : ' + str(tcp_c.header.header_length) + ' Header Size (Bytes) : ' + str(tcp_c.header.size) + ' Data Size (Bytes) : ' + str(tcp_c.data.size))

    

provider = create(ProviderType.Socket, 'eth0')
provider.loop(recv_pkts,0.01)