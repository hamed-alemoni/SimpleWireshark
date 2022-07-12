class Ethernet:
    # save ethernet header info
    def __init__(self, destination_mac_address, source_mac_address, type):

        self.destination_mac_address = destination_mac_address
        self.source_mac_address = source_mac_address
        self.type = type

    def __repr__(self):
        return f'(Ethernet) Destination Mac Address : {self.destination_mac_address} Source Mac Addresss : {self.source_mac_address} Type : {self.type}'

