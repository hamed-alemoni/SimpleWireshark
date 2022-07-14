from .variables import get_packet_number
from PyQt5.QtWidgets import *
from .sniffing import save_info


def save_as_pcap_files():
    if get_packet_number() != 0:

        current_file_name = open_file_dialog()

        if current_file_name:

            current_file_name = remove_file_format(current_file_name)

            save_info(current_file_name)

            return current_file_name


def open_file_dialog():
    # create a file dialog and open it
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    # user choose name and format for the file
    current_file_name, _ = QFileDialog.getSaveFileName(None,
                                                       "Save File", "", "Packet Capture(*.pcap)",
                                                       options=options)
    return current_file_name


def remove_file_format(file_name):
    # if user type .pcap with filename we remove .pcap from it
    if '.' in file_name:
        file_name = file_name[:file_name.index('.')]

    return file_name
