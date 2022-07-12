class Arp:
    # save arp header info
    def __init__(self, hardware_type, protocol_type, hardware_length, protocol_length, operation,
                 hardware_source_address, protocol_source_address, hardware_destination_address,
                 protocol_destination_address):
        self.hardware_type = hardware_type
        self.protocol_type = protocol_type
        self.hardware_length = hardware_length
        self.protocol_length = protocol_length
        self.operation = operation
        self.hardware_source_address = hardware_source_address
        self.protocol_source_address = protocol_source_address
        self.hardware_destination_address = hardware_destination_address
        self.protocol_destination_address = protocol_destination_address

    def __repr__(self):
        return f'(ARP) Hardware Type : {self.hardware_type} Protocol Type : {self.protocol_type} Hardware Length : {self.hardware_length} ' \
               f'Protocol Length : {self.protocol_length} Operation : {self.operation} ' \
               f'Hardware Source Address : {self.hardware_source_address} Protocol Source Address : {self.protocol_source_address} ' \
               f'Hardware Destination Address : {self.hardware_destination_address} Protocol Destination Address : {self.protocol_destination_address}'
