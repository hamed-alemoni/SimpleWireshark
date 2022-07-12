class Ip:
    # save ip header info
    def __init__(self, version, internet_header_length, type_of_service, header_length, id, flags, frag, time_to_live,
                 protocol_number, checksum, source_ip, destination_ip, options: list):
        self.version = version
        self.internet_header_length = internet_header_length
        self.type_of_service = type_of_service
        self.header_length = header_length
        self.id = id
        self.flags = flags
        self.frag = frag
        self.time_to_live = time_to_live
        self.protocol_number = protocol_number
        self.checksum = checksum
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.options = options

    def __repr__(self):
        return f'(IP)Version : {self.version} Internet Header Length : {self.internet_header_length} Source IP : {self.source_ip} ' \
               f'Destination IP : {self.destination_ip} TTL : {self.time_to_live} Protocol Number : {self.protocol_number}' \
               f' Length : {self.header_length} Frag : {self.frag} ID : {self.id} Flag : {self.flags}'


class Ipv6:
    # save ipv6 header info
    def __init__(self, version, traffic_class, flow_label, payload_length, next_header, hop_limit, source_ip,
                 destination_ip):
        self.version = version
        self.traffic_class = traffic_class
        self.flow_label = flow_label
        self.payload_length = payload_length
        self.next_header = next_header
        self.hop_limit = hop_limit
        self.source_ip = source_ip
        self.destination_ip = destination_ip

    def __repr__(self):
        return f'(IP) Version : {self.version} Traffic Class : {self.traffic_class} Flow Label : {self.flow_label} ' \
               f'Payload Length : {self.payload_length} Next Header : {self.next_header} Hop Limit : {self.hop_limit} ' \
               f'Source Ip : {self.source_ip} Destination Ip : {self.destination_ip} '
