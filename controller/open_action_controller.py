from PyQt5.QtWidgets import *
from .sniffing import read_pcap_file
from .table_widget_contoller import write_info_in_table_widget_format


def open_pcap_file(table_widget):
    filename = QFileDialog.getOpenFileName(None, 'Open File')
    packets = read_pcap_file(filename[0])
    for index in range(len(packets)):
        write_info_in_table_widget_format(table_widget, packets[index], index + 1)
