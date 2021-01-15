import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from core import *

def read(packet):
    eth_c = Ethernet(packet)
    print('Destination MAC : ' + eth_c.header.destination_mac_address + ' Source MAC : ' + eth_c.header.source_mac_address + ' Protocol : ' + str(eth_c.header.protocol) + ' Header Size (Bytes) : ' + str(eth_c.header.size) + ' Data Size (Bytes) : ' + str(eth_c.data.size)) 

    if eth_c.header.protocol == InternetType.IPv4:
        ip_c = IP(eth_c.data.value)
        print('Version : ' + str(ip_c.header.version) + ' IP Header Length : ' + str(ip_c.header.ihl) + ' TTL : ' + str(ip_c.header.time_to_live) + ' Protocol : ' + str(ip_c.header.protocol) + ' Source Address : ' + str(ip_c.header.source_ip_address) + ' Destination Address : ' + str(ip_c.header.destination_ip_address) + ' Header Size (Bytes) : ' + str(ip_c.header.size) + ' Data Size (Bytes) : ' + str(ip_c.data.size))
        
        if ip_c.header.protocol == TransportType.TCP:
            tcp_c = TCP(ip_c.data.value)
            print('Source Port : ' + str(tcp_c.header.source_port) + ' Dest Port : ' + str(tcp_c.header.destination_port) + ' Sequence Number : ' + str(tcp_c.header.sequence) + ' Acknowledgement : ' + str(tcp_c.header.acknowledgement) + ' TCP header length : ' + str(tcp_c.header.header_length) + ' Header Size (Bytes) : ' + str(tcp_c.header.size) + ' Data Size (Bytes) : ' + str(tcp_c.data.size))
            
        elif ip_c.header.protocol == TransportType.ICMP:
            icmp_c = ICMP(ip_c.data.value)
            print('Type : ' + str(icmp_c.header.type) + ' Code : ' + str(icmp_c.header.code) + ' Checksum : ' + str(icmp_c.header.checksum))
            
        elif ip_c.header.protocol == TransportType.UDP:
            upd_c = UDP(ip_c.data.value)
            print('Source Port : ' + str(upd_c.header.source_port) + ' Dest Port : ' + str(upd_c.header.destination_port) + ' Length : ' + str(upd_c.header.length) + ' Checksum : ' + str(upd_c.header.checksum))
            
        else:
            print('Protocol other than TCP/UDP/ICMP')
            
        print("")
    

def recv_pkts(data):
    try:
        read(data)
    except KeyboardInterrupt:
        exit('keyboard exit')
    except:
        exit('crap ... something went wrong')

provider = create(ProviderType.Socket)
devices = provider.get_all_devices()

print(devices)
	
dev = raw_input("Enter device name to sniff : ")
provider.set_device(dev)
	
print "Sniffing device " + dev
print("Sniffing device " + provider.device)
provider.loop(recv_pkts)