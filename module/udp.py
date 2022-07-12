class Udp:
    # save udp header info
    def __init__(self, source_port, destination_port, header_length, checksum):
        self.source_port = source_port
        self.destination_port = destination_port
        self.header_length = header_length
        self.checksum = checksum

    def __repr__(self):
        return f'(UDP)Source Port : {self.source_port} Destination Port : {self.destination_port} Length : {self.header_length} Checksum : {self.checksum}'
