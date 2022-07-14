from .save_as_action_controller import save_as_pcap_files
from .sniffing import save_info


def save_pcap_file(file_name):
    if not file_name:
        return save_as_pcap_files()
    else:
        save_info(file_name)
        return file_name
