# condition of sniffing loop
check_thread = True
# counting number of packets
packets_number = 0
previous_packets_number = 0


def set_check_thread(value: bool):
    global check_thread
    check_thread = value


def get_check_thread():
    global check_thread
    return check_thread


def set_packets_number(value: int):
    global packets_number
    packets_number = value


def get_packet_number() -> int:
    global packets_number
    return packets_number


def set_previous_packets_number(value: int):
    global previous_packets_number
    previous_packets_number = value


def get_previous_packet_number() -> int:
    global previous_packets_number
    return previous_packets_number
