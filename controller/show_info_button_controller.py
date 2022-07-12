from .sniffing import (network_packets, get_ethernet_information, get_ip_information, get_ipv6_information,
    get_arp_information, get_tcp_information, get_udp_information, get_icmp_information, get_icmpv6_information,
    get_raw_data)
from PyQt5.QtWidgets import *


def show_info_according_to_selected_row(current_row, list_widget):
    if current_row != -1:

        list_widget.clear()
        # find the packet in all packets
        packet = network_packets[current_row]

        # get layer info of the packet
        ethernet_layer_info = get_ethernet_information(packet)
        network_layer_info = get_network_layer_info(packet)
        transport_layer_info = get_transport_layer_info(packet)
        raw_data = get_raw_data(packet)

        # show it to user
        list_widget.addItem(QListWidgetItem(str(ethernet_layer_info) + '\n'))
        list_widget.addItem(QListWidgetItem(str(network_layer_info) + '\n'))
        list_widget.addItem(QListWidgetItem(str(transport_layer_info) + '\n'))
        list_widget.addItem(QListWidgetItem(str(raw_data) + '\n'))


def get_network_layer_info(packet):
    # save all network layer get info methods as a list
    all_network_layer_get_info_methods = [get_ip_information, get_ipv6_information, get_arp_information]
    # try to get info from correct method
    for get_info in all_network_layer_get_info_methods:

        info = get_info(packet)
        # we found right protocol
        if info != '':
            return info


def get_transport_layer_info(packet):
    # save all transport layer get info methods as a list
    all_transport_layer_get_info_methods = [get_tcp_information, get_udp_information, get_icmp_information,
                                            get_icmpv6_information]
    # try to get info from correct method
    for get_info in all_transport_layer_get_info_methods:

        info = get_info(packet)
        # we found right protocol
        if info != '':
            return info
