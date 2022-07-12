from PyQt5.QtWidgets import *
from .sniffing import get_ip_information, get_ipv6_information, get_arp_information


def set_column_names(table_widget, names: list):
    for i in range(len(names)):
        table_widget.setHorizontalHeaderItem(i, QTableWidgetItem(str(names[i])))


def write_info_in_table_widget_format(table_widget, packet: list, packet_number: int):
    row = packet_number - 1
    # get the packet
    packet = packet[0]

    table_widget.setRowCount(packet_number)
    # get primary information
    info = determine_network_layer_protocol(packet)
    # if there is info show it to user
    if info is not None:
        table_widget.setItem(row, 0, QTableWidgetItem(str(packet_number)))
        table_widget.setItem(row, 1, QTableWidgetItem(info[0]))
        table_widget.setItem(row, 2, QTableWidgetItem(info[1]))
        table_widget.setItem(row, 3, QTableWidgetItem(info[2]))
        table_widget.setItem(row, 4, QTableWidgetItem(info[3]))


def determine_network_layer_protocol(packet):
    info = []

    # we get ipv4 header info if it doesn't exist we get ipv6 header info instead
    protocol = get_ip_information(packet)

    # try ipv6 if there is no ipv4 else we extract ipv4 info
    if protocol == '':
        protocol = get_ipv6_information(packet)
    else:
        info = save_extracted_info(protocol.version, protocol.source_ip, protocol.destination_ip,
                                   determine_protocol_name(protocol.protocol_number))
        return info

    # try arp if there is no ipv6 else we extract ipv6 info
    if protocol == '':
        protocol = get_arp_information(packet)
    else:
        info = save_extracted_info(protocol.version, protocol.source_ip, protocol.destination_ip,
                                   determine_protocol_name(protocol.next_header))
        return info

    # try ... if there is no arp else we extract arp info
    if protocol == '':
        pass
    else:
        info = save_extracted_info(determine_protocol_name(protocol.protocol_type), protocol.protocol_source_address,
                                   protocol.protocol_destination_address, 'ARP')
        return info

    return None


def save_extracted_info(version, source_ip, destination_ip, protocol_name):
    info = [str(version), str(source_ip), str(destination_ip), str(protocol_name)]
    return info


def determine_protocol_name(protocol_number: int) -> str:
    if protocol_number == 0:
        return 'HOPOPT'
    elif protocol_number == 1:
        return 'ICMP'
    elif protocol_number == 2:
        return 'IGMP'
    elif protocol_number == 3:
        return 'GGP'
    elif protocol_number in (2048, 4):
        return 'IPv4'
    elif protocol_number == 5:
        return 'ST'
    elif protocol_number == 6:
        return 'TCP'
    elif protocol_number == 17:
        return 'UDP'
    elif protocol_number == 58:
        return 'ICMPv6'
