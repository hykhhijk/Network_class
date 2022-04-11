import socket
import struct
import binascii



class Udphdr:
    def __init__(self, Source, Destination, Length, Checksum):
        self.Soruce= Source
        self.Destination= Destination
        self.Length= Length
        self.Checksum= Checksum
    def pack_Udphdr(self):
        query = struct.pack("!HH", self.Soruce, self.Destination)
        query += struct.pack("!HH", self.Length, self.Checksum)
        return query
    def unpack_Udphdr(self, query):
        header = struct.unpack("!HHHH", query)
        return header


    def getSrcPort(self, query):
        header = struct.unpack("!HHHH", query)
        Srcport = header[0]
        return Srcport
    def getDstPort(self, query):
        header = struct.unpack("!HHHH", query)
        DstPort = header[1]
        return DstPort
    def getLength(self, query):
        header = struct.unpack("!HHHH", query)
        Length = header[2]
        return Length
    def getChecksum(self, query):
        header = struct.unpack("!HHHH", query)
        Checksum = header[3]
        return Checksum





if __name__ == "__main__":
    header = Udphdr(5555, 80, 1000, 0xFFFF)
    query = header.pack_Udphdr()
    print(binascii.b2a_hex(query))
    message = header.unpack_Udphdr(query)
    print(message)
    Source = header.getSrcPort(query)
    Destination = header.getDstPort(query)
    Length = header.getLength(query)
    Checksum = header.getChecksum(query)
    print("Source Port:{} Destination Port:{} Length:{} Chechsum:{}"
    .format(Source, Destination, Length, Checksum))


