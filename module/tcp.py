class Tcp:
    # save tdp header info
    def __init__(self, source_port, destination_port, sequence_number, acknowledge_number, data_offset, reserved, flags,
                 window_size, checksum, urgent_pointer, header_length, options: list):
        self.source_port = source_port
        self.destination_port = destination_port
        self.sequence_number = sequence_number
        self.acknowledge_number = acknowledge_number
        self.data_offset = data_offset
        self.reserved = reserved
        self.flags = flags
        self.window_size = window_size
        self.checksum = checksum
        self.urgent_pointer = urgent_pointer
        self.header_length = header_length
        self.options = options

    def __repr__(self):
        return f'(TCP)Source Port : {self.source_port} Destination Port : {self.destination_port} Sequence Number : {self.sequence_number}' \
               f' ACK Number : {self.acknowledge_number} Data Offset : {self.data_offset} Reserved : {self.reserved}' \
               f' Flags : {self.flags} Length Of Window : {self.window_size} Checksum : {self.checksum}' \
               f' Urgent Pointer : {self.urgent_pointer} Length : {self.header_length}'
