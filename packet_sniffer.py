print("Program Started")

from scapy.all import sniff

def show_packet(packet):
    print(packet.summary())

print("Sniffer Running... Capturing 5 packets")

sniff(count=5, prn=show_packet)

