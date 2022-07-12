from scapy.all import *

# appending a path
from module.udp import Udp
from module.tcp import Tcp
from module.ip import Ip
from module.ip import Ipv6
from module.arp import Arp
from module.icmp import Icmp, Icmpv6
from module.ethernet import Ethernet

network_packets = []


# sniffing network till count number of packet
def sniffing():
    global network_packets
    count = 1
    network_packet = sniff(count=count)
    network_packets.append(network_packet[0])
    return network_packet


def save_info(filename):
    global network_packets

    fullname = filename + '.pcap'

    wrpcap(fullname, network_packets)

# extract ethernet header info save it in a list as a Ethernet object
def get_ethernet_information(packet):
    try:
        ethernet = Ethernet(packet[Ether].dst, packet[Ether].src, packet[Ether].type)
    except IndexError:
        ethernet = ''

    return ethernet


# extract ip header info save it in a list as a Ip object
def get_ip_information(packet):
    try:
        ip = Ip(packet[IP].version, packet[IP].ihl, packet[IP].tos, packet[IP].len, packet[IP].id, packet[IP].flags,
                packet[IP].frag, packet[IP].ttl, packet[IP].proto, packet[IP].chksum, packet[IP].src, packet[IP].dst,
                packet[IP].options)
    except IndexError:
        ip = ''

    return ip


# extract tcp header info save it in a list as a Tcp object
def get_tcp_information(packet):
    try:
        tcp = Tcp(packet[TCP].sport, packet[TCP].dport, packet[TCP].seq, packet[TCP].ack, packet[TCP].dataofs,
                  packet[TCP].reserved, packet[TCP].flags, packet[TCP].window, packet[TCP].chksum,
                  packet[TCP].urgptr, len(packet[TCP]), packet[TCP].options)
    except IndexError:
        tcp = ''

    return tcp


# extract udp header info save it in a list as a Udp object
def get_udp_information(packet):
    try:
        udp = Udp(packet[UDP].sport, packet[UDP].dport, packet[UDP].len, packet[UDP].chksum)
    except IndexError:
        udp = ''

    return udp


def get_icmp_information(packet):
    try:
        icmp = Icmp(packet[ICMP].type, packet[ICMP].code, packet[ICMP].chksum, packet[ICMP].id, packet[ICMP].seq)
    except IndexError:
        icmp = ''

    return icmp


def get_icmpv6_information(packet):
    try:
        icmpv6 = Icmpv6(packet[ICMPv6ND_NS].type, packet[ICMPv6ND_NS].code, packet[ICMPv6ND_NS].cksum,
                        packet[ICMPv6ND_NS].res, packet[ICMPv6ND_NS].tgt,
                        packet[ICMPv6NDOptSrcLLAddr].type, packet[ICMPv6NDOptSrcLLAddr].len,
                        packet[ICMPv6NDOptSrcLLAddr].lladdr)
    except IndexError:
        icmpv6 = ''

    return icmpv6


def get_ipv6_information(packet):
    try:
        ipv6 = Ipv6(packet[IPv6].version, packet[IPv6].tc, packet[IPv6].fl, packet[IPv6].plen, packet[IPv6].nh,
                    packet[IPv6].hlim, packet[IPv6].src, packet[IPv6].dst)
    except IndexError:
        ipv6 = ''

    return ipv6


def get_arp_information(packet):
    try:
        arp = Arp(packet[ARP].hwtype, packet[ARP].ptype, packet[ARP].hwlen, packet[ARP].plen,
                  'who-has' if packet[ARP].op == 1 else packet[ARP].op,
                  packet[ARP].hwsrc, packet[ARP].psrc, packet[ARP].hwdst, packet[ARP].pdst)
    except IndexError:
        arp = ''

    return arp


def get_raw_data(packet):
    try:
        raw_data = packet[Raw].load
    except:
        raw_data = ''

    return raw_data
