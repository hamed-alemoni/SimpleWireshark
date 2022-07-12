class BaseIcmp:
    def __init__(self, title, type, code, checksum):
        self.type = type
        self.code = code
        self.checksum = checksum
        self.title = title

    def __repr__(self):
        return f'({self.title}) Type : {self.type} Code : {self.code} Checksum : {self.checksum}'


class Icmp(BaseIcmp):
    # save icmp header info
    def __init__(self, type, code, checksum, identifier, sequence_number):
        BaseIcmp.__init__(self, 'ICMP', type, code, checksum)
        self.identifier = identifier
        self.sequence_number = sequence_number

    def __repr__(self):
        return BaseIcmp.__repr__(self) + f' Identifier : {self.identifier}' \
                                         f' Sequence Number : {self.sequence_number}'


# in this class we get Icmpv6ndNeighborSolicitation and ICMPv6NDOptSrcLLAddr info as a one class
class Icmpv6(BaseIcmp):
    # save icmpv6nd_NS header info
    def __init__(self, icmpv6nd_type, code, checksum, reserved, target_address, icmpv6NDOptSrcLLAddr_type, length,
                 link_layer_address_of_the_neighbour):
        BaseIcmp.__init__(self, 'ICMPv6_ND', icmpv6nd_type, code, checksum)
        self.reserved = reserved
        self.target_address = target_address
        self.icmpv6NDOptSrcLLAddr_type = icmpv6NDOptSrcLLAddr_type
        self.length = length
        self.link_layer_address_of_the_neighbour = link_layer_address_of_the_neighbour

    def __repr__(self):
        return BaseIcmp.__repr__(self) + f' Reserved : {self.reserved} Target Address : {self.target_address}' \
                                         f'\n(ICMPv6NDOptSrcLLAddr) icmpv6NDOptSrcLLAddr_type : {self.icmpv6NDOptSrcLLAddr_type} Length : {self.length}' \
                                         f' Link Layer Address Of The Neighbour : {self.link_layer_address_of_the_neighbour}'
