from .sniffing import network_packets
from .variables import set_packets_number


def clear_table_widget(table_widget):
    table_widget.setRowCount(0)
    # initialize variable like we just started the program
    set_packets_number(0)
    network_packets.clear()
